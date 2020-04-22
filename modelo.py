# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:38:31 2020

@author: leonardo.patino
"""
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier

class Modelo:
    
    def ini(self,df):
        self.df = df
    
    def traducir(self,objeto):
        if objeto == "piedra":
            res = 1
        elif objeto == "papel":
            res = 2
        elif objeto == "tijera":
            res = 3
        return res
    
    def conv_res(self,res):
        if res == 1:
            salida = 2
        elif res == 2:
            salida = 3
        elif res == 3:
            salida = 1
        return salida
    
    def estadisticos(self):
        fre_piedra        = len(self.df[(self.df['jugador1'].isin(["piedra"]))])
        fre_piedra_gana   = len(self.df[(self.df['jugador1'].isin(["piedra"]) & self.df['ganador'].isin(["jugador1"]) )])
        fre_piedra_pierde = len(self.df[(self.df['jugador1'].isin(["piedra"]) & self.df['ganador'].isin(["maquina"]) )])
        fre_piedra_empata = len(self.df[(self.df['jugador1'].isin(["piedra"]) & self.df['ganador'].isin(["empate"]) )])    
        
        fre_papel         = len(self.df[(self.df['jugador1'].isin(["papel"]))])
        fre_papel_gana    = len(self.df[(self.df['jugador1'].isin(["papel"]) & self.df['ganador'].isin(["jugador1"]) )])
        fre_papel_pierde  = len(self.df[(self.df['jugador1'].isin(["papel"]) & self.df['ganador'].isin(["maquina"]) )])
        fre_papel_empata  = len(self.df[(self.df['jugador1'].isin(["papel"]) & self.df['ganador'].isin(["empate"]) )])
        
        fre_tijera        = len(self.df[(self.df['jugador1'].isin(["tijera"]))])
        fre_tijera_gana   = len(self.df[(self.df['jugador1'].isin(["tijera"]) & self.df['ganador'].isin(["jugador1"]) )])
        fre_tijera_pierde = len(self.df[(self.df['jugador1'].isin(["tijera"]) & self.df['ganador'].isin(["maquina"]) )])
        fre_tijera_empata = len(self.df[(self.df['jugador1'].isin(["tijera"]) & self.df['ganador'].isin(["empate"]) )])
        
        moda_ppt          = self.traducir(self.df["jugador1"].mode()[0])
        try:
            moda_gana_ppt = self.traducir(self.df[(self.df['ganador'].isin(["jugador1"]))]["jugador1"].mode()[0])
        except Exception as e:
            moda_gana_ppt = moda_ppt
        try:
            moda_pierde_ppt = self.traducir(self.df[(self.df['ganador'].isin(["maquina"]))]["jugador1"].mode()[0])
        except Exception as e:
            moda_pierde_ppt = moda_ppt
        try:
            moda_empata_ppt = self.traducir(self.df[(self.df['ganador'].isin(["empate"]))]["jugador1"].mode()[0])
        except Exception as e:
            moda_empata_ppt = moda_ppt
                               
        d2 = {  
         'numjugador1'      : self.df.loc[(len(self.df)-1):len(self.df),'numjugador1'][(len(self.df)-1)],        
         'jugador1'         : self.df.loc[(len(self.df)-1):len(self.df),'jugador1'][(len(self.df)-1)], 
         'maquina'          : self.df.loc[(len(self.df)-1):len(self.df),'maquina'][(len(self.df)-1)], 
         'ganador'          : self.df.loc[(len(self.df)-1):len(self.df),'ganador'][(len(self.df)-1)],      
         'fre_piedra'       : fre_piedra,
         'fre_piedra_gana'  : fre_piedra_gana,
         'fre_piedra_pierde': fre_piedra_pierde,
         'fre_piedra_empata': fre_piedra_empata,
         'fre_papel'        : fre_papel,
         'fre_papel_gana'   : fre_papel_gana,
         'fre_papel_pierde' : fre_papel_pierde,
         'fre_papel_empata' : fre_papel_empata,
         'fre_tijera'       : fre_tijera,
         'fre_tijera_gana'  : fre_tijera_gana,
         'fre_tijera_pierde': fre_tijera_pierde,
         'fre_tijera_empata': fre_tijera_empata,
         'moda_ppt'         : moda_ppt,
         'moda_gana_ppt'    : moda_gana_ppt,
         'moda_pierde_ppt'  : moda_pierde_ppt,
         'moda_empata_ppt'  : moda_empata_ppt     
         }
        df2 = pd.DataFrame(data=d2,index=[0])
               
        return df2
    
    def data_view(self):
        d3 = {
         'jugador1'         : self.df.loc[(len(self.df)-1):len(self.df),'jugador1'][(len(self.df)-1)], 
         'maquina'          : self.df.loc[(len(self.df)-1):len(self.df),'maquina'][(len(self.df)-1)], 
         'ganador'          : self.df.loc[(len(self.df)-1):len(self.df),'ganador'][(len(self.df)-1)],
         }        
        df3 = pd.DataFrame(data=d3,index=[0])
        return df3
    
    def scoreppt(self):
        ganadas = len(self.df[(self.df['ganador'].isin(["jugador1"]))])
        perdidas= len(self.df[(self.df['ganador'].isin(["maquina"]))])
        empate  = len(self.df[(self.df['ganador'].isin(["empate"]))])
        score   = ganadas/len(self.df)
        return ganadas,perdidas,empate,score
    
    def procesamiento(self,df2):
        y = df2['numjugador1']
        X = df2.loc[:,'fre_piedra':'moda_empata_ppt']
        """
        dataset_cuali_t = pd.get_dummies(X[["moda_ppt","moda_gana_ppt","moda_pierde_ppt","moda_empata_ppt"]])
        dataset_cuant_t = X[["fre_piedra","fre_piedra_gana","fre_piedra_pierde","fre_piedra_empata","fre_papel","fre_papel_gana","fre_papel_pierde","fre_papel_empata","fre_tijera","fre_tijera_gana","fre_tijera_pierde","fre_tijera_empata"]]
        X = np.concatenate((dataset_cuali_t, dataset_cuant_t), axis=1)  
        """
        return X,y
    
    def predict(self,X):   
        model = joblib.load('modelo_entrenado.pkl')
        predict = model.predict(X)[0]
        predict = self.conv_res(predict)
        return predict
               
    def fit(self,X,y,metodo="entrenar"):
        if metodo == "reentrenar":
            model = joblib.load('modelo_entrenado.pkl')
        elif metodo == "entrenar":
            model = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10, 20, 10, 5), random_state=1)        
        model.fit(X, y)
        model.predict(X)
        score = model.score(X, y)
        joblib.dump(model, 'modelo_entrenado.pkl')
        return score

"""
modelo = Modelo()
modelo.fit(modelo.procesamiento(df2)[0],modelo.procesamiento(df2)[1])
modelo.ini(df)
maquina = modelo.predict(modelo.procesamiento(modelo.estadisticos())[0])[0]
"""
      