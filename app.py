from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# your code goes between window and window.mainloop
window = Tk()

window.title('Writy')
window.configure(background = 'gray1')

# function for saving file
def save(event):
	with open('text.txt', 'w') as file:
		file.write(text1.get("1.0",'end-1c'))
		
# function for opening file
def openfile(event):
    file = filedialog.askopenfilename()
    f = open(file)
    text1.insert(1.0, f.read())

# text area to write
text1 = Text(window, bg = 'gray1', fg = 'white', insertbackground = 'white')
text1.focus_force() # give focus to text area
text1.bind('<Control-s>', save)
text1.bind('<Control-o>', openfile)
text1.bind('<Control-q>', lambda e: window.destroy())
text1.grid(row = 2, column = 0, columnspan = 50, padx = 5, pady = 5)

window.mainloop()
