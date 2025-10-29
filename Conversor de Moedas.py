def conversor(valor, moeda1, moeda2):
    valor_convertido = 0
    taxas = {
        ("real", "dolar"): 0.19, 
        ("real", "euro"): 0.16,
        ("real", "iene"): 28.49,
        ("dolar", "real"): 5.37,
        ("dolar", "euro"): 0.86,
        ("dolar", "iene"): 152.88,
        ("euro", "real"): 6.22,
        ("euro", "dolar"): 1.16,
        ("euro", "iene"): 177.12,
        ("iene", "real"): 0.035,
        ("iene", "dolar"): 0.0065,
        ("iene", "euro"): 0.0056
    }

    sigla = ""
    if(moeda2 == "real"):
        sigla = "BRL"

    elif(moeda2 == "dolar"):
        sigla = "USD"

    elif(moeda2 == "euro"):
        sigla = "EUR"

    elif(moeda2 == "iene"):
        sigla = "JPY"

    conversao = (moeda1, moeda2)
    return valor * taxas[conversao]

def main():
    print("====Tabela de moedas====")
    print("1 - Real")
    print("2 - Dólar")
    print("3 - Euro")
    print("4 - Iene")
    print("========================")

    opcoes = {1: "real", 2: "dolar", 3: "euro", 4: "iene"}
    siglas = {1: "BRL", 2: "USD", 3: "EUR", 4: "JPY"}

    valor = float(input("Qual o valor que você deseja converter: "))
    moeda1 = opcoes.get(int(input("Qual a moeda que você deseja converter: ")))
    moeda2 = int(input("Para qual moeda você deseja converter: "))

    moeda2_string = opcoes.get(moeda2)

    print(f"O valor convertido é {siglas.get(moeda2)} {conversor(valor, moeda1, moeda2_string):.2f}")

main()