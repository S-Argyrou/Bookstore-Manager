#======================== Import modules ========================#

import tkinter as tk
from tkinter import ttk
from my_functions import *
from tkinter import messagebox

#======================== Classes ========================#

class MainFrame(ttk.Frame):
    """ Create the main container that inherites from the Frame class."""
    
    def __init__(self, parent):
        """Initialise attributes of parent class."""
        # Call super function.
        super().__init__(master=parent)
        
        # Give the main frame relative values to make it responsive.
        # Place it in the centre of the main window.
        self.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.98, anchor="center")

        # Instantiate inner frames.
        self.top_frame = TopFrame(self)
        self.bottom_frame = BottomFrame(self)
        self.b_right_frame = BotRightFrame(self)       
        

class TopFrame(ttk.Frame):
    """ Create the top frame that inherites from the Frame class."""
    
    def __init__(self, parent):
        
        """Initialise attributes of parent class."""
        # Call super function.
        super().__init__(parent)

        # Create layout grid to neatly place widgets.
        # Establish how many units(weight) the widgets will occupy in the grid.
        # Set widgets to occupy the same amount of space per unit.        
        self.columnconfigure((1,2,4,5,7,8,9),weight=2, uniform="a")
        self.columnconfigure((0,3,6),weight=1, uniform="a")
        self.rowconfigure((0,1,2), weight=1, uniform="a")
        
        # Place the top frame.
        # Give it relative dimensions to make it responsive.
        self.place(x=0, y=0, relwidth=1, relheight=0.3)

        # Make widgets accessible to functions outside the classes.
        global label1, entry1, label2, entry2, label3, entry3

        # Create and place widgets inside the frame.
        # Make entries responsive, to store (get) into a variable the content typed. 
        label1= ttk.Label(self, text="Title")
        entry1= ttk.Entry(self, textvariable=title_text)
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1, columnspan=2, sticky="ew")
        
        label2= ttk.Label(self, text="Author") 
        entry2= ttk.Entry(self, textvariable=author_text)
        label2.grid(row=0, column=3)
        entry2.grid(row=0, column=4, columnspan=2, sticky="ew")
        
        label3= ttk.Label(self, text="Quantity") 
        entry3= ttk.Entry(self, textvariable=qnty_text)
        label3.grid(row=0, column=6)
        entry3.grid(row=0, column=7, sticky="ew")            
    

class BottomFrame(ttk.Frame):
    """ Create the bottom frame that inherites from the Frame class."""
    
    def __init__(self, parent):
        
        """Initialise attributes of parent class."""
        # Call super function.
        super().__init__(parent)
        
        # Place the bottom frame.
        # Give it relative dimensions to make it responsive.
        self.place(x=0, rely=0.3, relwidth=0.7, relheight=0.7)

        # Make table widget accessible to functions outside the classes.
        global table

        # Create table (Treeview).
        table = ttk.Treeview(self, columns=("ID","TITLE","AUTHOR", "QUANTITY"), show="headings")

        # Style the heading.
        table.heading("ID", text="ID")
        table.heading("TITLE", text="TITLE")
        table.heading("AUTHOR", text="AUTHOR")
        table.heading("QUANTITY", text="QUANTITY")

        # Place the table on the left.
        # Allow it to occupy as much space as possible.
        table.pack(side="left", fill="both", expand=True)

        # Allow entries in a table to be selected.
        table.bind("<<TreeviewSelect>>", select_button)
         
        # Create a scrollbar.  
        table_scrollbar = ttk.Scrollbar(self)

        # Place it next to the table.
        # Allow it to occupy as much space as possible.
        table_scrollbar.pack(expand=True, side="left", fill="y")

        # Connect scrollbar to table.
        table_scrollbar.configure(command=table.yview)
        table.configure(yscrollcommand=table_scrollbar.set)
        

class BotRightFrame(ttk.Frame):
    """ Create the bottom right frame that inherites from the Frame class."""

    def __init__(self, parent):
        
        """Initialise attributes of parent class."""
        # Call super function.
        super().__init__(parent)
        
        # Place the bottom right frame.
        # Give it relative dimensions to make it responsive.
        self.place(relx=0.7, rely=0.3, relwidth=0.3, relheight=0.7)

        # Create buttons and connect them to a function.
        button1 = ttk.Button(self, text="Add Book", command=add_button)
        button2 = ttk.Button(self, text="Update entry",command=update_button)
        button3 = ttk.Button(self, text="Search", command=search_button)
        button4 = ttk.Button(self, text="Delete", command=del_button)
        button5 = ttk.Button(self, text="View All", command=view_button)

        # Place buttons with some paddings.
        # Allow them to occupy as much space as possible.
        button1.pack(expand=True, fill="both", padx=10, pady=10)
        button2.pack(expand=True, fill="both", padx=10, pady=10)
        button3.pack(expand=True, fill="both", padx=10, pady=10)
        button4.pack(expand=True, fill="both", padx=10, pady=10)
        button5.pack(expand=True, fill="both", padx=10, pady=10)               


#======================== Functions ========================#

def select_button(event):
    """ Select one or multiple rows in the table, updating the entries
    everytime a new row is selected

    keyword arguments:
    event: every time a row is selected

    Returns:
    None
    """

    # Loop through every row in the table.
    for row in table.selection():

        # Store each row values into a variable.
        data = table.item(row)["values"]

        # Delete entry values of the previously selected row.
        reset()
        
        # Populate entries with values of the new selected row.        
        # title        
        entry1.insert(tk.END, data[1])

        # author
        entry2.insert(tk.END, data[2])
        
        # qnty
        entry3.insert(tk.END, data[3])

def reset():
    """ Clear all entries fields.

    keyword arguments:
    None

    Returns:
    None
    """
    # Clear fields.
    # title
    entry1.delete(0, tk.END)

    # author
    entry2.delete(0, tk.END)

    # quantity
    entry3.delete(0, tk.END)
   

def search_button():
    """ Search book by its title/author or both.

    keyword arguments:
    None

    Returns:
    None
    """
    # Check if both title and author entries are empty.
    if title_text.get() == "" and author_text.get() == "":

        # Show messagebox with warning message.
        messagebox.showwarning("Warning", "Please fill in title or author entry")

    # If at least one of the two is given, clear the table every time the button is pressed.
    else:        
        for item in table.get_children():            
            table.delete(item)

        # Store in a variable what is returned from the search function in the backend.
        data = search(title_text.get(), author_text.get())

        # Clear the entries content.
        reset()

        # Loop thorugh every row (just in case more than one value is found).
        for row in data:

            # Insert every row in the first line and le the others move down.
            table.insert(parent="", index=0, values=row)


def add_button():
    """ Add a book in the database and show it in the table.

    keyword arguments:
    None

    Returns:
    None
    """
    # Check if all entries (title,author and quantity) are empty. 
    if title_text.get() == "" or author_text.get() == "" or qnty_text.get() == "":

        # If so, show messagebox with warning message.
        messagebox.showwarning("Warning", "Please fill in all the entries")

    # If all entries have been given, check from backend if the database exists or not.
    else:
        create_db()

        # Call the add_book function in the backend to update the databse.
        add_book(title_text.get(), author_text.get(), qnty_text.get())

        # Store in a variable the values of the table entries.
        data= (id_int.get(), title_text.get(), author_text.get(), qnty_text.get())

        # Update also the treeview, by inserting the just-added book at the end.
        table.insert(parent="", index=tk.END, values=data)

        # Show the updated catalogue and print a success message.
        view_button()
        messagebox.showinfo("Success", "One item has been added")

        # Clear the entries content.
        reset()
    
         
def update_button():
    """ Update book specifications, both in table and database.

    keyword arguments:
    None

    Returns:
    None    
    """

    # Loop through every row selected.
    for row in table.selection():

        # Store the values (returned as tuple) of the row in a variable.
        data = table.item(row)["values"]

        # Assign to variable book_id the first element of the row.
        book_id = data[0]

        # Assign to another variable the values of the row.
        selected = table.focus()    

        # Update the selected row with the new values given.
        table.item(selected, values=(book_id, title_text.get(), author_text.get(), qnty_text.get()))

        # Call update_book function in backend and pass the new values.
        update_book(book_id, title_text.get(), author_text.get(), qnty_text.get())

        # Show success message
        messagebox.showinfo("Success", "Record updated")

        # Clear entries.
        reset()
        
def update_book_id():
    """ Update book id in table and database.
    Use when a row is deleted, to restore ascending oreder of books IDs.
    
    keyword arguments:
    None

    Returns:
    None
    """
    # Store the database content in a variable.
    data = view_catalogue()

    # Enumerate each row of the content, with first row index being equal to 1.
    for index, row in enumerate(data,1):

        # Set the new ID equal to the index and old ID equal to first element in row. 
        new_id = index
        old_id = row[0]

        # Call update_id from backend and pass the new ID and old ID.
        update_id(new_id, old_id)

def del_button():
    """ Delete a selected book from the database and the table.

    keyword arguments:
    None

    Returns:
    None
    """
    # Try to execute this code first.
    try:

        # Loop through every selected row.
        for row in table.selection():

            # Store the values (returned as tuple) of the row in a variable.
            data = table.item(row)["values"]            

            # Set the book ID equal to first element in the row. 
            book_id = data[0]

            # Delete the row from the table-
            table.delete(row)

            # Call delete_book function from backend, to delete item from the database as well.
            delete_book(book_id)

            # Show success message
            messagebox.showinfo("Success", "One item has been deleted")

        # Update book ID, show all catalogue and clear entries fields.
        update_book_id()
        view_button()    
        reset()

    # Raise exception if database does not exist.   
    except sqlite3.OperationalError:
        messagebox.showwarning("Warning", "The inventory does not exists.")

def view_button():
    """ Display all databse content in the table.

    keyword arguments:
    None

    Returns:
    None
    """
    
    # Try to execute this block of code.
    try:

        # Clear all entries in the table every time the button is pressed.
        for item in table.get_children():
           table.delete(item)

        # Store the database content in a variable.
        data = view_catalogue()

        # Loop through every row of the contnet, inserting it at the end of the table each time.
        for row in data:  
            table.insert(parent="", index=tk.END, values=row)

    # Raise exception if database does not exist. 
    except sqlite3.OperationalError:
        messagebox.showwarning("Warning", "The inventory does not exist yet.")  

 
#======================== Main ========================#

# Create main window and give it a title.
window = tk.Tk()
window.title("Bookstore Manager")

# Set window minimum size.
window.minsize(1300,500)

# Specify variable types for entries.
entry_text= tk.StringVar()
id_int = tk.IntVar()
title_text= tk.StringVar()
author_text= tk.StringVar()
qnty_text= tk.StringVar()

# Instantiate a main frame widget inside the window.
MainFrame(window)
    

# Run the app.
window.mainloop()

