# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:36:19 2020

@author: leonardo.patino
"""
# creamos la clase
class Ppt:
    # iniciamos con el método __init__
    def ini(self,j1,maquina):
        self.j1      = j1
        self.maquina = maquina        
               
    def traducir(self,objeto):
        if objeto == 1:
            res = "piedra"
        elif objeto == 2:
            res = "papel"
        elif objeto == 3:
            res = "tijera"
        return res    
    
    def reglas(self,j1,maquina):
        if j1 == "papel" and maquina == "papel":
            ganador = "empate"
        elif j1 == "papel" and maquina == "piedra":
            ganador = "jugador1"    
        elif j1 == "papel" and maquina == "tijera":
            ganador = "maquina" 
        elif j1 == "piedra" and maquina == "piedra":
            ganador = "empate" 
        elif j1 == "piedra" and maquina == "papel":
            ganador = "maquina" 
        elif j1 == "piedra" and maquina == "tijera":
            ganador = "jugador1" 
        elif j1 == "tijera" and maquina == "tijera":
            ganador = "empate"  
        elif j1 == "tijera" and maquina == "piedra":
            ganador = "maquina"
        elif j1 == "tijera" and maquina == "papel":
            ganador = "jugador1"    
        return ganador    
        
    def main(self):        
        j1 = self.traducir(self.j1)
        maquina = self.traducir(self.maquina)  
        ganador = self.reglas(j1,maquina) 
        numj1 = self.j1               
        return j1,maquina,ganador,numj1