import os

cadeiras = {}
qtd_cadeiras = 10

for i in range(qtd_cadeiras):
    cadeiras[f'B{i + 1}'] = f"[B {i + 1}]"
    print(f" [B {i + 1}]", end=' ')

print("\n", "-" * 70)

while True:
    reserva = input("Reservar a cadeira: ").upper()

    try:
        if cadeiras[reserva] == '[ --- ]':
            print('ERRO: Lugar ocupado!')
        else:
            print(f"CADEIRA {cadeiras[reserva]} RESERVADA!")
            cadeiras.update({reserva: '[ --- ]'})
    except KeyError:
        print("ERRO: Cadeira não existe!")

    simnao = input("\nDeseja reservar outra cadeira? (s/n) ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if simnao.lower() != 's':
        print("As cadeiras reservadas foram as seguintes: ")
        for i in cadeiras.values():
            print(i, end=' ')
        break
    else:
        for i in cadeiras.values():
            print(i, end=' ')
        print("\n", "-" * 65)
        continue