from tkinter import *
from tkinter.ttk import Combobox, Checkbutton

#-------------------------------------------------------
#
#
#-------------------------------------------------------
def clicked(label, txt):
	res = "Welcome to " + txt.get()
	label.configure(text = res)
	
#-------------------------------------------------------
#
#
#-------------------------------------------------------
def main():
	window = Tk()
	window.title("Welcome Python GUI")
	
	label = Label(window, text="My Label", font=("Arial Bold", 16))
	label.grid(column=0, row=0)
	
	txt = Entry(window,width=18)
	txt.grid(column=1, row=0)

	btn = Button(window, text="Button", bg="black", fg="white", command = lambda: clicked(label,txt))
	btn.grid(column=2, row=0)
	
	combo = Combobox(window)
	combo['values'] = (1,2,3,4,5,"Text")
	combo.current(1)
	combo.grid(column=0, row=1)
	
	chk_state = BooleanVar()
	chk_state.set(False)
	chk = Checkbutton(window, text='Choose', var=chk_state)
	chk.grid(column=0, row=2)
 
	
	window.geometry('640x480')
	window.mainloop()
	
	
#-------------------------------------------------------
#
#
#-------------------------------------------------------
if __name__ == "__main__":
	main()