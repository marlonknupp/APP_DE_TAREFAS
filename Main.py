import tkinter as tk 
from tkinter import ttk, font, messagebox 
from tkinter import PhotoImage


# Criando janela 

janela = tk.Tk()
janela.title("Meu app de tarefas")
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

frame_em_edicao = None

# funçao adicionar tarefaa

def adicionar_tarefa(): 
    global frame_em_edicao

    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else: 
            adicionar_item_tarefa(tarefa)
            entrada_tarefa.delete(0, tk.END)
    else:
       messagebox.showwarning("Entrada inválida", "Por favor, insira ma tarefa")

def adicionar_item_tarefa(tarefa):
    frame_tarefa = tk.frame(canvas_interior, bg="white", bd=1, relief=tk.SOLID)
  
    label_tarefa = tk.Label(frame_tarefa, text=tarefa, font=("Garamond", 16), bg= "white", width=25, height=2, anchor="w")
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

botao_editar = tk.Button(frame_tarefa, image=icon_editar, command= lambda f=frame_tarefa, l=label_tarefa: preparar_edicao(f, l), bg= "white", relief=tk.FLAT)
botao_editar.pack(side=tk.RIGHT, padx=5)

botao_deletar = tk.Button(frame_tarefa, image=icon_deletar, command=lambda f=frame_tarefa: deletar_tarefa(f), bg= "white", relief=tk.FLAT)
botao_deletar.pack(side=tk.RIGHT, padx=5)

frame_tarefa.pack(fill=tk.X, padx=5, pady=5)

checkbutton = ttk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alternar_sublinhado(label))
checkbutton.pack(side=tk.RIGHT, padx=5)

canvas_interior.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_em_edicao
    frame_em_edicao = frame_tarefa
    entrada_tarefa.delete(0, tk.END)
    entrada_tarefa.insert(0,label_tarefa.cget("text"))



def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao
    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget, tk.label):
            widget.config(text=nova_tarefa)

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas.interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def alternar_sublinhado(lavel):
    fonte_atual = label.cget("font")
    if "overstrike"in font_atual:
     nova_fonte = fonte_atual.replace("overstrike","")
    else:
     nova_fonte = fonte_atual + " overstrike "
    label.config(font=nova_fonte)

