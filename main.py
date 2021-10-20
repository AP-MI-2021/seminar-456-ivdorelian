from Logic.crud import create
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    prajituri = []
    prajituri = create(prajituri, 1, 'ecler', 'gustos, foarte', 10, 500, 1990)
    prajituri = run_ui(prajituri)

if __name__ == '__main__':
    test_crud()
    main()