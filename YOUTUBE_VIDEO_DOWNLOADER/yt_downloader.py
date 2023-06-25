from tkinter import *;
from pytube import YouTube ;

root=Tk()
root.title("YOUTUBE VIDEO DOWNLOADER")
root.geometry('430x150')
root.configure(background='red')

Label(root, text="Download Youtube videos for free", font='san-serif 14 bold',bg="red").grid(row=0,column=0)
 
Label(root, text="Paste your link here", font='san-serif 15 bold',bg="red").grid(row=1,column=0)
link = Entry(root, width=70).grid(row=2,column=0)
Button(root, text='Download', font='san-serif 16 bold', bg='white',command="download").grid(row=3,column=0)
def downloadyt():
    url = YouTube(str(link.get()))
    print(url)
    video = url.streams.first
    video.download()
    Label(root, text="Downloaded", font="arial 15").pack(pady=15)
 
 
root.mainloop()
  