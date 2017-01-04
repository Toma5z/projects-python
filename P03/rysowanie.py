from tkinter import * 



def put(x,y):
	w.create_rectangle(x,y,x+1,y+1, fill="blue")

okno_glowne = Tk()
okno_glowne.geometry('640x480+300+200')

w = Canvas(okno_glowne)
w.pack(fill=BOTH, expand=YES)

put(10,10)
put(20,20)



okno_glowne.mainloop()


