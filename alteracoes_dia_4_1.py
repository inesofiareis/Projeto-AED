from tkinter import *
from tkinter import ttk


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




    panel_tree = LabelFrame(window, text="Consultar a lista de tarefas", width= 650, height= 500, bd = "3", relief="sunken")
    panel_tree.place(x=10, y=100)

    tree = ttk.Treeview(panel_tree, columns = ("Título", "Descrição", "Estado", "Categoria") ,show = "headings")
    tree.column("Título", width= 100, anchor ="c")
    tree.column("Descrição", width= 300, anchor ="c")
    tree.column("Estado", width= 100, anchor ="c")
    tree.column("Categoria", width= 100, anchor ="c")
    tree.heading("Título", text="Título")
    tree.heading("Descrição", text="Descrição")
    tree.heading("Estado", text="Estado")
    tree.heading("Categoria", text="Categoria")
    tree.place(x=5,y=5)

    def selectItem(a):
        curItem = tree.focus()
        btn_edit["state"] = "normal"
        btn_remove["state"] = "normal"
        btn_comentar["state"] = "normal"
        print (tree.item(curItem))

    tree.bind('<ButtonRelease-1>', selectItem)


    lbl_create = Label(panel_tree, text="Deseja criar uma nova tarefa?")
    lbl_create.place(x=100, y = 250)
    btn_create = Button(panel_tree, text="Criar", width=10,  command = create)
    btn_create.place(x=10, y=250)


    lbl_edit = Label(panel_tree, text="Selecione uma tarefa e edite-a.")
    lbl_edit.place(x=100, y = 300)
    btn_edit = Button(panel_tree, text="Editar", width=10, state= DISABLED) # command = edit)
    btn_edit.place(x=10, y=300)


    lbl_comentar = Label(panel_tree, text="Selecione uma tarefa e pressione o botão para a comentar.")
    lbl_comentar.place(x=100, y = 350)
    btn_comentar = Button(panel_tree, text="Comentar", width=10, state = DISABLED) # command = remove)
    btn_comentar.place(x=10, y=350)



    lbl_remove = Label(panel_tree, text="Selecione um item e pressione o botão para o remover.")
    lbl_remove.place(x=100, y = 400)
    btn_remove = Button(panel_tree, text="Remover", width=10, state = DISABLED) # command = remove)
    btn_remove.place(x=10, y=400)
    window.mainloop()

window_main()