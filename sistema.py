import tkinter as tk
from tkinter import messagebox

# Função de exemplo para cada botão
def escanear_nota():
    messagebox.showinfo("Ação", "Escaneando Nota Fiscal...")

def recebido():
    messagebox.showinfo("Ação", "Nota Fiscal Recebida.")

def patrimonizado():
    messagebox.showinfo("Ação", "Bens Patrimonizados.")

def saida():
    messagebox.showinfo("Ação", "Saída do Almoxarifado Registrada.")

def entregue():
    messagebox.showinfo("Ação", "Bens Entregues.")

def recebido_nao_patrimonizado():
    messagebox.showinfo("Ação", "Recebido e Não Patrimonizado.")

# Criação da janela principal
root = tk.Tk()
root.title("Sistema de Controle de Patrimônio")
root.geometry("600x400")

# Frame para a parte esquerda
frame_esquerda = tk.Frame(root, width=300, height=400, padx=10, pady=10)
frame_esquerda.pack(side="left", fill="y")

# Exibir informações da Nota Fiscal
label_info_nota = tk.Label(frame_esquerda, text="Informações da Nota Fiscal", font=("Arial", 12))
label_info_nota.pack(anchor="nw")

# Janela de exibição das informações da nota fiscal
info_nota = tk.Text(frame_esquerda, height=15, width=35)
info_nota.pack()

# Estado das movimentações
label_estado = tk.Label(frame_esquerda, text="Estado das Movimentações", font=("Arial", 12))
label_estado.pack(anchor="nw")

# Janela de exibição das movimentações
estado_mov = tk.Text(frame_esquerda, height=6, width=35)
estado_mov.pack()

# Botão de "Recebido e Não Patrimonizado"
btn_nao_patrimonizado = tk.Button(frame_esquerda, text="Recebido e Não Patrimonizado", bg="red", fg="white", command=recebido_nao_patrimonizado)
btn_nao_patrimonizado.pack(anchor="sw", pady=10)

# Frame para a parte direita
frame_direita = tk.Frame(root, width=300, height=400, padx=10, pady=10)
frame_direita.pack(side="right", fill="y")

# Botões da direita
btn_escanear = tk.Button(frame_direita, text="Escanear", width=20, command=escanear_nota)
btn_escanear.pack(pady=10)

btn_recebido = tk.Button(frame_direita, text="Recebido", width=20, command=recebido)
btn_recebido.pack(pady=10)

btn_patrimonizado = tk.Button(frame_direita, text="Patrimonizado", width=20, command=patrimonizado)
btn_patrimonizado.pack(pady=10)

btn_saida = tk.Button(frame_direita, text="Saída", width=20, command=saida)
btn_saida.pack(pady=10)

btn_entregue = tk.Button(frame_direita, text="Entregue", width=20, command=entregue)
btn_entregue.pack(pady=10)

# Executar a interface
root.mainloop()
