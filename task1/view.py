from re import L
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

        elif menu[0] == "RPDA":
            pass

        elif menu[0] == "RPII":
            pass 

        elif menu[0] == "VNE":
            pass
 
        elif menu[0] == "VP":
            pass

        elif menu[0] == "EPE":
            pass

        elif menu[0] == "EUE":
            pass

        elif menu[0] == "EP":
            pass