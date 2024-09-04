import json
import time


def valorFinalSoma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA = SOMA + K
    print(f'Resposta: valor final é {SOMA}')

def fibonnaci(input):
    seq_fib = [0, 1]
    while seq_fib[-1] < input or len(seq_fib) < 3:
        prox = seq_fib[-1] + seq_fib[-2]
        seq_fib.append(prox)
        if input in seq_fib:
            print(seq_fib)
            print(f"Resposta: {input} está na sequencia")
            return
    print(f"Sequencia Fibonacci: {seq_fib}")
    print(f"Resposta: {input} não está na sequencia")

def lerDadosJson(caminho):
    with open(caminho, 'r',encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados

def faturamentoDiario(caminho):
    dados = lerDadosJson(caminho)
    media = tirarMedia(dados)
    dias_bons = 0
    menor_valor = dados[0]['valor']
    maior_valor = 0
    for i in dados:
        if i['valor'] == 0.0:
            continue
        if i['valor'] < menor_valor:
            menor_valor = i['valor']
        if i['valor'] > maior_valor:
            maior_valor = i['valor']
        if i['valor'] > media:
            dias_bons += 1
    
    print(f"""Resposta: 
Menor Valor: {menor_valor}
Maior Valor: {maior_valor}
Acima da média: {dias_bons} dias passaram de {media}
""")
    
def tirarMedia(dados):
    dias = 0
    total = 0
    for i in dados:
        if i['valor'] != 0.0:
            dias += 1
            total += i['valor']
    return total / dias

def valorTotalMensal(faturamentos):
    Dados = faturamentos
    valor_total = 0
    print("Resposta: ")
    for i in Dados:
        valor_total += i[1]
    for j in Dados:
        porcentagem = j[1] * 100 / valor_total
        print(f"{j[0]} - {j[1]} -  {round(porcentagem,2)}%")
    print(f'Faturamento Total: {round(valor_total,2)}')

def inverterString(string):
    string_invertida = ""
    for i in range(len(string)-1,-1,-1):
        string_invertida += string[i]

    print(f"\nResposta: {string_invertida}")



print("""1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?\n""")
valorFinalSoma()
print("\n")
input("Pressione Enter para próxima pergunta\n")


print("""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.\n""")

digito = input("Digite o numero: ")
while not digito.isdigit():
    print("Digite um numero valido!")
    digito = input("Digite o numero: ")
fibonnaci(int(digito))
print("\n")
input("Pressione Enter para próxima pergunta\n")

print("""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.\n""")
faturamentoDiario('Dados/dados.json')
print("\n")
input("Pressione Enter para próxima pergunta\n")

print("""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. \n""")
valorTotalMensal([["SP",67836.43],["RJ",36678.66],["MG",29229.88],["ES",27165.48],["Outros",19849.53]])
print("\n")
input("Pressione Enter para próxima pergunta\n")

print("""
5) Escreva um programa que inverta os caracteres de um string.""")
inverterString(input("Digite a string que será invertida: \n"))

print("\nFim do programa!")
input("Pressione Enter para sair...")

