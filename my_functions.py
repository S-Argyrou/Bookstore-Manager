#======================== Import modules ========================#

# import modules
import sqlite3

#======================== Functions ========================#
 
def create_db():
    """ Create a database if it does not exists.

    keyword arguments:
    None

    Returns:
    None
    """
    # Connect to database file called ebookstore.db.
    db = sqlite3.connect("ebookstore.db")

    # Get a cursor object
    cursor = db.cursor()

    # If it does not exists, create a table named 'books'.
    # Pass in four parameters: id (primary Key), title, author and quantity.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books
        (id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        qty INTEGER)''')

    # Save changes and close database.
    db.commit()
    db.close()
    

def add_book(book_title, book_author, book_qty):
    """ Add a book in the database.

    keyword arguments:
    book_title (str): the title of a book,
    book_author (str): the author of a book,
    book_qty (int): the quantity of a book

    Returns:
    None
    """    
    # Connect to the database file called ebookstore.db.
    db = sqlite3.connect("ebookstore.db")

    # Get a cursor object
    cursor = db.cursor()

    # Insert the book parameters in the database.
    # Let 'id' be automatically assigned.
    cursor.execute(''' INSERT INTO books 
    VALUES(NULL,?,?,?)''',
    (book_title, book_author, book_qty))
    
    # Save changes and close database.
    db.commit()
    db.close()
    
     
def update_id(new_id, book_id):
    """ Update a book ID in the database.

    keyword arguments:    
    new_id (int): the new ID of a book to be set,
    old_id (int): the old ID of a book

    Returns:
    None
    """
    
    # Connect to the database file called ebookstore.db.
    db = sqlite3.connect("ebookstore.db")

    # Get a cursor object
    cursor = db.cursor()

    # Update the new book ID based on the old ID.
    cursor.execute("""UPDATE books
    SET id = ? 
    WHERE id = ?""",
    (new_id, book_id,))
    
    # Save changes and close database.
    db.commit()
    db.close()

    
def update_book(book_id, book_title, book_author, book_qty):
    """ Update one up to all book parameters in the database.

    keyword arguments:
    book_id (int): the ID of a book (automatically assigned),
    book_title (str): the title of a book,
    book_author (str): the author of a book,
    book_qty (int): the quantity of a book

    Returns:
    None
    """
    
    # Connect to the database file called ebookstore.db.
    db = sqlite3.connect("ebookstore.db")

    # Get a cursor object
    cursor = db.cursor()

    # Update book parameters, based on the book ID.
    cursor.execute("""UPDATE books
    SET title = ?, author = ?, qty = ?
    WHERE id = ?""",
    (book_title, book_author, book_qty, book_id,))
    
    # Save changes and close database.
    db.commit()
    db.close()
 

def delete_book(book_id):
    """ Delete a book entry in the database.

    keyword arguments:
    book_id (int): the ID of the book we want to delete (automatically assigned),
    
    Returns:
    None
    """    
    
    # Connect to the database file called ebookstore.db.
    db = sqlite3.connect("ebookstore.db")

    # Get a cursor object
    cursor = db.cursor()

    # Delete the book based on its ID.
    cursor.execute("""DELETE FROM books
    WHERE id = ?""", (book_id,))
    
    # Save changes and close database.
    db.commit()
    db.close()
    

def search(book_title, book_author):
    """ Search a book based on the two parameters provided.

    keyword arguments:  
    book_title (str): the title of a book,
    book_author (str): the author of a book

    Returns:
    Book(s) found
    """
    
    # Connect to the database file called ebookstore.db.
    db = sqlite3.connect("ebookstore.db")

    # Get a cursor object
    cursor = db.cursor()

    # Select all the items based on a particular title or author parameter.
    cursor.execute("""SELECT * FROM books
    WHERE title=? or author=?""",
    (book_title, book_author))

    # Store the results in a variable.
    found = cursor.fetchall()
    
    # Close database.
    db.close()

    # Return the results.
    return found
     
def view_catalogue():
    """ Show the whole content of the database.

    Keyword arguments:
    None
    
    Returns:
    Wwole database content
    """
    
    # Connect to the database file called ebookstore.db.
    db = sqlite3.connect("ebookstore.db")

    # Get a cursor object
    cursor = db.cursor()

    # Select the whole database content.
    cursor.execute("SELECT * FROM books")

    # Store the results in a variable.
    data = cursor.fetchall()

    # Close database.
    db.close()

    # Return whole database content.
    return data   

