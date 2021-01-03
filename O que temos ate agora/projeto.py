from tkinter import *
import tkinter as tk
import os
# bibliotecas necessárias para os vídeos (é preciso instalar a imageio)
# import imageio
# from PIL import Image, ImageTk



# Aqui eu tentei implementar uma fução que tocasse um vídeo com o gif 
# que a Viviana fez, pelo que estive a ler, o tkinter é
# tão primitivo que temos de importar 423430248390284302
# bibliotecas para fazer isto funcionar, e nem sequer está a dar



# def stream(video):
    #try:
     #   image = video.get_next_data()
      #  frame_image = Image.fromarray(image)
       # frame_image=ImageTk.PhotoImage(frame_image)
        #l1.config(image=frame_image)
        #l1.image = frame_image
        #l1.after(delay, lambda: stream())
    #except:
     #   video.close()
      #  return   


# esta é a função da janela que aparece em primeiro lugar na nossa aplicação
def window_entrada(): # define a janela que aparece em primeiro lugar
    window_1 = Tk()
    window_1.geometry("400x500")
    window_1.title("Calend'it - Bem-Vindo!")
    window_1.iconbitmap("c:/aed.ico") # isto permite meter um logotipo na janela

# ignorem é para fazer o vídeo tocar
    #f1=Frame()
    #l1 = Label(f1)
    #l1.pack()
    #f1.pack()
    #video_name = "aed.mp4"   #Image-path
    #video = imageio.get_reader(video_name)
    #delay = int(1000 / video.get_meta_data()['fps'])
    #stream(video)


    # estes dois botões vão levar o user a uma janela onde se pode registar OU onde pode efetuar o login

    btn_register = Button(window_1, text="Registar", width=10, command = lambda:[registar(), window_1.destroy()])
    btn_register.place(x=150, y=300)     # basicamente o que o lambda aqui em cima faz é deixar-me implementar duas funções 
                                        # no mesmo botão. ao meter 2 funções no mesmo command, dá para apagar a janela!

    btn_login = Button(window_1, text="Login", width=10 , command = lambda:[login(), window_1.destroy()]) 
    btn_login.place(x=150, y=350)




# aqui vai para a parte em que o user se pode registar ou fazer o login, já te crier as janelas
# @viviana, agora só tens de meter as coisinhas cá dentro
# podes alterar o botão para como quiseres, não te esqueças é de copiar a parte do command

def registar(): 
    window_register = Tk()
    window_register.geometry("400x500")
    window_register.title("Calend'it - Registar")
    window_register.iconbitmap("c:/aed.ico")
    btn_register = Button(window_register, text="Registar", width=10,command= lambda:[window_main(), window_register.destroy()])
    btn_register.place(x=150, y=300)


def login():
    window_login = Tk()
    window_login.geometry("400x500")
    window_login.title("Calend'it - Login")
    window_login.iconbitmap("c:/aed.ico")
    btn_login = Button(window_login, text="Login", width=10, command = lambda:[window_main(), window_login.destroy()])
    btn_login.place(x=150, y=300)


# a partir daqui é tudo o que já tínhamos, que acharem que a parte visual está feia (eu só fiz um rascunho okay hahahah)
# alterem e mandem o vosso código!
# encontrei uma cena que nos permite alterar os temas? temos é de usar a bibloteca ttkinter acho eu
# vejam aqui

def window_main():
    window = Tk()
    window.geometry("1400x750")
    window.title("Calend'it")
    window.iconbitmap("c:/aed.ico")

    # Aqui estão as funções que nos permitem abrir as categorias/ estados

    #categorias
    def Pessoais():

        painel1=LabelFrame(window,text='Pessoais',fg='#ea8c5c', font=('Arial',12), width=350, height=250, relief=SUNKEN)
        painel1.place(x=410,y=95)

    #-----------------------//------------------------#     
    def Profissionais():

        painel1=LabelFrame(window,text='Profissionais',fg='#ea8c5c', font=('Arial',12), width=350, height=250, relief=SUNKEN)
        painel1.place(x=410,y=95)

    #-----------------------//------------------------# 
    def Projetos():

        painel1=LabelFrame(window,text='Projetos',fg='#ea8c5c', font=('Arial',12), width=350, height=250, relief=SUNKEN)
        painel1.place(x=410,y=95)
        

    # estados
    def not_finished():

        painel1=LabelFrame(window,text='Não Concluídas',fg='#ea8c5c', font=('Arial',12), width=350, height=250, relief=SUNKEN)
        painel1.place(x=410,y=370)
 
    def in_progress():

        painel1=LabelFrame(window,text='Em Progresso',fg='#ea8c5c', font=('Arial',12), width=350, height=250, relief=SUNKEN)
        painel1.place(x=410,y=370)

    def finished():

        painel1=LabelFrame(window,text='Concluídas',fg='#ea8c5c', font=('Arial',12), width=350, height=250, relief=SUNKEN)
        painel1.place(x=410,y=370)
        


    # Aqui vão estar as funções dos botões que eu ainda tenho de programar ai desculpem


    # este é o botão que guarda as atividades que o utilizador regista
    # vocês sabem como é que eu posso guardar as informações num ficheiro .txt?
    # vou tentar explicar

    # então temos aquela parte que nos permite criar uma nova tarefa
    # o utilizador vai inserir um título, uma descrição, meter o estado e a categoria a que pertence
    # depois guarda as alterações

    # eu precisava de guardar tudo o que o user registou para depois poder exibir tudo outra vez se ele quiser
    # editar a tarefa, percebem?
    # mas eu não tou bem a ver como vou fazer isso sem criar 3281372189 ficheiros .txt

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

        
    # botão que cria a nova atividade, depois vai fazer display do título naquela listbox ali embaixo
    def create():
        to_do = entry_title.get()
        lbox_to_do.insert(END, to_do)
        entry_title.delete(0, END)


    # falta definir estas functions
    # def edit():

    # def delete():

    # def save_comment():


    # Aqui está implementado os menus que depois descem para baixo na parte de cima da janela
    # divididos em categorias, estados e um botão sair
    barra_menu=Menu(window)

    submenu= Menu(barra_menu)
    submenu_two = Menu(barra_menu)

    submenu.add_command(label="Pessoais", command=Pessoais)
    submenu.add_command(label="Profissionais", command=Profissionais)
    submenu.add_command(label="Projetos", command=Projetos)

    submenu_two.add_command(label="Não concluído", command=not_finished)
    submenu_two.add_command(label="Em progresso", command=in_progress)
    submenu_two.add_command(label="Concluído", command=finished)

    barra_menu.add_cascade(label="Categorias", menu=submenu)
    barra_menu.add_cascade(label="Estados", menu=submenu_two)
    barra_menu.add_command(label="Sair", command= window.quit)

    window.configure(menu=barra_menu)



    # Aqui está feita a caixa com a lista de tarefas
    painel_items = PanedWindow(window, width=350, height=400, bd=2, relief= "sunken")
    painel_items.place( x= 10, y=100) 

    # e a própria lista
    lbl_listbox = Label(painel_items, text="Todas as Tarefas")
    lbl_listbox.place(x=90, y=10)
    lbox_to_do = Listbox(painel_items, width = 45, height=20, bd=2, relief="sunken")
    lbox_to_do.place(x=10, y=50)



    # Caixa com botões de criar, editar ou remover 
    painel_btn = PanedWindow(window, width=350, height=100, bd=2, relief= "sunken")
    painel_btn.place( x= 10, y=525) 

    #Botão criar
    btn_create = Button(painel_btn, text="Criar", width=10,  command = create)
    btn_create.place(x=30, y=35)

    #editar
    btn_edit = Button(painel_btn, text="Editar", width=10) # command = edit)
    btn_edit.place(x=130, y=35)

    #remover
    btn_remove = Button(painel_btn, text="Remover", width=10) # command = remove)
    btn_remove.place(x=230, y=35)



    # Caixa para comentar 
    painel_comment= PanedWindow(window, width=500, height=150, bd=2, relief= "sunken")
    painel_comment.place( x= 800, y=525) 

    # a parte que permite meter o comentário
    lbl_comment = Label(painel_comment, text="Comentar:")
    lbl_comment.place(x=20, y = 40)
    txt_comment = Text(painel_comment, width = 40, height = 5)
    txt_comment.place(x=150, y = 30)

    #o botão que salva o comentário e o vai meter algures
    btn_save = Button(painel_comment, text="Salvar", width=10) # command = save_comment)
    btn_save.place(x=10, y=80)



    # Inês - Painel que vai conter as infos sobre uma tarefa 
    painel_to_do = PanedWindow(window, width=500, height=400, bd=2, relief= "sunken")
    painel_to_do.place( x= 800, y=100) 

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

    # associar a uma categoria
    frame = LabelFrame(painel_to_do, width=200, height=150,bd ="3", relief="sunken", fg="blue", text="Categoria")
    frame.place (x=250,y=200)
    selected = IntVar()
    personal = StringVar()
    job = StringVar()
    project = StringVar()
    radio= Radiobutton(frame, text="Pessoais", variable=selected, value=personal)
    radio2= Radiobutton(frame, text="Profissionais", variable=selected, value=job)
    radio3= Radiobutton(frame, text="Projetos", variable=selected, value=project)
    radio.place(x=40,y=20)
    radio2.place(x=40, y=50)
    radio3.place(x=40, y=80)

    # salvar alterações
    btn_save = Button(painel_to_do, text="Salvar", width=10, command = save_changes)
    btn_save.place(x=410, y=360)


# esta função é chamada logo no início para abrir logo a janela
window_entrada()

# vi na net que se só metermos mainloop() todas as janelas persistem até o botão das fechar ser pressionado
mainloop()