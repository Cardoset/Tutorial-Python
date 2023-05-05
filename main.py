nome = 'gabriel'
idade = 25
peso = 99.75
altura = 175

print(f'Nome: {nome},Idade: {idade},Peso; {peso}.Altura: {altura}',)

sede = 5
fome = 5
cansaco = 10
necessidades = 0
sono = 2

print(f'Sede:{sede}, Fome:{fome}, Cansaço:{cansaco}, Necessidades:{necessidades}, Sono:{sono}')

# comer lanche com meu amigo nizio
fome -= 0
sede += 2
necessidades += 2

print(f'Sede:{sede}, Fome:{fome}, Cansaço:{cansaco}, Necessidades:{necessidades}, Sono:{sono}')

if fome > 0 and fome < 5 :
    print("ainda estou com fome")
elif 10 > fome >= 5  :
    print("Estou com muita fome")

else:
    print("estou sem fome")

while True: # função de loop infinita (até que seja executada o break)

    horas = input("quantas horas deseja dormir?")

    try:
        horas = int(horas) # converte string para inteiro
    except:
        print('voce não vai dormir se continuar falando errado')  # retorna erro, caso aconteça algum erro no try
    else: # se o try for bem sucedido
        if horas >10 :
            print(" voce nao pode dormir mais que 10 horas talkey!!!")
        elif horas <= 0:
            print("voce precisar dormir pelo menos 1 hora")
        else:
            break

print(f'voce vai dormir {horas} horas!')