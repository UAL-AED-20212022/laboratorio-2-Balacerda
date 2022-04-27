import controller as c
from models.LinkedList import LinkedList

paises = LinkedList()

def main():
    while True:
        menu_raw = input()
        menu = menu_raw.split()
    
        if menu_raw == "":
            return 0

        elif menu[0] == "RPI":
            pais_novo = menu[1]
            c.RPI(paises, pais_novo)

        elif menu[0] == "RPF":
            pais_novo = menu[1]
            c.RPF(paises, pais_novo)

        elif menu[0] == "RPDE":               
            pais_novo = menu[1]
            pais_registado = menu[2]
            c.RPDE(paises, pais_novo, pais_registado)

        elif menu[0] == "RPAE":
            pais_novo = menu[1]
            pais_registado = menu[2]
            c.RPAE(paises, pais_novo, pais_registado)

        elif menu[0] == "RPII":
            pais_novo = menu[1]
            indice = int(menu[2])
            c.RPII(paises, pais_novo, indice)

        elif menu[0] == "VNE":
            c.VNE(paises)
 
        elif menu[0] == "VP":
            nome_pais = menu[1]
            c.VP(paises, nome_pais)

        elif menu[0] == "EPE":
            c.EPE(paises)

        elif menu[0] == "EUE":
            c.EUE(paises)

        elif menu[0] == "EP":
            nome_pais = menu[1]
            c.EP(paises, nome_pais)