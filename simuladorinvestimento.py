 #I.R Até 180 dias: 22,5%
#De 181 a 360 dias: 20%
#De 361 a 720 dias: 17,5%
#A partir de 721 dias: 15%.

#Taxa B3 0.25% ao ano

# rentabilidade = Preço de venda/Preço de compra - 1 
while True:
    print("-----------------------------------")
    print("     Seja bem-vindo(a) ao MyBank   ")
    print("      SIMULADOR DE INVESTIMENTO    ")
    print("-----------------------------------")

    print ("Titulos disponiveis:")
    print ("1 - Tesouro Prefixado 2024")
    print ("2 - Tesouro Prefixado 2026")
    cliente = str(input("Qual titulo você gostaria de fazer uma simulação?:"))
    if cliente == '1':
        investir = float(input("Qual o valor você quer investir?:"))
        mês = float(input("Se você for investir todo o mês, qual o valor?:"))
        aportes = 32
        total = (mês * aportes) + investir
        rentabilidade = total / investir - 1 
        bruto = total * (rentabilidade/100)
        valorbruto = bruto + total
        IR = (15/100)
        b3 = (0.25/100) * 3
    else:
        investir = float(input("Qual o valor você quer investir?:"))
        mês = float(input("Se você for investir todo o mês, qual o valor?:"))
        aportes = 50
        total = (mês * aportes) + investir
        rentabilidade = total / investir - 1 
        bruto = total * (rentabilidade/100)
        valorbruto = bruto + total
        IR = (15/100)
        b3 = (0.25/100) * 5

    IRtotal = (valorbruto - total) * IR

    b3total = (valorbruto - total) * b3

    valorliquido = valorbruto - (IRtotal + b3total)

    print("-----------------------------------")       
    print("      RESULTADO DA SIMULAÇÃO       ")
    print("-----------------------------------")

    print("Valor inicial investido: {}".format(investir))
    print("Aportes de {} por {} meses".format(mês,aportes))
    print("Valor total investido {}".format(total))
    print("-----------------------------------")  
    print("Valor Bruto: {}".format(valorbruto))
    print("I.R: {}".format(IRtotal))
    print("Taxa da B3: {}".format(b3total))
    print("Valor Liquido: {}".format(valorliquido))
    print("-----------------------------------") 
    opcao = str(input("Deseja realizar outra simulação? s/n: "))
    if opcao == 'n':
        break
print ("Progrma Encerrado")
