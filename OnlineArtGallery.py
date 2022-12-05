import tkinter as tk
from tkinter import *

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
    labl_0 = Label(data_enter, text="Customer Entry Form", width=20, font=("bold", 50))
    labl_0.pack()
    labl_1 = Label(data_enter, text="Full Name", width=40, font=("bold", 20))
    labl_1.place(x=250,y=130)
    entry_1 = tk.Entry(data_enter)
    entry_1.place(x=575, y=130)
    labl_2 = Label(data_enter, text="Art Title", width=40, font=("bold", 20))
    labl_2.place(x=250, y=180)
    entry_02 = tk.Entry(data_enter)
    entry_02.place(x=575, y=180)
    labl_3 = Label(data_enter, text="Phone Number", width=40, font=("bold", 20))
    labl_3.place(x=245, y=230)
    entry_03 = tk.Entry(data_enter)
    entry_03.place(x=575, y=230)
    labl_4 = Label(data_enter, text="Address", width=40, font=("bold", 20))
    labl_4.place(x=250, y=280)
    entry_04 = tk.Entry(data_enter)
    entry_04.place(x=575, y=280)
    labl_5 = Label(data_enter, text="Amount", width=40, font=("bold", 20))
    labl_5.place(x=250, y=330)
    entry_05 = tk.Entry(data_enter)
    entry_05.place(x=575, y=330)
    labl_6 = Label(data_enter, text="Email Address", width=40, font=("bold", 20))
    labl_6.place(x=245, y=380)
    entry_06 = tk.Entry(data_enter)
    entry_06.place(x=575, y=380)
    Button(data_enter, text='Submit', width=20, bg='brown', fg='black').place(x=575, y=480)


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

    s = tk.Style()
    s.theme_use('clam')

    # Add a Treeview widget
    tree = tk.Treeview(artist_window, column=("c1", "c2", "c3"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="FName")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="LName")

    tree.insert('', 'end', text="1", values=('1', 'Joe', 'Nash'))
    tree.insert('', 'end', text="2", values=('2', 'Emily', 'Mackmohan'))
    tree.insert('', 'end', text="3", values=('3', 'Estilla', 'Roffe'))
    tree.insert('', 'end', text="4", values=('4', 'Percy', 'Andrews'))
    tree.insert('', 'end', text="5", values=('5', 'Stephan', 'Heyward'))

    tree.pack()


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
