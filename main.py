from Logic.crud import create
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    prajituri = []
    undo_list = []
    redo_list = []
    prajituri = create(prajituri, 1, 'ecler', 'gustos, foarte', 10, 500, 2013, undo_list, redo_list)
    prajituri = create(prajituri, 2, 'amandina', 'foarte dulce', 12, 600, 2020, undo_list, redo_list)
    prajituri = create(prajituri, 3, 'inghetata ciocolata', 'prea mult zahar', 17, 700, 2013, undo_list, redo_list)
    prajituri = create(prajituri, 4, 'tort', 'pentru mai multe persoane', 60, 2500, 2015, undo_list, redo_list)
    # prajituri = create(prajituri, 5, 'inghetata vanilie', 'fara ciocolata :(', 21, 300, 2020, undo_list, redo_list)
    # prajituri = create(prajituri, 6, 'cheese cake', 'nu imi place', 14, 700, 2020, undo_list, redo_list)
    # prajituri = create(prajituri, 7, 'brownie', 'de mai multe feluri', 23, 300, 2013, undo_list, redo_list)
    prajituri = run_ui(prajituri, undo_list, redo_list)


if __name__ == '__main__':
    test_crud()
    main()