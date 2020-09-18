import Table

jk_state = {'memory0':'0.x', 'set':'1.x', 'reset':'x.1', 'memory1':'x.0'}

def gen_gray(n_bit):
    res = list()

    combinazioni = int(2 ** n_bit)

    #ottengo il codice di gray di un numero
    for num in range(combinazioni):
        gray_num = num ^ (num >> 1)

        gray_num = bin(gray_num)
        gray_num = gray_num.replace('0b', '')

        gray_num = '%*s' % (n_bit, gray_num)
        gray_num = gray_num.replace(' ', '0')

        res.append(gray_num)

    return tuple(res)

def combination_jk(q1, q2):
    if(q1 == '0'):
        if(q2 == '0'):
            return jk_state['memory0']
        else:
            return jk_state['set']
    else:
        if(q2 == '0'):
            return jk_state['reset']
        else:
            return jk_state['memory1']

def jk(*listbox):
    res = list()

    #per ogni flip flop aggiungo una lista
    for ff in range(len(listbox[0].get(0))):
        res.append(list())

    #per ogni flip flop aggiungo j e k
    for ff in res:
        ff.append(list())
        ff.append(list())

    state_q1 = listbox[0].get(0, 'end')
    state_q2 = listbox[1].get(0, 'end')

    for i_state in range(len(state_q1)):
        s_q1 = state_q1[i_state]
        s_q2 = state_q2[i_state]

        for bit in range(len(res)):
            comb = combination_jk(s_q1[bit], s_q2[bit])
            comb = comb.split('.')

            res[bit][0].append(comb[0])
            res[bit][1].append(comb[1])

    return tuple(res)

def create_table(jk, n_ff):

    #metto i bit sulle colonne e sulle righe della tabella
    n_bit_col = None
    n_bit_row = None

    if((n_ff % 2) == 1):
        n_bit_col = int(n_ff / 2) + 1
        n_bit_row = int(n_ff / 2)
    else:
        n_bit_col = int(n_ff / 2)
        n_bit_row = int(n_ff / 2)

    #prendo il codice di gray
    gray_col = gen_gray(n_bit_col)
    gray_row = gen_gray(n_bit_row)

    table = list()

    for row in range(len(gray_row)):
        table.append(list())
        for col in range(len(gray_col)):

            state = gray_row[row] + gray_col[col]
            i = int(state, 2)

            val = ' '
            try:
                val = jk[i]
            except IndexError:
                val = ' '

            table[row].append(val)

    return (tuple(table), gray_row, gray_col)

def draw_table(tab, *gray):
    Table.turtle_table.screen.tracer(0, 0)
    Table.turtle_table.color('red')
    Table.turtle_table.clear()

    turtle = Table.turtle_table
    n_row = len(tab)
    n_col = len(tab[0])

    wide_cell = 50

    width = n_col * wide_cell
    height = n_row * wide_cell

    #pos iniziale
    pos_1 = (-width / 2, height / 2)

    for row in range(n_row + 1):
        turtle.penup()
        turtle.goto(pos_1[0], pos_1[1] - (wide_cell * row))
        #scrivo il codice di gray
        if(row > 0):
            turtle.color('black')
            turtle.back(8 * len(gray[0][0]))
            turtle.write(gray[0][row - 1])
            turtle.forward(8 * len(gray[0][0]))
            turtle.color('red')

        turtle.pendown()
        turtle.forward(width)

    turtle.right(90)

    for col in range(n_col + 1):
        turtle.penup()
        turtle.goto(pos_1[0] + (wide_cell * col), pos_1[1])
        if(col < n_col):
            turtle.color('black')
            turtle.write(gray[1][col])
            turtle.color('red')

        turtle.pendown()
        turtle.forward(height)

    turtle.left(90)

    #scrivo gli 1 e x nelle celle
    turtle.color('black')
    turtle.penup()

    for row in range(n_row):
        for col in range(n_col):
            turtle.goto(pos_1[0] + (col * wide_cell) + (wide_cell * 0.35), pos_1[1] - (row * wide_cell) - (wide_cell * 0.8))
            turtle.write(tab[row][col], font=('Arial', 20, 'normal'))

    turtle.screen.update()


#funzione per trovare l'ultimo elemento selezionato
def last_element_selected(*listbox):
    listbox_q1 = listbox[0]
    listbox_q2 = listbox[1]

    #prendo gli indici e quello con la tuple piena lo ritorno
    index_q1 = listbox_q1.curselection()
    index_q2 = listbox_q2.curselection()

    if(len(index_q1) > 0):
        return index_q1[0]
    elif(len(index_q2) > 0):
        return index_q2[0]
    else:
        return None

def table_button(event):
    listbox_q1 = event.widget.master.nametowidget('listbox_q1')
    listbox_q2 = event.widget.master.nametowidget('listbox_q2')

    #se ho inserito almeno uno stato
    if(len(listbox_q1.get(0, 'end')) > 0 and len(listbox_q2.get(0, 'end')) > 0):
        state_jk = jk(listbox_q1, listbox_q2)
        gen_gray(len(listbox_q1.get(0)))
        Table.init(event.widget.master, state_jk)

def add_button(event):
    #caselle di testo per prendere il testo da inserire
    textbox_q1 = event.widget.master.nametowidget('textbox_q1')
    textbox_q2 = event.widget.master.nametowidget('textbox_q2')
    textbox_n_ff = event.widget.master.nametowidget('textbox_n_ff')

    #prendo il numero dei flip flop
    n_ff = int(textbox_n_ff.get())

    text_q1 = textbox_q1.get()
    text_q2 = textbox_q2.get()

    #se il numerp di bit dello stato è uguale al numero dei flip flop
    if(len(text_q1) == n_ff and len(text_q2) == n_ff):
        #listbox per inserire lo stato
        listbox_q1 = event.widget.master.nametowidget('listbox_q1')
        listbox_q2 = event.widget.master.nametowidget('listbox_q2')

        listbox_q1.insert('end', text_q1)
        listbox_q2.insert('end', text_q2)

        #pulisco il testo dalle textbox
        textbox_q1.delete(0, 'end')
        textbox_q2.delete(0, 'end')

        del listbox_q1, listbox_q2

    del text_q1, text_q2, n_ff, textbox_n_ff, textbox_q1, textbox_q2

def delete_button(event):
    listbox_q1 = event.widget.master.nametowidget('listbox_q1')
    listbox_q2 = event.widget.master.nametowidget('listbox_q2')

    #elimino l'elemento selezionato
    element = last_element_selected(listbox_q1, listbox_q2)
    
    if(element != None):
        textbox_q1 = event.widget.master.nametowidget('textbox_q1')
        textbox_q2 = event.widget.master.nametowidget('textbox_q2')

        listbox_q1.delete(element)
        listbox_q2.delete(element)

        #elimino il testo dalle caselle
        textbox_q1.delete(0, 'end')
        textbox_q2.delete(0, 'end')

        del textbox_q1, textbox_q2

    del listbox_q1, listbox_q2, element

def listbox_select(event):
    listbox_q1 = event.widget.master.nametowidget('listbox_q1')
    listbox_q2 = event.widget.master.nametowidget('listbox_q2')

    element = last_element_selected(listbox_q1, listbox_q2)

    if(element != None):
        textbox_q1 = event.widget.master.nametowidget('textbox_q1')
        textbox_q2 = event.widget.master.nametowidget('textbox_q2')

        #sostituisco il testo con l'elemmto selezionato
        textbox_q1.delete(0, 'end')
        textbox_q2.delete(0, 'end')

        textbox_q1.insert(0, listbox_q1.get(element))
        textbox_q2.insert(0, listbox_q2.get(element))

        del textbox_q1, textbox_q2

    del listbox_q1, listbox_q2, element

def modify_button(event):
    #modifico il testo nelle listbox dal testo delle textbox
    textbox_q1 = event.widget.master.nametowidget('textbox_q1')
    textbox_q2 = event.widget.master.nametowidget('textbox_q2')
    textbox_n_ff = event.widget.master.nametowidget('textbox_n_ff')

    #stessa logica di add_button
    n_ff = int(textbox_n_ff.get())
    text_q1 = textbox_q1.get()
    text_q2 = textbox_q2.get()

    if(len(text_q1) == n_ff and len(text_q2) == n_ff):
        listbox_q1 = event.widget.master.nametowidget('listbox_q1')
        listbox_q2 = event.widget.master.nametowidget('listbox_q2')

        element = last_element_selected(listbox_q1, listbox_q2)

        if(element != None):
            listbox_q1.delete(element)
            listbox_q2.delete(element)

            listbox_q1.insert(element, text_q1)
            listbox_q2.insert(element, text_q2)

            textbox_q1.delete(0, 'end')
            textbox_q2.delete(0, 'end')

        del listbox_q1, listbox_q2, element
    del text_q1, text_q2, textbox_n_ff, textbox_q1, textbox_q2

def listbox_select_table(event):

    i_element = event.widget.curselection()

    if(len(i_element) > 0):
        i_element = i_element[0]
        element = event.widget.get(i_element)

        jk = element[0]
        i = int(element[1])

        if(jk == 'j'):
            tab = create_table(Table.jk_states[i][0], len(Table.jk_states))
        else:
            tab = create_table(Table.jk_states[i][1], len(Table.jk_states))

        draw_table(tab[0], tab[1], tab[2])

        Table.points.clear()
        Table.points_turtle.clear()

        del jk, i

    del element

def canvas_click(event):

    #prendo le coordinate
    canv = event.widget

    y = ((canv.winfo_height() / 2) - event.y)
    x = -(canv.winfo_width() / 2) + event.x

    #in base al pulsante cliccato, aggiungo il punto o mi fermo a disegnare
    if(event.num == 1):
        Table.points.append((x, y, 1))
        Table.drawing = True
    elif(event.num == 3):
        Table.drawing = False

        last = Table.points[-1]

        Table.points.pop()
        Table.points.append((last[0], last[1], 0))

        del last

    print(Table.points)    

    turtle = Table.points_turtle
    turtle.screen.tracer(0,0)

    #disegno i punti
    turtle.penup()
    turtle.color('blue')
    turtle.clear()

    for point in Table.points:
        turtle.goto(point[0], point[1])
        if(point[2]):
            turtle.pendown()
        else:
            turtle.penup()

    turtle.screen.update()
    del canv, x, y, turtle

def canvas_motion(event):
    if(Table.drawing):
        canv = event.widget

        y = ((canv.winfo_height() / 2) - event.y)
        x = -(canv.winfo_width() / 2) + event.x

        Table.points.append((x, y, 0))

        turtle = Table.points_turtle
        turtle.screen.tracer(0,0)

        #disegno i punti
        turtle.penup()
        turtle.color('blue')
        turtle.clear()

        for point in Table.points:
            turtle.goto(point[0], point[1])
            if(point[2]):
                turtle.pendown()
            else:
                turtle.penup()

        turtle.screen.update()
        Table.points.pop()

        del canv, x, y, turtle

