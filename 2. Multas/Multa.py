placa = input("Placa do veículo: ")
valocidade_veiculo = float(input("Velocidade do veículo: "))
velocidade_permitida = float(input("Velocidade Máxima Permitida: "))

gravissima = velocidade_permitida*0.51
grave = velocidade_permitida*0.21

if valocidade_veiculo > velocidade_permitida:
    if valocidade_veiculo > (velocidade_permitida + gravissima):
        print("Infração gravíssima: Multa de R$ 880,41")
    elif valocidade_veiculo > (velocidade_permitida + grave):
        print("Infração grave: Multa de R$ 195,23")
    else:
        print("Infração média: Multa de R$ 130,16")
else:
    print("Veículo dentro do limite de velocidade permitido.")