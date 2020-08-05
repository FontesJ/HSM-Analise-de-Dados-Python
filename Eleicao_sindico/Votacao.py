qtd_candidatos = 10
azul = 0
vermelho = 0
amarelo = 0
nulo = 0

while qtd_candidatos > 3:
    qtd_candidatos = int(input("Quantos candidatos concorrerão? (Máximo 3): "))
    if qtd_candidatos > 3:
        print("O número de candidatos deve ser no máximo 3!")

qtd_chapas = qtd_candidatos
chapas = ['Azul', 'Vermelho', 'Amarelo']
candidatos = ['Nenhum', 'Nenhum', 'Nenhum']

for n in range(0, qtd_candidatos):
    candidatos[n] = input("Nome do candidato: ")

for x in range(0, 35):
    if candidatos[2] != 'nenhum':
        print('Candidatos: ', '\n1. Azul: ',     candidatos[0],
                              '\n2. Vermelho: ', candidatos[1],
                              '\n3. Amarelo: ',  candidatos[2])
    elif candidatos[1] != 'nenhum':
        print('Candidatos: ',   '\n1. Azul: ',     candidatos[0],
                                '\n2. Vermelho: ', candidatos[1])
    elif candidatos[0] != 'nenhum':
        print('Candidatos: ', '\n1. Azul: ', candidatos[0])
    else:
        print('Não há nenhum candidato!')

    voto = int(input('Qual é o seu voto (1, 2 ou 3; 0 para nulo): '))

    if voto == 1 :
        azul += 1
    elif voto == 2:
        vermelho += 1
    elif voto == 3:
        amarelo += 1
    elif voto == 0:
        nulo +=1
    else:
        'Voto inválido!'

print('Apuração de votos: ')
print('Azul: ', azul)
print('Vermelho: ', vermelho)
print('Amarelo: ', amarelo)
print('Nulos: ', nulo)

if azul > vermelho and azul > amarelo:
    print('O SÍNDICO ELEITO É', candidatos[0])
elif vermelho > azul and vermelho > amarelo:
    print('O SÍNDICO ELEITO É', candidatos[1])
elif amarelo > azul and amarelo > vermelho:
    print('O SÍNDICO ELEITO É', candidatos[2])