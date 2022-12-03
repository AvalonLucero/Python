import tkinter as tk

window = tk.Tk()

window.geometry("650x250")
window.attributes('-fullscreen', True)
window.title("Main")
window.configure(bg='#006eff')


label1 = tk.Label(window, text="Online Art Gallery", bg="#006eff", fg="white", font=("Times", 70, "bold"))
label1.pack()

search1 = tk.Entry(window, bd=5, width=30)
search1.pack()
search2 = tk.Button(window, width=10, height=2, text="Search", fg='black')
search2.pack()


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
