import tkinter as tk
from tkinter import ttk
from tkinter import *

import mysql.connector

mydb = mysql.connector.connect(user='root', password='password',
                               host='localhost',
                               database='ArtGallery')
my_conn = mydb.cursor()

window = tk.Tk()

# Main or Home Page
window.geometry("650x250")
window.attributes('-fullscreen', True)
window.title("Main")
window.configure(bg='#006eff')

main = tk.Label(window, text="Online Art Gallery", bg="#006eff", fg="white", font=("Times", 70, "bold"))
main.pack()


def primary_search():
    searched_artist = Toplevel(window)
    searched_artist.title("Searched Artist")
    searched_artist.configure(bg="black")
    searched_artist.geometry("200x200")


def search_records():
    sql_query = "SELECT * FROM artist WHERE FirstName= ?"
    vals = search1.get()
    print(vals)
    my_conn.execute(sql_query, vals)
    my_rows = my_conn.fetchall()
    print(my_rows)
    total_rows = my_conn.rowcount
    print("TOTAL ROWS: ", total_rows)
    my_conn.close()


# Search Entry for Art
search1 = tk.Entry(window, bd=5, width=30)
search1.pack()
search2 = tk.Button(window, width=10, height=2, text="Search Artist", fg='black',
                    command=lambda: [primary_search(), search_records()])
search2.pack()


def enter_info():
    data_enter = tk.Toplevel(window)
    data_enter.title("Data Entry")
    data_enter.configure(bg='purple')
    data_enter.geometry("100x100")
    label_0 = Label(data_enter, text="Customer Entry Form", width=20, font=("bold", 50), bg='purple')
    label_0.pack()
    label_1 = Label(data_enter, text="Full Name", width=40, font=("bold", 20), bg='purple')
    label_1.place(x=250, y=130)
    entry_1 = tk.Entry(data_enter)
    entry_1.place(x=575, y=130)
    label_2 = Label(data_enter, text="Art Title", width=40, font=("bold", 20), bg='purple')
    label_2.place(x=250, y=180)
    entry_02 = tk.Entry(data_enter)
    entry_02.place(x=575, y=180)
    label_3 = Label(data_enter, text="Phone Number", width=40, font=("bold", 20), bg='purple')
    label_3.place(x=245, y=230)
    entry_03 = tk.Entry(data_enter)
    entry_03.place(x=575, y=230)
    label_4 = Label(data_enter, text="Address", width=40, font=("bold", 20), bg='purple')
    label_4.place(x=250, y=280)
    entry_04 = tk.Entry(data_enter)
    entry_04.place(x=575, y=280)
    label_5 = Label(data_enter, text="Amount", width=40, font=("bold", 20), bg='purple')
    label_5.place(x=250, y=330)
    entry_05 = tk.Entry(data_enter)
    entry_05.place(x=575, y=330)
    label_6 = Label(data_enter, text="Email Address", width=40, font=("bold", 20), bg='purple')
    label_6.place(x=245, y=380)
    entry_06 = tk.Entry(data_enter)
    entry_06.place(x=575, y=380)
    # The submit button action

    def add_entry():
        search1.delete(0, END)
        data_enter.withdraw()
        try:
            sql = "INSERT INTO Customers(Customer_name, art_title_desired, phone_number, address, amount, " \
                  "email_address) VALUES (%s,%s,%s,%s,%s,%s) "
            insert = (entry_1.get(), entry_02.get(), entry_03.get(), entry_04.get(), entry_05.get(), entry_06.get())
            my_conn.execute(sql, insert)
            my_conn.commit()
            print(my_conn.rowcount, "Record inserted successfully into Customer table")
        except mysql.connector.Error as error:
            print("Failed to insert record into Customer table {}".format(error))
        finally:
            if mydb.is_connected():
                mydb.close()
                print("MySQL connection is closed")
    Button(data_enter, text='Submit', width=20, bg='brown', fg='black', command=add_entry).place(x=575, y=480)


purchaseButton = tk.Button(
    text="Purchase/Sign Up",
    width=10, height=4,
    bg="#34e8eb", fg="black",
    font=("Monaco", 7),
    command=enter_info)
purchaseButton.pack()
# Purchase button


def open_artwork():
    artwork_window = tk.Toplevel(window)
    artwork_window.configure(bg="red")
    artwork_window.title("Artwork")
    artwork_label = tk.Label(artwork_window, text="Artwork", bg="red", fg='black', font=("Times", 70, "bold"))
    artwork_label.pack()

    columns = ('Title', 'Artist_id', 'Year_made', 'Style', 'Price', 'Order_Date')
    tree = ttk.Treeview(artwork_window, column=columns, show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("Title", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("Artist_id", text="Artist ID")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("Year_made", text="Year Made")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("Style", text="Style")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("Price", text="Price")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("Order_Date", text="Order Date")
    tree.pack()
# If the artwork button is pressed


artworkButton = tk.Button(
    window,
    text="Artwork",
    width=15, height=5,
    bg='#34e8eb', fg='black',
    font=("Monaco", 25),
    command=open_artwork)
# Artwork Button


def open_artist():
    artist_window = tk.Toplevel(window)
    artist_window.configure(bg="green")
    artist_window.title("Artist")
    artist_label = tk.Label(artist_window, text="Artist", bg="green", fg="black", font=("Times", 70, "bold"))
    artist_label.pack()

    columns = ('Artist_id', 'FirstName', 'LastName', 'Birthplace', 'Age', 'Genre_type', 'Sex', 'Available_pieces')
    tree = ttk.Treeview(artist_window, column=columns, show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("Artist_id", text="Artist ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("FirstName", text="First Name")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("LastName", text="Last Name")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("Birthplace", text="Birthplace")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("Age", text="Age")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("Genre_type", text="Genre Type")
    tree.column("#7", anchor=tk.CENTER)
    tree.heading("Sex", text="Sex")
    tree.column("#8", anchor=tk.CENTER)
    tree.heading("Available_pieces", text="Available Pieces")
    tree.pack()
# If the artist button is pressed


artistButton = tk.Button(
    text="Artist",
    width=15, height=5,
    bg="#34e8eb", fg="black",
    font=("Monaco", 25),
    command=open_artist)
# Artist Button


def open_genre():
    genre_window = tk.Toplevel(window)
    genre_window.configure(bg="yellow")
    genre_window.title("Genre")
    genre_label = tk.Label(genre_window, text="Genre", bg="yellow", fg="black", font=("Times", 70, "bold"))
    genre_label.pack()

    columns = ('Type_art', 'Style_art', 'Artist_id')
    tree = ttk.Treeview(genre_window, column=columns, show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("Type_art", text="Type of Art")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("Style_art", text="Style of Art")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("Artist_id", text="Artist ID")
    tree.pack()
# If the genre button is pressed


genreButton = tk.Button(
    text="Genre",
    width=15, height=5,
    bg="#34e8eb", fg="black",
    font=("Monaco", 25),
    command=open_genre)
# Genre Button


def open_place():
    place_window = tk.Toplevel(window)
    place_window.configure(bg="orange")
    place_window.title("Place")
    place_label = tk.Label(place_window, text="Place", bg="orange", fg='black', font=("Times", 70, "bold"))
    place_label.pack()

    columns = ('Place_id', 'Exhibition_name', 'Address_held', 'Rental_price')
    tree = ttk.Treeview(place_window, column=columns, show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("Place_id", text="Place ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("Exhibition_name", text="Exhibition Name")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("Address_held", text="Address")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("Rental_price", text="Rental Price")
    tree.pack()
# If the place button is pressed


placeButton = tk.Button(
    text="Place",
    width=15, height=5,
    bg="#34e8eb", fg="black",
    font=("Monaco", 25),
    command=open_place)
# Place Button

# Placements of the four buttons
artworkButton.place(x=375, y=300)
artistButton.place(x=375, y=600)
genreButton.place(x=775, y=300)
placeButton.place(x=775, y=600)

window.mainloop()
