# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:21:36 2020

@author: leonardo.patino
"""
import pandas as pd
from random import randint, uniform,random,sample
from ppt import Ppt
from modelo import Modelo        


partidas = 30
i = 0

while i < partidas:    
    gabela = 3                  
    # instancias
    juego=Ppt()
    modelo = Modelo() 
    
    print("**********Partida N:", i,"**********")
    #ENTRADA DEL USUARIO
    while True:
        try:
            j1 = int(input("1:piedra 2:papel 3:tijera     "))
            if j1 >= 1 and j1 <= 3:
                break
            else:
                print("asegurese de colocar un numero entre 1 y 3")
        except Exception as e:
                print("No se permiten letras, asegurese de colocar un numero entre 1 y 3")
    
    #VALIDAR SI PASARLE UN RANDOM O EL PREDICT
    try:
        df2
    except NameError: 
        maquina = int(randint(1,3))
        print("-> no existe df2")
        print("-> uso random")
    else:
        modelo.ini(df)
        modelo.fit(modelo.procesamiento(df2)[0],modelo.procesamiento(df2)[1])
        #maquina = modelo.predict(modelo.procesamiento(modelo.estadisticos())[0])[0] if len(df2) > gabela else int(randint(1,3))
        print("-> si existe df2")
        if len(df2) > gabela:
            maquina = modelo.predict(modelo.procesamiento(modelo.estadisticos())[0])
            print("-> uso predict")
        else:
            maquina = int(randint(1,3))
            print("-> uso random")
    
    #INICIALIZAR VARIABLES             
    juego.ini(j1,maquina)
    res1 = juego.main()[0]
    res2 = juego.main()[1]
    res3 = juego.main()[2]
    res4 = juego.main()[3]
    
    try:
        v_j1 
    except NameError: 
        v_j1 = []
    try:
        v_maquina 
    except NameError: 
        v_maquina = []
    try:
        v_ganador
    except NameError: 
        v_ganador = []
    try:
        v_numj1
    except NameError: 
        v_numj1 = []    
        
    v_j1.append(res1)
    v_maquina.append(res2)
    v_ganador.append(res3)
    v_numj1.append(res4)
    
    d = {
         'jugador1'    : v_j1, 
         'numjugador1' : v_numj1, 
         'maquina'     : v_maquina, 
         'ganador'     : v_ganador
         }
    
    df = pd.DataFrame(data=d)
    
    if len(df) > gabela:
        try:
            df2
        except NameError: 
            modelo.ini(df)
            df2 = modelo.estadisticos()
        else:
            df2 = pd.concat([df2, modelo.estadisticos()])
    
    modelo.ini(df)
    df3 = modelo.data_view()        
    print(modelo.data_view())
    print("Ganadas:",modelo.scoreppt()[0],"-> Perdidas:",modelo.scoreppt()[1],"-> Empates:",modelo.scoreppt()[2],"-> Score:",modelo.scoreppt()[3])     
    i = i + 1

#df.drop([4,4], inplace=True)
 

    
    