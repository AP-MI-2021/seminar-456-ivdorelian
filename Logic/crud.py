from Domain.praitura import creeaza_prajitura, get_id


def create(lst_prajituri,
           id_prajitura: int, nume, descriere, pret, calorii, an_introducere):
    """
    TODO
    :param lst_prajituri: lista de prajituri.
    :param id_prajitura:
    :param nume:
    :param descriere:
    :param pret:
    :param calorii:
    :param an_introducere:
    :return: o noua lista formata din lst_prajituri si noua prajitura adaugata.
    """

    if read(lst_prajituri, id_prajitura) is not None:
        raise ValueError(f'Exista deja o prajitura cu id-ul {id_prajitura}')

    prajitura = creeaza_prajitura(id_prajitura, nume, descriere, pret, calorii, an_introducere)
    #lst_prajituri.append(prajitura)
    return lst_prajituri + [prajitura]


def read(lst_prajituri, id_prajitura: int=None):
    """
    Citeste o prajitura din "baza de date".
    :param lst_prajituri: lista de prajituri
    :param id_prajitura: id-ul prajiturii dorite.
    :return:
        - prajitura cu id-ul id_prajitura, daca exista
        - lista cu toate prajiturile, daca id_prajitura=None
        - None, daca nu exista o prajitura cu id_prajitura
    """

    if not id_prajitura:
        return lst_prajituri

    prajitura_cu_id = None
    for prajitura in lst_prajituri:
        if get_id(prajitura) == id_prajitura:
            prajitura_cu_id = prajitura

    if prajitura_cu_id:
        return prajitura_cu_id
    return None

def update(lst_prajituri, new_prajitura):
    """
    Actualizeaza o prajitura.
    :param lst_prajituri: lista de prajituri.
    :param new_prajitura: prajitura care se va actualiza - id-ul trebuie sa fie unul existent.
    :return: o lista cu prajitura actualizata.
    """

    # lst_prajituri=[p1:(1,ecler), p2:(2,amandina)], prajitura=(2,lavacake)

    if read(lst_prajituri, get_id(new_prajitura)) is None:
        raise ValueError(f'Nu xista o prajitura cu id-ul {get_id(new_prajitura)} pe care sa o actualizam.')

    new_prajituri = []
    for prajitura in lst_prajituri:
        if get_id(prajitura) != get_id(new_prajitura):
            new_prajituri.append(prajitura)
        else:
            new_prajituri.append(new_prajitura)
    return new_prajituri


def delete(lst_prajituri, id_prajitura: int):
    """

    :param lst_prajituri:
    :param id_prajitura:
    :return: o lista de prajitura fara prajitura cu id-ul id_prajitura.
    """

    if read(lst_prajituri, id_prajitura) is None:
        raise ValueError(f'Nu xista o prajitura cu id-ul {id_prajitura} pe care sa o stergem.')


    new_prajituri = []
    for prajitura in lst_prajituri:
        if get_id(prajitura) != id_prajitura:
            new_prajituri.append(prajitura)

    return new_prajituri

