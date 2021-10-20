from Domain.praitura import get_str, get_nume, get_descriere, get_pret, get_calorii, get_an_introducere, \
    creeaza_prajitura
from Logic.crud import create, read, update, delete


def show_menu():
    print('1. CRUD')
    print('2. Reducere pret pentru anumite prajituri.')
    print('x. Exit')


def handle_add(prajituri):
    id_prajitura = int(input('Dati id-ul prajiturii: '))
    nume = input('Dati numele prajiturii: ')
    descriere = input('Dati descrierea prajiturii: ')
    pret = float(input('Dati pretul prajiturii: '))
    calorii = int(input('Dati caloriile prajiturii: '))
    an_introducere = int(input('Dati anul introducerii prajiturii: '))
    return create(prajituri, id_prajitura, nume, descriere, pret, calorii, an_introducere)


def handle_show_all(prajituri):
    for prajitura in prajituri:
        print(get_str(prajitura))


def handle_show_details(prajituri):
    id_prajitura = int(input('Dati id-ul prajiturii pentru care doriti detalii: '))
    prajitura = read(prajituri, id_prajitura)
    print(f'Nume: {get_nume(prajitura)}')
    print(f'Descriere: {get_descriere(prajitura)}')
    print(f'Pret: {get_pret(prajitura)}')
    print(f'Calorii: {get_calorii(prajitura)}')
    print(f'An introducere: {get_an_introducere(prajitura)}')


def handle_update(prajituri):
    id_prajitura = int(input('Dati id-ul prajiturii care se actualizeaza: '))
    nume = input('Dati noul nume al prajiturii: ')
    descriere = input('Dati noua descriere prajiturii: ')
    pret = float(input('Dati noul pret al prajiturii: '))
    calorii = int(input('Dati noile calorii ale prajiturii: '))
    an_introducere = int(input('Dati noul an al introducerii prajiturii: '))
    return update(prajituri, creeaza_prajitura(id_prajitura, nume, descriere, pret, calorii, an_introducere))


def handle_delete(prajituri):
    id_prajitura = int(input('Dati id-ul prajiturii care se va sterge: '))
    prajituri = delete(prajituri, id_prajitura)
    print('Stergerea a fost efectuata cu succes.')
    return prajituri


def handle_crud(prajituri):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii prajitura')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            prajituri = handle_add(prajituri)
        elif optiune == '2':
            prajituri = handle_update(prajituri)
        elif optiune == '3':
            prajituri = handle_delete(prajituri)
        elif optiune == 'a':
            handle_show_all(prajituri)
        elif optiune == 'd':
            handle_show_details(prajituri)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return prajituri


def run_ui(prajituri):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            prajituri = handle_crud(prajituri)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return prajituri