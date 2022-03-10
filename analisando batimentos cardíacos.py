print("{:=^40}".format("Analisando Batimentos"))
bpm = int(input("Insira seus batimentos cardiácos: "))
idade = int(input("Insira a sua idade em anos: "))
if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Dentro da faixa da normalidade")
    if bpm < 120:
        print("Abaixo da faixa adequada")
    if bpm > 140:
        print("Acima da faixa adequada")
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Batimentos dentro da faixa de normalidade")
    if bpm < 80:
        print("Abaixo da faixa da normalidade")
    if bom > 100:
        print("Acima da faixa de normalidade")
elif idade >= 18 and idade <= 65:
    if bpm >= 70 and bpm <= 80:
        print ("Dentro da faixa da normalidade")
    if bpm < 70:
        print("Batimentos abaixo da faixa da normalidade")
    if bpm > 80:
        print("Acima da faixa da normalidade")
elif idade > 65:
    if bpm >= 50 and bpm <= 60:
        print("Batimentos dentro da normalidade")
    if bpm < 50:
        print("Batimentos abaixo da normalidade")
    if bpm > 60:
        print("batimentos acima da normalidade")
else:
    print("Não constam dados")