print("=====LOJAS=====")
print(" ")

# Array
lojas = ["Santo André", "São Bernardo do Campo", "São Caetano do Sul", "Diadema"]

# Exibindo lojas
for i, loja in enumerate(lojas, 1):
    print(f"{i} - {loja}")
    print(" ")

# Escolhendo uma loja para exibição
loja_selecionada = int(input("Selecione a loja deseja: "))

# Exibindo a loja selecionada (caso exista)
if 1 <= loja_selecionada <= len(lojas):
    print(lojas[loja_selecionada -1])
else:
    print("Loja inválida")