import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
import os
from datetime import datetime

# Função para criar QR Code
def criar_qr_code(patrimonio, pasta):
    qr = qrcode.make(patrimonio)
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    qr.save(os.path.join(pasta, f"{patrimonio}.png"))

# Função para registrar patrimônio
def registrar_patrimonio():
    patrimonio = entry_patrimonio.get()
    descricao = entry_descricao.get()
    quantidade = entry_quantidade.get()
    
    if not patrimonio or not descricao or not quantidade.isdigit():
        messagebox.showwarning("Entrada Inválida", "Preencha todos os campos corretamente.")
        return

    data_registro = datetime.now().strftime("%d/%m/%Y")
    hora_registro = datetime.now().strftime("%H:%M:%S")

    with open("patrimonios.txt", "a") as arquivo:
        arquivo.write(f"{patrimonio},{data_registro},{hora_registro},{descricao},{quantidade}\n")

    pasta = filedialog.askdirectory(title="Escolha a pasta para salvar o QR Code")
    if pasta:
        criar_qr_code(patrimonio, pasta)
        messagebox.showinfo("Sucesso", f"Patrimônio '{patrimonio}' registrado e QR Code salvo.")
        mostrar_registro(patrimonio, data_registro, hora_registro, descricao, quantidade)

# Função para mostrar o registro
def mostrar_registro(patrimonio, data, hora, descricao, quantidade):
    registro = (f"Patrimônio: {patrimonio}\n"
                f"Data: {data}\n"
                f"Hora: {hora}\n"
                f"Descrição: {descricao}\n"
                f"Quantidade: {quantidade}\n")
    messagebox.showinfo("Registro do Patrimônio", registro)

# Função para listar patrimônios
def listar_patrimonios():
    try:
        with open("patrimonios.txt", "r") as arquivo:
            lista = arquivo.readlines()
        if lista:
            messagebox.showinfo("Patrimônios Registrados", "".join(lista))
        else:
            messagebox.showinfo("Patrimônios Registrados", "Nenhum patrimônio registrado ainda.")
    except FileNotFoundError:
        messagebox.showwarning("Erro", "Nenhum patrimônio registrado ainda.")

# Função para apagar um registro
def apagar_registro():
    patrimonio = entry_apagar.get()
    registros = []
    
    try:
        with open("patrimonios.txt", "r") as arquivo:
            registros = arquivo.readlines()
        
        registros_filtrados = [r for r in registros if not r.startswith(patrimonio + ",")]

        if len(registros) == len(registros_filtrados):
            messagebox.showwarning("Erro", "Registro não encontrado.")
        else:
            with open("patrimonios.txt", "w") as arquivo:
                arquivo.writelines(registros_filtrados)
            messagebox.showinfo("Sucesso", f"Registro de '{patrimonio}' apagado.")
    except FileNotFoundError:
        messagebox.showwarning("Erro", "Nenhum patrimônio registrado ainda.")

# Função para registrar a saída de um patrimônio
def registrar_saida():
    patrimonio = entry_saida.get()
    local_destino = entry_local_destino.get()
    
    if not patrimonio or not local_destino:
        messagebox.showwarning("Entrada Inválida", "Preencha todos os campos.")
        return

    try:
        with open("patrimonios.txt", "r") as arquivo:
            lista = arquivo.readlines()
        
        if any(patrimonio in linha for linha in lista):
            with open("saidas.txt", "a") as saidas:
                saidas.write(f"{patrimonio},{local_destino},{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            messagebox.showinfo("Saída Registrada", f"Patrimônio '{patrimonio}' saiu para '{local_destino}'.")
        else:
            messagebox.showwarning("Erro", "Registro não encontrado.")
    except FileNotFoundError:
        messagebox.showwarning("Erro", "Nenhum patrimônio registrado ainda.")

# Função para listar saídas
def listar_saidas():
    try:
        with open("saidas.txt", "r") as arquivo:
            lista = arquivo.readlines()
        if lista:
            messagebox.showinfo("Saídas Registradas", "".join(lista))
        else:
            messagebox.showinfo("Saídas Registradas", "Nenhuma saída registrada ainda.")
    except FileNotFoundError:
        messagebox.showwarning("Erro", "Nenhuma saída registrada ainda.")

# Função para verificar login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario == "fiscal" and senha == "senha123":  # Exemplo de credenciais
        frame_login.pack_forget()  # Esconde a tela de login
        mostrar_opcoes()           # Mostra as opções de gerenciamento
    else:
        messagebox.showwarning("Erro", "Usuário ou senha inválidos.")

# Função para mostrar opções de gerenciamento
def mostrar_opcoes():
    frame_opcoes.pack(pady=20)

# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Patrimônios")

# Frame de login
frame_login = tk.Frame(root)
frame_login.pack(pady=20)

label_usuario = tk.Label(frame_login, text="Usuário:")
label_usuario.grid(row=0, column=0)
entry_usuario = tk.Entry(frame_login)
entry_usuario.grid(row=0, column=1)

label_senha = tk.Label(frame_login, text="Senha:")
label_senha.grid(row=1, column=0)
entry_senha = tk.Entry(frame_login, show='*')
entry_senha.grid(row=1, column=1)

btn_login = tk.Button(frame_login, text="Login", command=verificar_login)
btn_login.grid(row=2, columnspan=2)

# Frame de opções de gerenciamento
frame_opcoes = tk.Frame(root)

# Frame de registro
label_patrimonio = tk.Label(frame_opcoes, text="Nome do Patrimônio:")
label_patrimonio.pack()
entry_patrimonio = tk.Entry(frame_opcoes)
entry_patrimonio.pack()

label_descricao = tk.Label(frame_opcoes, text="Descrição:")
label_descricao.pack()
entry_descricao = tk.Entry(frame_opcoes)
entry_descricao.pack()

label_quantidade = tk.Label(frame_opcoes, text="Quantidade:")
label_quantidade.pack()
entry_quantidade = tk.Entry(frame_opcoes)
entry_quantidade.pack()

btn_registrar = tk.Button(frame_opcoes, text="Registrar Patrimônio", command=registrar_patrimonio)
btn_registrar.pack()

btn_listar = tk.Button(frame_opcoes, text="Listar Patrimônios", command=listar_patrimonios)
btn_listar.pack()

# Frame para manuseio dos itens
label_apagar = tk.Label(frame_opcoes, text="Nome do Patrimônio para apagar:")
label_apagar.pack()
entry_apagar = tk.Entry(frame_opcoes)
entry_apagar.pack()

btn_apagar = tk.Button(frame_opcoes, text="Apagar Registro", command=apagar_registro)
btn_apagar.pack()

label_saida = tk.Label(frame_opcoes, text="Nome do Patrimônio para saída:")
label_saida.pack()
entry_saida = tk.Entry(frame_opcoes)
entry_saida.pack()

label_local_destino = tk.Label(frame_opcoes, text="Local de Destino:")
label_local_destino.pack()
entry_local_destino = tk.Entry(frame_opcoes)
entry_local_destino.pack()

btn_registrar_saida = tk.Button(frame_opcoes, text="Registrar Saída", command=registrar_saida)
btn_registrar_saida.pack()

btn_listar_saidas = tk.Button(frame_opcoes, text="Listar Saídas", command=listar_saidas)
btn_listar_saidas.pack()

root.mainloop()
