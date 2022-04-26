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
            RPI(paises, pais_novo)

        elif menu[0] == "RPF":
            pass

        elif menu[0] == "RPDE":               
            pass

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

def RPI(paises, pais_novo):
    c.RPI(paises, pais_novo)