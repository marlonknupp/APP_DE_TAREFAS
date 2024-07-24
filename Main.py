import tkinter as tk 
from tkinter import ttk, font, messagebox 
from tkinter import PhotoImage


# Criando janela 
janela = tk.Tk()
janela.title("Meu app de tarefas")
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho =  tk.Label(janela, text="Meu App de tarefas", font=fonte_cabecalho, bg="#F0f0f0", fg="#333").pack(pady=20)
janela.mainloop()

#######3