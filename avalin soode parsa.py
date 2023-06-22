from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
def login():
    if USER_ENTRY.get() == 'roham'and PASS_ENTRY.get() == '1388':
        root.destroy()
        win = Tk()
        win.title('big porojeh')
        win.geometry('800x400')
        win.resizable(False, False)
        scr = Scrollbar()
        scr.place(x=220, y=10, height=650)
        lst = Listbox(win)
        lst.config(xscrollcommand=scr.set, width=132, height= 15)
        scr.config(command = lst.xview)
        lst.place(x= 0,y= 250)
        bg= 'gray'
        fg= 'white'
        
    
class Window(Tk):
	lastid = 1
	def __init__(self):
		super().__init__()
		self.title("school project")
		self.geometry("600x450")
		self.resizable(False, False)

		listbox = Treeview(self, selectmode = BROWSE)
		listbox['columns'] = ("ID","Name", "Lastname", "address", "phone")
		listbox['show'] = 'headings'
		for c in listbox['columns']: listbox.column(c, width = 120)
		for i in listbox['columns']: listbox.heading(i, text = i)
		listbox.place(y = 210)

		#first row
		name_label = Label(self, text = "name:")
		name_label.place(y = 10, x = 30)

		name_entry = Entry(self, width = 15)
		name_entry.place(y = 10, x = 90)
		
		lastname_label = Label(self, text = "lastname:")
		lastname_label.place(y = 10, x = 290)

		lastname_entry = Entry(self, width = 15)
		lastname_entry.place(y = 10,x = 380)

		#second row
		address_label = Label(self, text = "address:")
		address_label.place(y = 40, x = 17)

		address_entry = Entry(self, width = 15)
		address_entry.place(y = 40, x = 90)

		phonenumber_label = Label(self, text = "phone number:")
		phonenumber_label.place(y = 40, x = 253)

		phonenumber_entry = Entry(self, width = 15)
		phonenumber_entry.place(y = 40, x = 380)

		search_info = LabelFrame(self, width = 40, text = "search for name")
		search_info.place(y = 110, x = 200)

		name_search_entry = Entry(search_info, width = 20)
		name_search_entry.pack(padx = 5, pady = 5)

		#functions
		def add():
			name = name_entry.get()
			lname = lastname_entry.get()
			addr = address_entry.get()
			phone = phonenumber_entry.get()
			if len(name) == 0 or len(lname) == 0 or len(addr) == 0 or len(phone) == 0:
				messagebox.showerror("invalid input error", "please don't add value without filling!")
			elif not phone.isdigit():
				messagebox.showerror("invalid phone number", "the phone number is not valid for registeration!")
			else:
				listbox.insert("", "end", values = (self.lastid, name, lname, addr, phone))
				self.lastid += 1

		def delete():
			try:
				selecteditem = listbox.focus()
				listbox.delete(selecteditem)
			except: messagebox.showerror("no value selected!", "select a item first!")

		def search():
			target = name_search_entry.get()

			if len(target) != 0:
				results = 0
				values = []
				for child in listbox.get_children():
					name = listbox.item(child)['values'][1]
					if str(name).lower().find(target.lower()) != -1:
						results += 1
						values.append(tuple(listbox.item(child)['values']))
						
				if results != 0:
					new_view = Toplevel(self)
					new_view.resizable(False, False)
					new_view.title("search result")

					searchbox = Treeview(new_view, selectmode = BROWSE)
					searchbox['columns'] = ("ID","Name", "Lastname", "address", "phone")
					searchbox['show'] = 'headings'
					for c in searchbox['columns']: searchbox.column(c, width = 120)
					for i in searchbox['columns']: searchbox.heading(i, text = i)
					searchbox.pack()
					for i in values:
						searchbox.insert("", "end", values = i)
					new_view.mainloop()
				else: pass
			else: pass

		def clear():
			phonenumber_entry.delete(0, 'end')
			address_entry.delete(0, 'end')
			name_entry.delete(0, 'end')
			lastname_entry.delete(0, 'end')

		#buttons area & first row
		adding_button = Button(self, text = "add", width = 13, command = lambda: add())
		adding_button.place(y = 70, x = 100)

		delete_button = Button(self, text = "delete", width = 13, command = delete)
		delete_button.place(y = 70, x = 240)

		delete_field_button = Button(self, text = "clear", width = 13, command = clear)
		delete_field_button.place(y = 70, x = 380)
		
		#second row

		search_button = Button(search_info, text = "search", width = 13, command = search)
		search_button.pack(pady = 5)

MOHEM_LABLE = Label(root, fg='black', text='@godrat_hamrah_ba_parsa_ast', font='arial 8 bold', bg='gray')
MOHEM_LABLE.place(x=10, y=320)
USER_LABLE = Label(root, fg='black', text='USER NAME: ', bg='gray')
USER_LABLE.place(x=70, y=80)
PASS_LABEL = Label(root, fg='black', text='PASSWORD: ', bg='gray')
PASS_LABEL.place(x=300, y=80)

USER_ENTRY = Entry(root)
USER_ENTRY.place(x=150, y=80)
PASS_ENTRY = Entry(root)
PASS_ENTRY.place(x=380, y=80)

LOGIN_BTN = Button(root, text='Login', font= 'arial 16 bold', width=10, command= Login)
LOGIN_BTN.place(x=100, y=200)
CANCEL_BTN = Button(root, text='Cancel', font='arial 16 bold', width=10, command=exit)
CANCEL_BTN.place(x=330, y=200)


root.config(bg='gray')
root.mainloop()
if __name__ == '__main__':
	window = Window()
	window.mainloop()
    