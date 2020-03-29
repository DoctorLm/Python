#/usr/bin/python
from Tkinter import *

def main():
    tk = Tk()
    canvas = Canvas(tk, width = 800, height = 600)
    canvas.pack()
    
    def moverectangle(event):
        if event.keysym == "Up":
            canvas.move(1,0,-5*8)
        elif event.keysym == "Down":
            canvas.move(1,0,5*8)
        elif event.keysym == "Left":
            canvas.move(1,-5*8,0)
        elif event.keysym == "Right":
            canvas.move(1,5*8,0)

    canvas.create_rectangle(180,180,220,220,fill="red")
    canvas.bind_all("<KeyPress-Up>",moverectangle)
    canvas.bind_all("<KeyPress-Down>",moverectangle)
    canvas.bind_all("<KeyPress-Left>",moverectangle)
    canvas.bind_all("<KeyPress-Right>",moverectangle)
    mainloop()

if __name__ == '__main__':
    main()
