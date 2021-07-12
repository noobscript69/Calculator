from tkinter import *
from datetime import datetime


def click(event):
  global calValue
  text = event.widget.cget("text")
  print(text)
  if text == "=":
    if calValue.get().isdigit():
     value = int(calValue.get())
    else:
        try:
            value = eval(screen.get())
        except Exception as e:
            print(e)
            value = "Error"
    calValue.set(value)
    screen.update()
  elif text == "C":
      calValue.set("")
      screen.update()
  else:
      calValue.set(calValue.get() + text)
      screen.update()

root = Tk()
root.geometry("644x600")
root.title("vvvvvv")

root.configure(background="white")
calValue = StringVar()
calValue.set("")

screen = Entry(root, textvar=calValue, font="Lucida 20")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

frame1 = Frame(root, bg="grey")
button1 = Button(frame1, text="9", padx="28", pady="20", font="lucida 20")
button1.pack(side=LEFT, padx=18, pady=12)
button1.bind("<Button-1>", click)

button2 = Button(frame1, text="8", padx="28", pady="20", font="lucida 20")
button2.pack(side=LEFT, padx=18, pady=12)
button2.bind("<Button-1>", click)

button3 = Button(frame1, text="7", padx="28", pady="20", font="lucida 20")
button3.pack(side=LEFT, padx=18, pady=12)
button3.bind("<Button-1>", click)

button4 = Button(frame1, text="+", padx="28", pady="20", font="lucida 20")
button4.pack(side=LEFT, padx=18, pady=12)
button4.bind("<Button-1>", click)

frame1.pack()


frame1 = Frame(root, bg="grey")
button1 = Button(frame1, text="6", padx="28", pady="20", font="lucida 20")
button1.pack(side=LEFT, padx=18, pady=12)
button1.bind("<Button-1>", click)

button2 = Button(frame1, text="5", padx="28", pady="20", font="lucida 20")
button2.pack(side=LEFT, padx=18, pady=12)
button2.bind("<Button-1>", click)

button3 = Button(frame1, text="4", padx="28", pady="20", font="lucida 20")
button3.pack(side=LEFT, padx=18, pady=12)
button3.bind("<Button-1>", click)

button4 = Button(frame1, text="-", padx="28", pady="20", font="lucida 20")
button4.pack(side=LEFT, padx=18, pady=12)
button4.bind("<Button-1>", click)


frame1.pack()


frame1 = Frame(root, bg="grey")
button1 = Button(frame1, text="3", padx="28", pady="20", font="lucida 20")
button1.pack(side=LEFT, padx=18, pady=12)
button1.bind("<Button-1>", click)

button2 = Button(frame1, text="2", padx="28", pady="20", font="lucida 20")
button2.pack(side=LEFT, padx=18, pady=12)
button2.bind("<Button-1>", click)

button3 = Button(frame1, text="1", padx="28", pady="20", font="lucida 20")
button3.pack(side=LEFT, padx=18, pady=12)
button3.bind("<Button-1>", click)

button4 = Button(frame1, text="*", padx="28", pady="20", font="lucida 20")
button4.pack(side=LEFT, padx=18, pady=12)
button4.bind("<Button-1>", click)

frame1.pack()


frame1 = Frame(root, bg="grey")
button1 = Button(frame1, text="C", padx="28", pady="20", font="lucida 20")
button1.pack(side=LEFT, padx=18, pady=12)
button1.bind("<Button-1>", click)

button2 = Button(frame1, text="0", padx="28", pady="20", font="lucida 20")
button2.pack(side=LEFT, padx=18, pady=12)
button2.bind("<Button-1>", click)

button3 = Button(frame1, text="=", padx="28", pady="20", font="lucida 20")
button3.pack(side=LEFT, padx=18, pady=12)
button3.bind("<Button-1>", click)

button4 = Button(frame1, text="/", padx="28", pady="20", font="lucida 20")
button4.pack(side=LEFT, padx=18, pady=12)
button4.bind("<Button-1>", click)

frame1.pack()

root.mainloop()

