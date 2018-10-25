from tkinter import *

# your code goes between window and window.mainloop
window = Tk()

window.title('Writy')
window.configure(background = 'gray1')

# function for saving file
def save(event):
	with open('text.txt', 'w') as file:
		file.write(text1.get("1.0",'end-1c'))

# text area to write
text1 = Text(window, bg = 'gray1', fg = 'white', insertbackground = 'white')
text1.bind('<Return>', save)
text1.bind('<Escape>', lambda e: window.destroy())
text1.grid(row = 2, column = 0, columnspan = 50, padx = 5, pady = 5)

window.mainloop()
