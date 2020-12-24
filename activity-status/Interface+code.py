from tkinter import *

window = Tk()
window.geometry("1000x750")
window.title("To-Do List")


# definir as funções e atribuir aos respetivos butões

def save():
    task = entry_title.get()
    description = txt_description.get()
    state = value.get()
    
    entry_title.delete(0, END)
    txt_description.delete(0, END)


def create():

def edit():

def delete():








# Caixa com a lista de tarefas ----------------------------
painel_items = PanedWindow(window, width=350, height=400, bd=2, relief= "sunken")
painel_items.place( x= 10, y=100) 
# ---------------------------------------------------------------

# Caixa com botões de editar ou remover -------------------
painel_btn = PanedWindow(window, width=350, height=100, bd=2, relief= "sunken")
painel_btn.place( x= 10, y=525) 

btn_create = Button(painel_btn, text="Criar", width=10)
btn_create.place(x=30, y=35)


btn_edit = Button(painel_btn, text="Editar", width=10)
btn_edit.place(x=130, y=35)

btn_remove = Button(painel_btn, text="Remover", width=10)
btn_remove.place(x=230, y=35)

#--------------------------------------------------------------------

# Caixa com outros botões --------------------------------------------
painel_comment= PanedWindow(window, width=500, height=150, bd=2, relief= "sunken")
painel_comment.place( x= 450, y=525) 

btn_save = Button(painel_comment, text="Salvar", width=10)
btn_save.place(x=10, y=80)



lbl_comment = Label(painel_comment, text="Comentar:")
lbl_comment.place(x=20, y = 40)

txt_comment = Text(painel_comment, width = 40, height = 5)
txt_comment.place(x=150, y = 30)



# Painel do to do --------------------------------
painel_to_do = PanedWindow(window, width=500, height=400, bd=2, relief= "sunken")
painel_to_do.place( x= 450, y=100) 

lbl_title = Label(painel_to_do, text="Título:")
lbl_title.place(x=15, y = 30)

entry_title = Entry(painel_to_do, width = 50)
entry_title.place(x = 90, y= 30)


lbl_description = Label(painel_to_do, text="Descrição:")
lbl_description.place(x=15, y = 70)

txt_description = Text(painel_to_do, width = 55, height = 5)
txt_description.place(x=15, y = 100)

frame = LabelFrame(painel_to_do, width=200, height=150,bd ="3", relief="sunken", fg="blue", text="Estado")
frame.place (x=15,y=200)
selected = IntVar()
nc = StringVar()
ep = StringVar()
c = StringVar()
radio= Radiobutton(frame, text="Não concluída", variable=selected, value=nc)
radio2= Radiobutton(frame, text="Em progresso", variable=selected, value=ep)
radio3= Radiobutton(frame, text="Concluída", variable=selected, value=c)
radio.place(x=40,y=20)
radio2.place(x=40, y=50)
radio3.place(x=40, y=80)

btn_save = Button(painel_to_do, text="Salvar", width=10, command = save)
btn_save.place(x=410, y=360)



window.mainloop()