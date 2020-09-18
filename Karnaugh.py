import tkinter, Func

win_width = 450
win_height = 330

win = tkinter.Tk('main')
win.config(bg='white', width=win_width, height=win_height)

#textbox
textbox_q1 = tkinter.Entry(win, width=26, bg='white', relief='groove', bd=2, name='textbox_q1')
textbox_q2 = tkinter.Entry(win, width=26, bg='white', relief='groove', bd=2, name='textbox_q2')
textbox_n_ff = tkinter.Entry(win, width=7, bg='white', relief='groove', bd=2, name='textbox_n_ff')

#listbox
listbox_q1 = tkinter.Listbox(win, width=26, height=15, relief='groove', bd=2, name='listbox_q1', bg='white')
listbox_q2 = tkinter.Listbox(win, width=26, height=15, relief='groove', bd=2, name='listbox_q2', bg='white')

#button
add_button = tkinter.Button(win, text='Add', width=8, bg='white', relief='groove', bd=2)
delete_button = tkinter.Button(win, text='Delete', width=8, bg='white', relief='groove', bd=2)
modify_button = tkinter.Button(win, text='Modify', width=8, bg='white', relief='groove', bd=2)
table_button = tkinter.Button(win, text='Table', width=8, bg='white', relief='groove', bd=2)

#bind degli eventi
table_button.bind('<' + tkinter.EventType.ButtonPress.__str__() + '-1>', func=Func.table_button, add='+')
add_button.bind('<' + tkinter.EventType.ButtonPress.__str__() + '-1>', func=Func.add_button, add='+')
delete_button.bind('<' + tkinter.EventType.ButtonPress.__str__() + '-1>', func=Func.delete_button, add='+')
listbox_q1.bind('<' + tkinter.EventType.ButtonRelease.__str__() + '-1>', func=Func.listbox_select, add='+')
listbox_q2.bind('<' + tkinter.EventType.ButtonRelease.__str__() + '-1>', func=Func.listbox_select, add='+')
modify_button.bind('<' + tkinter.EventType.ButtonPress.__str__() + '-1>', func=Func.modify_button, add='+')


#place dei widget
textbox_n_ff.place(x=20, y=5)
textbox_q1.place(x=20, y=30)
textbox_q2.place(x=win_width - 185, y=30)

listbox_q1.place(x=20, y=60)
listbox_q2.place(x=win_width-185, y=60)

add_button.place(x=win_width-259, y=68)
delete_button.place(x=win_width-259, y=108)
modify_button.place(x=win_width - 259, y=148)
table_button.place(x=win_width - 259, y=248)

win.title('Carnot')
win.mainloop()