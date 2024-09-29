import qrcode # Certifique-se de ter este módulo instalado
from datetime import datetime
import os
from tkinter import filedialog, messagebox
import tkinter as tk

def cadastrar_produto():
    nome_fiscal = input("Digite o nome do fiscal: ")
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))

    # Abrir o diálogo de seleção de pasta
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal do Tkinter
    pasta_destino = filedialog.askdirectory(title="Selecione a pasta para salvar o QR code")
    root.destroy()

    if not pasta_destino:
        print("Nenhuma pasta selecionada. O QR code não será salvo.")
        return

    hora_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Gerar o QR code com os dados do produto
    dados_qr = f"Produto: {nome_produto}\nFiscal: {nome_fiscal}\nQuantidade: {quantidade}\nCadastrado em: {hora_cadastro}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(dados_qr)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Salvar o QR code na pasta escolhida
    nome_arquivo_qr = f"qr_{nome_produto.replace(' ', '_')}.png"
    caminho_completo_qr = os.path.join(pasta_destino, nome_arquivo_qr)
    img.save(caminho_completo_qr)
    print(f"QR code salvo em: {caminho_completo_qr}")

    # Opção de impressão (você precisará instalar e configurar uma biblioteca de impressão)
    imprimir = messagebox.askyesno("Imprimir QR Code", "Deseja imprimir o QR Code?")
    if imprimir:
        try:
            # ... (código para imprimir o QR code usando a biblioteca adequada) ...
            print("QR code impresso com sucesso!")
        except Exception as e:
            print(f"Erro ao imprimir o QR code: {e}")

    # Log de cadastro
    with open("log_produtos.txt", "a") as arquivo_log:
        # Alteração na ordem dos campos no log
        arquivo_log.write(f"Fiscal: {nome_fiscal}, Produto: {nome_produto}, Quantidade: {quantidade}, Cadastrado em: {hora_cadastro}, QR code: {caminho_completo_qr}\n")

# Exemplo de uso
cadastrar_produto()
