#ESTRUTURA DE REPETIÇÃO-pesquisa de satisfação TudoWeb
# entrada e processamento de dados
satisfacao_boa = 0
satisfacao_ruim = 0
for i in range(1, 11):
    Pesquisa = input("Bem-vindo a pesquisa de satisfação da TudoWeb! Por favor, digite seu nome:")
    idade_cliente= int(input("Digite sua idade:"))
    while idade_cliente < 0 or idade_cliente > 120:
        print("Por favor, digite uma idade válida para continuar:")
        idade_cliente = int(input("Digite sua idade:"))
    satisfacao = int(input("Em uma escala de 1 a 3, como você avalia nosso atendimento? " \
"sendo, 1- Excelente, 2- Bom, 3- Ruim:   "))
    if satisfacao == 1:
        print("Muito obrigada, sua avaliação é essencial para nossa evolução!")
    elif satisfacao == 2:
        print("Muito obrigada, sua avaliação é essencial para nossa evolução!")
    else:
        print("Lamentamos sua insatisfação, por favor, poderia nos informar onde podemos melhorar?")
        insatisfacao = input("Digite sua opinião: ")
        print("Resposta registrada, muito obrigada por sua contribuição!")
    if satisfacao == 1 or satisfacao == 2:
            satisfacao_boa += 1
    else:
            satisfacao_ruim += 1


#saída de dados
print("E Vamos aos resultados da nossa pesquisa!!")

if satisfacao_boa >= 5:
        print("Que ótimo, estamos com um total de", satisfacao_boa, "avaliações boas a frente de" , satisfacao_ruim, "avaliações ruins!! Muito bem equipe!!")
else:   print("Que pena, estamos com um total de", satisfacao_ruim, "avaliações ruins a frente de" , satisfacao_boa, "avaliações boas. Vamos trabalhar para melhorar!!")