# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
  if cupom == "DESCONTO20":
    preco_final = float(preco - 20 - (100 * descontos[cupom]))
    print(f"{preco_final:.2f}")
  else:
    preco_final = float(preco - (100 * descontos[cupom]))
    print(f"{preco_final:.2f}")