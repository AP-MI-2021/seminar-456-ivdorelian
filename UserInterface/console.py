
from Logic.max_calorii_per_an import get_max_calorii_per_an
from Domain.praitura import get_str, get_nume, get_descriere, get_pret, get_calorii, get_an_introducere, \
    creeaza_prajitura
from Logic.crud import create, read, update, delete
from Logic.ordonare_raport_pret_calorii import get_ordonare_raport_pret_calorii
from Logic.reducere_pret import reducere_pret_pentru_nume
from Logic.undo_redo import do_undo, do_redo
from Logic.undo_redo_efficient import do_undo_efficient, do_redo_efficient


def handle_add(prajituri, undo_list, redo_list):
    try:
        id_prajitura = int(input('Dati id-ul prajiturii: '))
        nume = input('Dati numele prajiturii: ')
        descriere = input('Dati descrierea prajiturii: ')
        pret = float(input('Dati pretul prajiturii: '))
        calorii = int(input('Dati caloriile prajiturii: '))
        an_introducere = int(input('Dati anul introducerii prajiturii: '))
        return create(prajituri, id_prajitura, nume, descriere, pret, calorii, an_introducere, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri

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


def handle_update(prajituri, undo_list, redo_list):
    try:
        id_prajitura = int(input('Dati id-ul prajiturii care se actualizeaza: '))
        nume = input('Dati noul nume al prajiturii: ')
        descriere = input('Dati noua descriere prajiturii: ')
        pret = float(input('Dati noul pret al prajiturii: '))
        calorii = int(input('Dati noile calorii ale prajiturii: '))
        an_introducere = int(input('Dati noul an al introducerii prajiturii: '))
        updated = creeaza_prajitura(id_prajitura, nume, descriere, pret, calorii, an_introducere)
        return update(prajituri, updated, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri

def handle_delete(prajituri, undo_list, redo_list):

    try:
        id_prajitura = int(input('Dati id-ul prajiturii care se va sterge: '))
        prajituri = delete(prajituri, id_prajitura, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return prajituri
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri

def handle_crud(prajituri, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii prajitura')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            prajituri = handle_add(prajituri, undo_list, redo_list)
        elif optiune == '2':
            prajituri = handle_update(prajituri, undo_list, redo_list)
        elif optiune == '3':
            prajituri = handle_delete(prajituri, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(prajituri)
        elif optiune == 'd':
            handle_show_details(prajituri)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return prajituri


def handle_reducere_pret(prajituri):
    try:
        nume = input('Dati stringul cautat in nume pentru reducerea preturilor: ')
        procentaj = float(input('Dati procentajul cu care va fi redus pretul (intre 0 si 100): '))

        prajituri = reducere_pret_pentru_nume(prajituri, nume, procentaj)

        print('Preturile au fost reduse cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri


def show_menu():
    print('1. CRUD')
    print('2. Reducere pret pentru anumite prajituri.')
    print('3. TODO.')
    print('4. Prajiturile cu numar maxim de calorii din fiecare an.')
    print('5. Ordonoarea prajiturilor dupa raportul pret / calorii.')
    print('u. Undo.')
    print('r. Redo.')
    print('x. Exit')

def handle_max_calorii_per_an(prajituri):
    result = get_max_calorii_per_an(prajituri)

    for an in result:
        print(f'{an}: {get_str(result[an])}')

def handle_ordonare_raport_pret_calorii(prajituri):
    ordonate = get_ordonare_raport_pret_calorii(prajituri)
    handle_show_all(ordonate)


def handle_undo(prajituri, undo_list, redo_list):
    #undo_result = do_undo(undo_list, redo_list, prajituri)
    undo_result = do_undo_efficient(undo_list, redo_list, prajituri)
    if undo_result is not None:
        return undo_result
    return prajituri


def handle_redo(prajituri, undo_list, redo_list):
    # redo_result = do_redo(undo_list, redo_list, prajituri)
    redo_result = do_redo_efficient(undo_list, redo_list, prajituri)
    if redo_result is not None:
        return redo_result
    return prajituri


def run_ui(prajituri, undo_list, redo_list):

    while True:
        handle_show_all(prajituri)
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            prajituri = handle_crud(prajituri, undo_list, redo_list)
        elif optiune == '2':
            prajituri = handle_reducere_pret(prajituri)
        elif optiune == '3':
            pass # TODO
        elif optiune == '4':
            handle_max_calorii_per_an(prajituri)
        elif optiune == '5':
            handle_ordonare_raport_pret_calorii(prajituri)
        elif optiune == 'u':
            prajituri = handle_undo(prajituri, undo_list, redo_list)
        elif optiune == 'r':
            prajituri = handle_redo(prajituri, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return prajituri
