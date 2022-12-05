import tkinter as tk
from tkinter import *

import mysql.connector

db = mysql.connector.connect(user='root', password='flYing2024$',
                             host='localhost',
                             database='ArtGallery')
my_conn = db.cursor()

window = tk.Tk()

window.geometry("650x250")
window.attributes('-fullscreen', True)
window.title("Main")
window.configure(bg='#006eff')

main = tk.Label(window, text="Online Art Gallery", bg="#006eff", fg="white", font=("Times", 70, "bold"))
main.pack()

search1 = tk.Entry(window, bd=5, width=30)
search1.pack()
search2 = tk.Button(window, width=10, height=2, text="Search", fg='black')
search2.pack()


def enter_info():
    data_enter = tk.Toplevel(window)
    data_enter.title("Data Entry")
    data_enter.geometry("100x100")
    label_0 = Label(data_enter, text="Customer Entry Form", width=20, font=("bold", 50))
    label_0.pack()
    label_1 = Label(data_enter, text="Full Name", width=40, font=("bold", 20))
    label_1.place(x=250, y=130)
    entry_1 = tk.Entry(data_enter)
    entry_1.place(x=575, y=130)
    label_2 = Label(data_enter, text="Art Title", width=40, font=("bold", 20))
    label_2.place(x=250, y=180)
    entry_02 = tk.Entry(data_enter)
    entry_02.place(x=575, y=180)
    label_3 = Label(data_enter, text="Phone Number", width=40, font=("bold", 20))
    label_3.place(x=245, y=230)
    entry_03 = tk.Entry(data_enter)
    entry_03.place(x=575, y=230)
    label_4 = Label(data_enter, text="Address", width=40, font=("bold", 20))
    label_4.place(x=250, y=280)
    entry_04 = tk.Entry(data_enter)
    entry_04.place(x=575, y=280)
    label_5 = Label(data_enter, text="Amount", width=40, font=("bold", 20))
    label_5.place(x=250, y=330)
    entry_05 = tk.Entry(data_enter)
    entry_05.place(x=575, y=330)
    label_6 = Label(data_enter, text="Email Address", width=40, font=("bold", 20))
    label_6.place(x=245, y=380)
    entry_06 = tk.Entry(data_enter)
    entry_06.place(x=575, y=380)

    def add_entry():
        sql = 'INSERT INTO Customer(`Customer_name`, `art_title_desired`, `phone_number`, `address`, `amount`,' \
              '`email_address`) '
        ' VALUES (%s, %s, %s, %s, %s, %s)'
        insert = (entry_1.get(), entry_02.get(), entry_03.get(), entry_04.get(), entry_05.get(), entry_06.get())
        my_conn.execute(sql, insert)
        data_enter.destroy()
        if my_conn:
            my_conn.close()

    Button(data_enter, text='Submit', width=20, bg='brown', fg='black', command=add_entry).place(x=575, y=480)


purchaseButton = tk.Button(
    text="Purchase/Sign Up",
    width=10, height=4,
    bg="#34e8eb", fg="black",
    font=("Monaco", 7),
    command=enter_info)
purchaseButton.pack()


def open_artwork():
    artwork_window = tk.Toplevel(window)
    artwork_window.configure(bg="red")
    artwork_window.title("Artwork")
    artwork_label = tk.Label(artwork_window, text="Artwork", bg="red", fg='black', font=("Times", 70, "bold"))
    artwork_label.pack()


artworkButton = tk.Button(
    window,
    text="Artwork",
    width=15, height=5,
    bg='#34e8eb', fg='black',
    font=("Monaco", 25),
    command=open_artwork)


def open_artist():
    artist_window = tk.Toplevel(window)
    artist_window.configure(bg="green")
    artist_window.title("Artist")
    artist_label = tk.Label(artist_window, text="Artist", bg="green", fg="black", font=("Times", 70, "bold"))
    artist_label.pack()


artistButton = tk.Button(
    text="Artist",
    width=15, height=5,
    bg="#34e8eb", fg="black",
    font=("Monaco", 25),
    command=open_artist)


def open_genre():
    genre_window = tk.Toplevel(window)
    genre_window.configure(bg="yellow")
    genre_window.title("Genre")
    genre_label = tk.Label(genre_window, text="Genre", bg="yellow", fg="black", font=("Times", 70, "bold"))
    genre_label.pack()


genreButton = tk.Button(
    text="Genre",
    width=15, height=5,
    bg="#34e8eb", fg="black",
    font=("Monaco", 25),
    command=open_genre)


def open_place():
    place_window = tk.Toplevel(window)
    place_window.configure(bg="orange")
    place_window.title("Place")
    place_label = tk.Label(place_window, text="Place", bg="orange", fg='black', font=("Times", 70, "bold"))
    place_label.pack()


placeButton = tk.Button(
    text="Place",
    width=15, height=5,
    bg="#34e8eb", fg="black",
    font=("Monaco", 25),
    command=open_place)

artworkButton.place(x=375, y=300)
artistButton.place(x=375, y=600)
genreButton.place(x=775, y=300)
placeButton.place(x=775, y=600)

window.mainloop()
