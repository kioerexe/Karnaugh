import tkinter, Func, turtle

win_width=650
win_height=550

jk_states = None
turtle_table = None
points_turtle = None
points = list()
drawing = False

def init(master, jk):
    global jk_states, turtle_table, points_turtle
    jk_states = jk

    win = tkinter.Toplevel(master)
    win.config(bg='white', width=win_width, height=win_height)

    textbox_n_ff = master.nametowidget('textbox_n_ff')
    n_ff = int(textbox_n_ff.get())

    #listbox
    listbox_jk = tkinter.Listbox(win, bg='white', width=15, height=8, relief='groove', bd=2)
    
    #per ogni flip flop aggiungo j e k alla listbox
    for ff in range(n_ff):
        listbox_jk.insert('end', 'j' + ff.__str__())
        listbox_jk.insert('end', 'k' + ff.__str__())

    del textbox_n_ff, n_ff

    #canvas
    canv_table = tkinter.Canvas(win, bg='white', width=win_width - 140, height=win_height - 50, relief='groove', bd=2)

    turtle_table = turtle.RawTurtle(canv_table, visible=False)
    points_turtle = turtle.RawTurtle(canv_table, visible=False)

    #bind degli eventi
    listbox_jk.bind('<' + tkinter.EventType.ButtonRelease.__str__() + '-1>', func=Func.listbox_select_table, add='+')
    canv_table.bind('<' + tkinter.EventType.ButtonPress.__str__() + '>', func= Func.canvas_click, add='+')
    canv_table.bind('<' + tkinter.EventType.Motion.__str__() + '>', func=Func.canvas_motion, add='+')

    #place dei widget
    listbox_jk.place(x=10, y=25)
    canv_table.place(x=120, y=25)

    win.title('Carnot-Table')
    win.mainloop()
