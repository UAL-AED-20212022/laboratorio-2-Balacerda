from models.LinkedList import LinkedList
paises = LinkedList()


def RPI(paises, pais_novo):
    paises.insert_at_start(pais_novo)
    return paises.traverse_list()

def RPF(paises, pais_novo):
    paises.insert_at_end(pais_novo)
    return paises.traverse_list()

def RPDE(paises, pais_novo, pais_registado):
    paises.insert_after_item(pais_registado, pais_novo)
    return paises.traverse_list()

def RPAE(paises, pais_novo, pais_registado):
    paises.insert_before_item(pais_registado, pais_novo)
    return paises.traverse_list()

def RPII(paises, pais_novo, indice: int):
    paises.insert_at_index(indice, pais_novo)
    return paises.traverse_list()

def VNE(paises):
    return print(f"O número de elementos são {paises.get_count()}")

def VP(paises, nome_pais):
    if (paises.search_item(nome_pais) == False):
        return print(f"O país {nome_pais} não se encontra na lista")
    elif (paises.search_item(nome_pais) == True):
        return print(f"O país {nome_pais} encontra-se na lista")

def EPE(paises):
    primeiro_elemento = paises.start_node.item
    paises.delete_at_start()
    return print(f"O país {primeiro_elemento} foi eliminado da lista")

def EUE(paises):
    ultimo_elemento = paises.get_last_node()
    paises.delete_at_end()
    return print(f"O país {ultimo_elemento} foi eliminado da lista")

def EP(paises, nome_pais):
    if (paises.search_item(nome_pais) == False):
        return print(f"O país {nome_pais} não se encontra na lista")
    elif (paises.search_item(nome_pais) == True):
        paises.delete_element_by_value(nome_pais)
        return print(f"O país {nome_pais} foi eliminado da lista") 