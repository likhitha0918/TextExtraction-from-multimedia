from tkinter import *
from pytesseract import pytesseract
import wave, math, contextlib
import moviepy.editor as mp
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import pyttsx3 as pp
import pyqrcode
from PIL import Image


root = Tk()
root.geometry('1000x600+80+10')
root.title('TEXT EXTRACTION FROM MULTI-MEDIA')
root.resizable(0, 0)
meaning = ''
peopleimage = PhotoImage(file='people.png')
searchimage = PhotoImage(file='search.png')


timage = PhotoImage(file='t button.png')
qrimage = PhotoImage(file='qr.png')
#cimage = PhotoImage(file='c button.png')

cbimage = PhotoImage(file='text.png')
shaimage = PhotoImage(file='sha.png')
engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # [0]for male

def videotxt():
    newWindow = Toplevel(root)
    newWindow.title("VIDEO TO TEXT CONVERSION")
    newWindow.geometry("900x600")
    Label(newWindow, text="Video to text extraction window", font=('castellar', 20, 'bold'), fg='red3', bg='whitesmoke').pack()

    Label1 = Label(newWindow, text='Enter the File Name / PATH :', font=('castellar', 15, 'bold'), fg='red3', bg='whitesmoke')
    Label1.place(x=50, y=120)

    Label2 = Label(newWindow, text='Extracted Text :', font=('castellar', 15, 'bold'), fg='red3', bg='whitesmoke')
    Label2.place(x=50, y=210)

    entry = Entry(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, width=25)
    entry.place(x=420, y=110)
    entry.focus_set()

    textarea = Text(newWindow, font=('Cambria', 18, 'italic'), bd=8, relief=GROOVE, height=9, width=60, wrap='word')
    textarea.place(x=50, y=250)

    textarea1 = Text(newWindow, font=('Arial Black', 18, 'italic'), bd=8, relief=GROOVE, height=1, width=8,
                     wrap='word')
    textarea1.place(x=300, y=200)

    textarea2 = Text(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, height=1, width=14,
                     wrap='word')
    textarea2.place(x=440, y=200)
    textarea1.insert(END, " 0%")
    textarea2.insert(END, "Please wait..")

    def search():
        B = entry.get()
        transcribed_audio_file_name = "transcribed_speech.wav"
        zoom_video_file_name = B
        audioclip = AudioFileClip(zoom_video_file_name)
        audioclip.write_audiofile(transcribed_audio_file_name)
        with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
        total_duration = math.ceil(duration / 60)
        textarea2.delete("1.0", "end")
        textarea2.insert(END, "Duration :")
        timep = (total_duration,"min")
        textarea2.insert(END, "sec")
        textarea2.insert(END, timep)
        r = sr.Recognizer()
        for i in range(0, total_duration):
            print(total_duration)
            with sr.AudioFile(transcribed_audio_file_name) as source:
                audio = r.record(source, offset=i * 60, duration=60)
            f = open("transcription.txt", "a")
            print("text file opened")
            f.write(r.recognize_google(audio))
            print("Writing in file")
            f.write(" ")
        print("Completed writing")
        textarea1.delete("1.0", "end")
        textarea1.insert(END, " 100%")
        f.close()

    def text():
        fa = open("transcription.txt", "r")
        content = fa.read()
        textarea.insert(END, content)
        print(content)
        fa.close()

    def qr():
        fa = open("transcription.txt", "r")
        content = fa.read()
        print(content)
        fa.close()
        s = content
        url = pyqrcode.create(s)
        url.png('myqr.png', scale=8)
        img = Image.open('myqr.png')
        img.show()


    def erase():
        fa = open("transcription.txt", "w")
        content = fa.write()
        content.truncate()
        fa.close()


    
    searchButton = Button(newWindow, image=searchimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                          command=search)
    searchButton.place(x=750, y=100)

    textButton = Button(newWindow, image=timage, bd=0, activebackground='whitesmoke', cursor='hand2',
                          command=text)
    textButton.place(x=650, y=170)

    textButton = Button(newWindow, image=timage, bd=0, activebackground='whitesmoke', cursor='hand2', command=erase)
    Button.place(x=550, y=210)

#BACKGROUND IMAGE
bgimage = PhotoImage(file='bg.png')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)
#LABEL
enterwordLabel = Label(root, text='Text Extraction', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
enterwordLabel.place(x=280, y=20)


videototxtimage = PhotoImage(file='button_video-to-text.png')


videototxt = Button(root, image=videototxtimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=videotxt)
videototxt.place(x=350, y=300)




root.mainloop()