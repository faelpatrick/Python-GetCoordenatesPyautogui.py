from tkinter import *
from PIL import *
from random import Image, ImageTk 

pontuacao = 0

root = Tk()
root.geometry('900x700+900+800')
root.resizable(x=True, y=True)
root.title('Jogo de Hallowen')
root.configure(bg='black')
fonte = ('Arial', 18)
def iniciar_jogo():
    global pontuacao
    potuacao = 0
    atualizar_pontuacao()
    aparecer_fantasma()




def atualizar_pontuacao():
    lbl_pontuacao.config(text=f'PONTOS:{pontuacao}')



def aparecer_fantasma():
    largura_tela = root.winfo_width()
    altura_tela = root.winfo_height()













lbl_pontuacao = Tk.label(root, text='PONTOS: O', font='Arial')

















root.mainloop()