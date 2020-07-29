"""
A program that will store book information:
Title, Author, Year, ISBN

User can:
View all Records
Search For Entry
Add Entry
Update Entry
Delete Item
Close window

USES tkinter for FRONT END, SQLITE3 for backend
learned to use a seperate file for backend and import to front end.
learned how to connect and manipulate data from a database
"""
from tkinter import *
import backend

# FRONT END

window = Tk()
window.wm_title("BookStore")

# Button Functions
def view_command():
    resultsBox.delete(0,END)
    for result in backend.viewAll():
        resultsBox.insert(END, result)

def search_command():
    resultsBox.delete(0, END)
    # Need to use .get() for StringVar Object in order to return plain string value
    for result in backend.search(title=title_text.get(), author=author_text.get(), year = year_text.get(), isbn = isbn_text.get()):
        resultsBox.insert(END, result)

def add_command():
    backend.insert(title= title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get())
    resultsBox.delete(0,END)
    resultsBox.insert(END, (title_text.get(),author_text.get(), year_text.get(), isbn_text.get()))
    

def get_Selected_Row(event):
    try:
        global selected_Tuple
        index=resultsBox.curselection()[0]
        selected_Tuple=resultsBox.get(index)
        title_text.set(selected_Tuple[1])
        author_text.set(selected_Tuple[2])
        year_text.set(selected_Tuple[3])
        isbn_text.set(selected_Tuple[4])
        return selected_Tuple
    except IndexError:
        pass

def delete_command():
    backend.delete(selected_Tuple[0])
    view_command()

def update_command():
    backend.update(id=selected_Tuple[0], title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get())
    view_command()

def empty_entries():
    title_text.set("")
    author_text.set("")
    year_text.set("")
    isbn_text.set("")

print()

# Entry labels
title_label = Label(window, text="Title")
title_label.grid(row=0,column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0,column=2)

year_label = Label(window, text="Year")
year_label.grid(row=1,column=0)

isbn_label= Label(window, text="ISBN")
isbn_label.grid(row=1,column=2)

# Entries
title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

# List box
resultsBox = Listbox(window, height=6, width=35)
resultsBox.grid(row=2, column=0, rowspan=6, columnspan=2)

# ScrollBar
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

resultsBox.config(yscrollcommand=scroll.set)
scroll.config(command=resultsBox.yview)

resultsBox.bind('<<ListboxSelect>>', get_Selected_Row)

# Buttons
viewAll_Button = Button(window, text="View All", width=12, command=view_command)
viewAll_Button.grid(row=2, column=3)

searchEntry_Button = Button(window, text="Search Entry", width=12, command=search_command)
searchEntry_Button.grid(row=3, column=3)

addEntry_Button = Button(window, text="Add Entry", width=12, command=add_command)
addEntry_Button.grid(row=4, column=3)

update_Button = Button(window, text="Update", width=12, command=update_command)
update_Button.grid(row=5, column=3)

delete_Button = Button(window, text="Delete", width=12, command=delete_command)
delete_Button.grid(row=6, column=3)

close_Button = Button(window, text="Close", width=12, command=window.destroy)
close_Button.grid(row=7, column=3)

window.mainloop()