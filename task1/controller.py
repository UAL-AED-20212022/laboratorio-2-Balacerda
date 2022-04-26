import models.LinkedList as l


def RPI(paises, pais_novo):
    paises.insert_at_start(pais_novo)
    return paises.traverse_list()

def RPF(paises, pais_novo):
    paises.insert_at_end(pais_novo)
    return paises.traverse_list()

def RPDE(paises, pais_novo, pais_registado):
    paises.insert_after_item(pais_novo, pais_registado)
    return paises.traverse_list()

def RPAE():
    pass

def RPII():
    pass

def VNE():
    pass

def VP():
    pass

def EPE():
    pass

def EUE():
    pass

def EP():
    pass
