# Biblioteca Tkinter: UI
from tkinter import *
import tkinter as tk
import os
def Pessoais():
    #newWindow=Toplevel(window)
    #newWindow.geometry("600x300")

    painel1=LabelFrame(window,text='Pessoais',fg='#ea8c5c', font=('Arial',12), width=600, height=270, relief=SUNKEN)
    painel1.place(x=10,y=15)

#-----------------------//------------------------#     
def Profissionais():

    painel1=LabelFrame(window,text='Profissionais',fg='#ea8c5c', font=('Arial',12), width=600, height=270, relief=SUNKEN)
    painel1.place(x=10,y=15)

#-----------------------//------------------------# 
def Projetos():

    painel1=LabelFrame(window,text='Projetos',fg='#ea8c5c', font=('Arial',12), width=600, height=270, relief=SUNKEN)
    painel1.place(x=10,y=15)
    


#-----------------------//------------------------#    
window=Tk() #invoca classe tk, cria a "main window"
window.geometry("620x350")
window.title('Agenda')



#Implementar menu
barra_menu=Menu(window)

submenu= Menu(barra_menu)
submenu.add_command(label="Pessoais", command=Pessoais)
submenu.add_command(label="Profissionais", command=Profissionais)
submenu.add_command(label="Projetos", command=Projetos)
barra_menu.add_cascade(label="Categorias", menu=submenu)
barra_menu.add_command(label="Sair", command= window.quit)

window.configure(menu=barra_menu)



window.mainloop()