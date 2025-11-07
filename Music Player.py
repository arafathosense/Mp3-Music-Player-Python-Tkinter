from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Arafat MP3 Player')
root.geometry("600x400")
root.config(bg="#181818")

mixer.init()

# Song Listbox
songs_list = Listbox(root, bg="#1f1f1f", fg="white", font='arial 14 bold',
                     height=12, width=50, selectbackground="#00eaff", selectforeground="black", border=0)
songs_list.pack(pady=10)

# Functions
def play():
    song = songs_list.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def previous():
    p_one = songs_list.curselection()
    p_one = p_one[0] - 1
    temp = songs_list.get(p_one)
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(p_one)
    songs_list.selection_set(p_one)

def next():
    n_one = songs_list.curselection()
    n_one = n_one[0] + 1
    temp2 = songs_list.get(n_one)
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(n_one)
    songs_list.selection_set(n_one)

def add():
    temp_song = filedialog.askopenfilenames(title="Choose Song", filetypes=(("MP3 Files", "*.mp3"),))
    for s in temp_song:
        songs_list.insert(END, s)

def delete():
    curr_songs = songs_list.curselection()
    songs_list.delete(curr_songs[0])

# Button Frame
frame = Frame(root, bg="#181818")
frame.pack(pady=10)

btn_style = {"font": "arial 12 bold", "width": 7, "height":1, "bd":0}

Button(frame, text='Play', bg="#00ff84", fg="black", command=play, **btn_style).grid(row=0, column=0, padx=5)
Button(frame, text='Pause', bg="#ffaa00", fg="black", command=pause, **btn_style).grid(row=0, column=1, padx=5)
Button(frame, text='Stop', bg="#ff0059", fg="white", command=stop, **btn_style).grid(row=0, column=2, padx=5)
Button(frame, text='Resume', bg="#009dff", fg="white", command=resume, **btn_style).grid(row=0, column=3, padx=5)
Button(frame, text='Previous', bg="#8a2be2", fg="white", command=previous, **btn_style).grid(row=0, column=4, padx=5)
Button(frame, text='Next', bg="#ff00aa", fg="white", command=next, **btn_style).grid(row=0, column=5, padx=5)

# Menu
def open_menu_window():
    menu_win = Toplevel(root)
    menu_win.title("Menu")
    menu_win.geometry("200x160")
    menu_win.config(bg="#202020")



    Button(menu_win, text="Add Songs", command=add, bg="#00ff84", fg="black", font=("Arial", 12, "bold"), width=12).pack(pady=4)
    Button(menu_win, text="Delete Selected", command=delete, bg="#ff0059", fg="white", font=("Arial", 12, "bold"), width=12).pack(pady=8)
    Button(menu_win, text="Exit App", command=root.destroy, bg="#ffaa00", fg="black", font=("Arial", 12, "bold"), width=12).pack(pady=8)

my_menu = Menu(root)
root.config(menu=my_menu)
my_menu.add_command(label="Menu", command=open_menu_window)


root.mainloop()
