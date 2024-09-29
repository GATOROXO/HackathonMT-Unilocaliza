import random
from datetime import datetime

def emitir_nota_fiscal():
    # Coleta de informações básicas
    emitente = input("Nome do emitente: ")
    cnpj_emitente = input("CNPJ do emitente: ")
    destinatario = input("Nome do destinatario: ")
    cnpj_destinatario = input("CNPJ do destinatario: ")
    descricao_produtos = input("Descrição dos produtos/serviços: ")
    valor_total = float(input("Valor total da nota: "))

    # Geração de identificadores seriais aleatórios
    numero_nota = random.randint(100000000, 999999999)
    serie_nota = random.randint(1, 999)
    chave_acesso = ''.join(random.choices('0123456789', k=44))

    # Data e hora de emissão
    data_emissao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simulação da emissão da nota (sem comunicação com sistemas externos)
    print("\n--- Nota Fiscal Eletrônica ---")
    print(f"Emitente: {emitente} (CNPJ: {cnpj_emitente})")
    print(f"Destinatario: {destinatario} (CNPJ: {cnpj_destinatario})")
    print(f"Descrição: {descricao_produtos}")
    print(f"Valor total: R$ {valor_total:.2f}")
    print(f"Número: {numero_nota}, Série: {serie_nota}")
    print(f"Chave de acesso: {chave_acesso}")
    print(f"Data de emissão: {data_emissao}")
    print("-----------------------------\n")

# Exemplo de uso
emitir_nota_fiscal()
