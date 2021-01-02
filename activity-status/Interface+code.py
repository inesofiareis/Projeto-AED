from tkinter import *
import os

# definida a window
window = Tk()
window.geometry("1000x750")
window.title("To-Do List")

pasta = "c:\\tarefas"
ficheiro ="c:\\tarefas\\info_tarefas.txt"

if os.path.exists(pasta) == False:
    os.mkdir(pasta)
else:
    print("A pasta já existia em {0}".format(pasta))


print()


if os.path.isfile:
    ficheiro = open("c:\\tarefas\\info_tarefas.txt" , "a", encoding="utf-8")
else:
    print("O ficheiro já existia em {0}".format(ficheiro))


# definir as funções e atribuir aos respetivos botões

def save_changes():
    global ficheiro

    task = entry_title.get(0, END)
    description = txt_description.get(0, END)
    state = value.get(0, END)

    file = open("info_tarefa.txt", "a")
    file.write(task + ";" + description + ";" + state + "\n")
    file.close()
    entry_title.delete(0, END)
    txt_description.delete(0, END)

    




def create():
    to_do = entry_title.get()
    lbox_to_do.insert(END, to_do)
    entry_title.delete(0, END)


# def edit():

# def delete():


# def save_comment():




# Caixa com a lista de tarefas 
painel_items = PanedWindow(window, width=350, height=400, bd=2, relief= "sunken")
painel_items.place( x= 10, y=100) 

lbl_listbox = Label(painel_items, text="Todas as Tarefas")
lbl_listbox.place(x=90, y=10)
lbox_to_do = Listbox(painel_items, width = 45, height=20, bd=2, relief="sunken")
lbox_to_do.place(x=10, y=50)


# Caixa com botões de criar, editar ou remover 
painel_btn = PanedWindow(window, width=350, height=100, bd=2, relief= "sunken")
painel_btn.place( x= 10, y=525) 

btn_create = Button(painel_btn, text="Criar", width=10,  command = create)
btn_create.place(x=30, y=35)

btn_edit = Button(painel_btn, text="Editar", width=10) # command = edit)
btn_edit.place(x=130, y=35)

btn_remove = Button(painel_btn, text="Remover", width=10) # command = remove)
btn_remove.place(x=230, y=35)



# Caixa para comentar 
painel_comment= PanedWindow(window, width=500, height=150, bd=2, relief= "sunken")
painel_comment.place( x= 450, y=525) 

btn_save = Button(painel_comment, text="Salvar", width=10) # command = save_comment)
btn_save.place(x=10, y=80)

lbl_comment = Label(painel_comment, text="Comentar:")
lbl_comment.place(x=20, y = 40)

txt_comment = Text(painel_comment, width = 40, height = 5)
txt_comment.place(x=150, y = 30)



# Painel do to do --------------------------------
painel_to_do = PanedWindow(window, width=500, height=400, bd=2, relief= "sunken")
painel_to_do.place( x= 450, y=100) 

#titulo
lbl_title = Label(painel_to_do, text="Título:")
lbl_title.place(x=15, y = 30)

entry_title = Entry(painel_to_do, width = 50)
entry_title.place(x = 90, y= 30)

# descrição
lbl_description = Label(painel_to_do, text="Descrição:")
lbl_description.place(x=15, y = 70)

txt_description = Text(painel_to_do, width = 55, height = 5)
txt_description.place(x=15, y = 100)

# se está concluido ou não
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

# salvar alterações
btn_save = Button(painel_to_do, text="Salvar", width=10, command = save_changes)
btn_save.place(x=410, y=360)



window.mainloop()