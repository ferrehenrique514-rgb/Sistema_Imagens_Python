import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


imagens_tk = []


def carregar_imagens():
    nomes_arquivos = [
        entrada1.get().strip(),
        entrada2.get().strip(),
        entrada3.get().strip(),
        entrada4.get().strip(),
        entrada5.get().strip(),          
    ]
    #Limpar imagens anteriores
    for wedget in frame_imagens.winfo_children():
        wedget.destroy()




    imagens_tk.clear()


    for i, nome in enumerate(nomes_arquivos):
        if not nome:
            continue


        if not os.path.isfile(nome):
            messagebox.showerror("Erro", f"Imagem{i+1}:\nArquivo'{nome}' não encontrado.")
            continue
           
        try:
            imagem_pil = Image.open(nome)
            imagem_pil = imagem_pil.resize((250, 150))
            imagem_tk = ImageTk.PhotoImage(imagem_pil)
            imagens_tk.append(imagem_tk)


            label = tk.Label(frame_imagens, image=imagem_tk)
            label.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Erro", f"imagem{i+1}: \nErro ao carregar:\n{e}")


#Criando a Janela
janela = tk.Tk()
janela.title("Exibindo até 5 Imagens ")
janela.geometry("800x600")


#Instruçoes para o usuario
tk.Label(janela, text="Digite até 5 nomes de imagem(ex: foto.jpg):").pack(pady=(10,5))


#Entrada da informação
entrada1 = tk.Entry(janela, width=50)
entrada1.pack(pady=2)


entrada2 = tk.Entry(janela, width=50)
entrada2.pack(pady=2)


entrada3 = tk.Entry(janela, width=50)
entrada3.pack(pady=2)


entrada4 = tk.Entry(janela, width=50)
entrada4.pack(pady=2)


entrada5 = tk.Entry(janela, width=50)
entrada5.pack(pady=2)


botao_carregar = tk.Button(janela, text="Carregar Imagem", command=carregar_imagens)
botao_carregar.pack(pady=10)


#Criar local pra receber as imagens
frame_imagens = tk.Frame(janela)
frame_imagens.pack(pady=10)


#Iniciara interface frafica
janela.mainloop()