import tkinter as tk   # python3
import tkinter as tk   # python
from PIL import ImageTk, Image
import speech_recognition as sr
import sys


TITLE_FONT = ("Helvetica", 18, "bold")


def speech():
    i = 0
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    print(alphabet[0])
    asd = ""
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
            # instead of r.recognize_google(audio)
            asd = r.recognize_google(audio)
            print("You said: " + asd)
            if asd == "yes":
                print("you did it")
            if asd == alphabet[1]:
                i += 1
                print(i)
            # asd = ""
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        asd = ""

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes("-fullscreen", True)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F,geometry in zip((StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix), ('1940x800', '500x500', '800x500', '1940x800', '1940x800', '1940x800', '1940x800')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            # store the frame and the geometry for this frame
            self.frames[page_name] = (frame, geometry)

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame, geometry = self.frames[page_name]
        # change geometry of the window
        self.update_idletasks()
        self.geometry(geometry)
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fname = "coba2.gif"
        cv = tk.Canvas(self, bg="pink")
        cv.pack(side='top', fill='both', expand='yes')
        img = ImageTk.PhotoImage(file = "C:\\Users\\Shintia Tamara\\PycharmProjects\\ProjectAI\\coba2.gif")
        cv.create_image(10, 10, image = img, anchor = "nw")
        btn1 = tk.Button(cv, text="QUIT", height=2, width=20, bg="#686DCE", borderwidth=0,
                      fg="white", font=('Sans', '10', 'bold'))
        btn1.pack(side='right', padx=50, pady=50, anchor='se')
        btn2 = tk.Button(cv, text="START", height=2,command=lambda: controller.show_frame("PageSix"), width=20, bg="#686DCE", borderwidth=0, fg="white",
                      font=('Sans', '10', 'bold'))
        btn2.pack(side='right', padx=5, pady=50, anchor='se')


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        letter = tk.Label(self, text="E", font=("Helvetica", 432))
        letter.pack(side="bottom", expand="YES")



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        letter = tk.Label(self, text="F P", font=("Helvetica", 216))
        letter.pack(side="bottom", expand="YES")


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        letter = tk.Label(self, text="T O Z", font=("Helvetica", 152))
        letter.pack(side="bottom", expand="YES")


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        letter = tk.Label(self, text="L P E D", font=("Helvetica", 108))
        letter.pack(side="bottom", expand="YES")


class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        letter = tk.Label(self, text="P E C F D", font=("Helvetica", 87))
        letter.pack(side="bottom", expand="YES")


class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        letter = tk.Label(self, text="E D F C Z P", font=("Helvetica", 65))
        letter.pack(side="bottom", expand="YES")


if __name__ == "__main__":
    app = SampleApp()
    # if(app==p)
    app.mainloop()