from Domain.praitura import get_an_introducere, get_calorii


def get_max_calorii_per_an(lst_prajituri):
    """
    TODO specificatii
    :param lst_prajituri:
    :return: un dictionar in care cheia este anul si valoarea
             este prajitura cu numar maxim de calorii
             din acel an.
    """
    result = {} # result[x] = prajitura cu nr maxim de calorii din anul x
    for prajitura in lst_prajituri:
        an = get_an_introducere(prajitura)
        calorii = get_calorii(prajitura)
        if an not in result:
            result[an] = prajitura
        else: # se poate folosi elif
            if calorii > get_calorii(result[an]):
                result[an] = prajitura

    return result