 #I.R Até 180 dias: 22,5%
#De 181 a 360 dias: 20%
#De 361 a 720 dias: 17,5%
#A partir de 721 dias: 15%.

#Taxa B3 0.25% ao ano

# rentabilidade = Preço de venda/Preço de compra - 1 

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
    total = mês * aportes

IRtotal =  (IR * valorbruto) 

b3total = valorbruto - (valorbruto - b3)


valortotal = valorbruto - (IRtotal + b3total)

print("Valor inicial investido: {}".format(investir))
print("Aportes de {} por {} meses".format(mês,aportes))
print("Valor total investido {}".format(total))
print(rentabilidade)
print(valorbruto)
print(IRtotal)
print(b3total)
print(valortotal)