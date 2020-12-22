from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("To-Do List")

painel1 = PanedWindow(window, width=200, height=400, bd=2, relief= "sunken")
painel1.place( x= 10, y=100) 

btn_create = Button(window, text="Criar uma nova atividade")
btn_create.place(x=300, y=300)


btn_add = Button(window, text="Adicionar às tarefas")
btn_add.place(x=300, y=300)

btn_remove = Button(window, text="Remover tarefa")
btn_remove.place(x=300, y=350)

btn_adicionar = Button(window, text="Adicionar")
btn_adicionar.place(x=100, y=150)

lista_acti = Listbox(window)
lista_acti.place(x=50, y=150)

btn_adicionar = Button(window, text="Criar uma nova atividade")
btn_adicionar.place(x=40, y=350)


window.mainloop()