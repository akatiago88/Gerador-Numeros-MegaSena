import random
import os
from tkinter import *
from tkinter import messagebox
import res_pandas as rp

# Caminho para a pasta do exe e configurações da janela do tkinter
caminho_app = os.path.dirname(__file__)
arquivotxt = open(caminho_app + '\\dados.txt', 'w')
app = Tk()
app.title('Gerador de números - Mega Sena')
app.geometry('600x500')
app.configure(bg='#008f58')

# Lista com os números sorteados
numeros_sorteados = []


def sorteia_num1():
    numero_n1_sorteado = random.choices(rp.numeros_n1, weights=rp.chances_n1)
    return numero_n1_sorteado


def sorteia_num2():
    numero_n2_sorteado = random.choices(rp.numeros_n2, weights=rp.chances_n2)
    return numero_n2_sorteado


def sorteia_num3():
    numero_n3_sorteado = random.choices(rp.numeros_n3, weights=rp.chances_n3)
    return numero_n3_sorteado


def sorteia_num4():
    numero_n4_sorteado = random.choices(rp.numeros_n4, weights=rp.chances_n4)
    return numero_n4_sorteado


def sorteia_num5():
    numero_n5_sorteado = random.choices(rp.numeros_n5, weights=rp.chances_n5)
    return numero_n5_sorteado


def sorteia_num6():
    numero_n6_sorteado = random.choices(rp.numeros_n6, weights=rp.chances_n6)
    return numero_n6_sorteado


def sorteia_mais():  # Quando for pedido para sortear mais de 6 números
    numero_nn_sorteado = [(numeros, chances) for numeros, chances in zip([rp.numeros_n1, rp.numeros_n2, rp.numeros_n3,
                                                                          rp.numeros_n4, rp.numeros_n5, rp.numeros_n6],
                                                                         [rp.chances_n1, rp.chances_n2, rp.chances_n3,
                                                                          rp.chances_n4,
                                                                          rp.chances_n5, rp.chances_n6])]
    return numero_nn_sorteado


# Chama a função de sortear número por número e verifica a lista se não tem repetido
def sorteia(num):
    n1 = sorteia_num1()
    numeros_sorteados.append(n1)
    if len(numeros_sorteados) == num:
        return

    n2 = sorteia_num2()
    while len(numeros_sorteados) < num:
        if n2 in numeros_sorteados:
            n2 = sorteia_num2()
        else:
            numeros_sorteados.append(n2)
    if len(numeros_sorteados) == num:
        return

    n3 = sorteia_num3()
    while len(numeros_sorteados) < num:
        if n3 in numeros_sorteados:
            n3 = sorteia_num3()
        else:
            numeros_sorteados.append(n3)
    if len(numeros_sorteados) == num:
        return

    n4 = sorteia_num4()
    while len(numeros_sorteados) < num:
        if n4 in numeros_sorteados:
            n4 = sorteia_num4()
        else:
            numeros_sorteados.append(n4)
    if len(numeros_sorteados) == num:
        return

    n5 = sorteia_num5()
    while len(numeros_sorteados) < num:
        if n5 in numeros_sorteados:
            n5 = sorteia_num5()
        else:
            numeros_sorteados.append(n5)
    if len(numeros_sorteados) == num:
        return

    n6 = sorteia_num6()
    while len(numeros_sorteados) < num:
        if n6 in numeros_sorteados:
            n6 = sorteia_num6()
        else:
            numeros_sorteados.append(n6)
    if len(numeros_sorteados) == num:
        return

    nn = sorteia_mais()
    while len(numeros_sorteados) < num:
        if nn in numeros_sorteados:
            nn = sorteia_mais()
        else:
            numeros_sorteados.append(nn)
    if len(numeros_sorteados) == num:
        return


# Chama a função sorteia, personalisa o texto a ser retornado e salva no dados.txt na pasta do .exe
def chama_sorteia():
    qtde_numeros = int(sb_qtde_num.get())
    qtde_jogos = int(sb_qtde_num_jogos.get())
    num_rep = 0

    while num_rep < qtde_jogos:
        sorteia(qtde_numeros)
        sorteado_temp = ' - '.join(str(numero) for numero in numeros_sorteados)
        sorteado = sorteado_temp.replace('[', '').replace(']', '')
        text_num_gerados.insert('end', sorteado+'\n')
        arquivotxt.write(sorteado+'\n')
        num_rep += 1
        numeros_sorteados.clear()
    arquivotxt.close()
    messagebox.showinfo(title='Sucesso', message='Número gerados e salvos no dados.txt. Boa Sorte!')


def msg_sobre():
    messagebox.showinfo(title='Sobre nós', message='Software desenvolvido por Tiago Silva \n'
                                                   'Contato: akatiago88@gmail.com')


# Parte gráfica - Tkinter
# Imagem topo
img_logo = PhotoImage(file=caminho_app+'\\senapng2.PNG')
l_logo = Label(app, image=img_logo)
l_logo.place(x=55, y=10)
# Quadro com as informações para gerar
frame_quadro2 = LabelFrame(app, text='Informações para Gerar', borderwidth=1, relief='sunken')
frame_quadro2.place(x=10, y=170, width=220, height=270)
# Quadro com o text com os número gerados
frame_quadro3 = LabelFrame(app, text='Números Gerados', borderwidth=1, relief='sunken')
frame_quadro3.place(x=310, y=170, width=275, height=270)
# Labels de informações para o quadro 2
lb_qtde_numeros = Label(frame_quadro2, text='Quantidade de números por jogo')
lb_qtde_numeros.place(x=5, y=10)
lb_qtde_jogos = Label(frame_quadro2, text='Quantidade de jogos a ser gerados')
lb_qtde_jogos.place(x=5, y=90)
# Spinbox para as quantidades de numeros e jogos
sb_qtde_num = Spinbox(frame_quadro2, from_=6, to=10)
sb_qtde_num.place(x=9, y=40, width=50)
sb_qtde_num_jogos = Spinbox(frame_quadro2, from_=1, to=50)
sb_qtde_num_jogos.place(x=9, y=120)
# Text para mostrar jogos sorteados
text_num_gerados = Text(frame_quadro3)
text_num_gerados.place(width=270, height=250)
# Botão gerar números
Button(app, bg='#00aa69', text='GERAR NÚMEROS', command=chama_sorteia, font=12).place(x=10, y=450, width=575, height=40)
# Menu
barra_de_menus = Menu(app)
app.config(menu=barra_de_menus)
menu_gerador = Menu(barra_de_menus, tearoff=0)
menu_gerador.add_command(label='Créditos', command=msg_sobre)
barra_de_menus.add_cascade(label='Sobre', menu=menu_gerador)

# Executa como se não houvesse o amanhã
app.mainloop()
