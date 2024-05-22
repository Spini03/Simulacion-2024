import statistics as st
from math import radians
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

cant_ganadas1, cant_ganadas2, cant_ganadas3, cant_ganadas4, cant_ganadas5 = 0, 0, 0, 0, 0
cant_tiradas = 500
valor_prom_esperada=18
valor_fr_esperada=1/37
valor_var_esperada=114
valor_desvio_esperado=10.67707825

tiradas = []
valores_ruleta1, valores_ruleta2, valores_ruleta3, valores_ruleta4, valores_ruleta5 = [], [], [], [], []
f_relativa_1, f_relativa_2, f_relativa_3, f_relativa_4, f_relativa_5, fr_esperada = [], [], [], [], [], []
media1, media2, media3, media4, media5, media_esperada = [], [], [], [], [], []
varianza1, varianza2, varianza3, varianza4, varianza5, varianza_esperada = [], [], [], [], [], []
desvio1, desvio2, desvio3, desvio4, desvio5, desvio_esperado = [], [], [], [], [], []

band=False
while band==False:
    valor=int(input("Ingrese valor entre 0 y 36: "))
    if 0<=valor<=36:
        band=True
        for s in range(0, cant_tiradas):

            num = np.random.randint(0,37)
            num1 = np.random.randint(0,37)
            num2 = np.random.randint(0,37)
            num3 = np.random.randint(0,37)
            num4 = np.random.randint(0,37)
            tiradas.append(s)
            f_relativa_1.append(cant_ganadas1/(s+1))
            f_relativa_2.append(cant_ganadas2/(s+1))
            f_relativa_3.append(cant_ganadas3/(s+1))
            f_relativa_4.append(cant_ganadas4/(s+1))
            f_relativa_5.append(cant_ganadas5/(s+1))
            fr_esperada.append(valor_fr_esperada)
            valores_ruleta1.append(num)
            valores_ruleta2.append(num1)
            valores_ruleta3.append(num2)
            valores_ruleta4.append(num3)
            valores_ruleta5.append(num4)
            media1.append(np.mean(valores_ruleta1))
            media2.append(np.mean(valores_ruleta2))
            media3.append(np.mean(valores_ruleta3))
            media4.append(np.mean(valores_ruleta4))
            media5.append(np.mean(valores_ruleta5))
            media_esperada.append(valor_prom_esperada)
            if(s!=0):
                varianza1.append(st.variance(valores_ruleta1))
                varianza2.append(st.variance(valores_ruleta2))
                varianza3.append(st.variance(valores_ruleta3))
                varianza4.append(st.variance(valores_ruleta4))
                varianza5.append(st.variance(valores_ruleta5))
                varianza_esperada.append(valor_var_esperada)
                desvio1.append(st.stdev(valores_ruleta1))
                desvio2.append(st.stdev(valores_ruleta2))
                desvio3.append(st.stdev(valores_ruleta3))
                desvio4.append(st.stdev(valores_ruleta4))
                desvio5.append(st.stdev(valores_ruleta5))
                desvio_esperado.append(valor_desvio_esperado)
            if(int(num) == valor):
                cant_ganadas1 = cant_ganadas1 + 1
            if(int(num1) == valor):
                cant_ganadas2 = cant_ganadas1 + 1
            if(int(num2) == valor):
                cant_ganadas3 = cant_ganadas1 + 1
            if(int(num3) == valor):
                cant_ganadas4 = cant_ganadas1 + 1
            if(int(num4) == valor):
                cant_ganadas5 = cant_ganadas1 + 1
            print("Progreso: ", s/cant_tiradas*100, "%")

        fig=plt.figure("Simulación de Ruleta", figsize=(15,10))
        funcion_fr=fig.add_subplot(211)
        histograma_fr=fig.add_subplot(212)
        
        funcion_fr.plot(tiradas,f_relativa_1, color="red")
        funcion_fr.plot(tiradas,f_relativa_2, color="blue")
        funcion_fr.plot(tiradas,f_relativa_3, color="green")
        funcion_fr.plot(tiradas,f_relativa_4, color="yellow")
        funcion_fr.plot(tiradas,f_relativa_5, color="orange")
        funcion_fr.plot(tiradas,fr_esperada)
        funcion_fr.set_title(f"Frecuencias Relativas - Valor de ruleta elegido: {valor}")   # Establece el título del gráfico
        funcion_fr.set_xlabel("N° de tirada")   # Establece el título del eje x
        funcion_fr.set_ylabel("Frecuencia Relativa")   # Establece el título del eje y
        funcion_fr.legend()
        
        eje_x = range(0,37)
        absisa=[]
        for i in eje_x:
            cont=0
            for j in valores_ruleta1:
                if j==i:
                    cont=cont+1
            for j in valores_ruleta2:
                if j==i:
                    cont=cont+1
            for j in valores_ruleta3:
                if j==i:
                    cont=cont+1
            for j in valores_ruleta4:
                if j==i:
                    cont=cont+1
            for j in valores_ruleta5:
                if j==i:
                    cont=cont+1
            absisa.append(cont/(cant_tiradas*5))
        histograma_fr.bar(eje_x, absisa, align='center')
        histograma_fr.set_title("Frecuencias Relativas de cada posible valor posible de la ruleta") 
        histograma_fr.set_xticks(eje_x)
        plt.show()

        
        plt.plot(tiradas,media1, color="Red" )
        plt.plot(tiradas,media2, color="blue")
        plt.plot(tiradas,media3, color="green")
        plt.plot(tiradas,media4, color="yellow")
        plt.plot(tiradas,media5, color="orange")
        plt.plot(tiradas,media_esperada)
        plt.title("Gráfica del Promedio de los valores de las tiradas")   # Establece el título del gráfico
        plt.xlabel("N° de tirada")   # Establece el título del eje x
        plt.ylabel("Promedio")      # Establece el título del eje y
        plt.legend()
        plt.show()

        nro_tirada_x = range(1, cant_tiradas)
        plt.plot(nro_tirada_x,varianza1, color="Red" )
        plt.plot(nro_tirada_x,varianza2, color="blue")
        plt.plot(nro_tirada_x,varianza3, color="green")
        plt.plot(nro_tirada_x,varianza4, color="yellow")
        plt.plot(nro_tirada_x,varianza5, color="orange")
        plt.plot(nro_tirada_x,varianza_esperada)
        plt.title("Gráfica de la Varianza de los valores de las tiradas")   # Establece el título del gráfico
        plt.xlabel("N° de tirada")   # Establece el título del eje x
        plt.ylabel("Varianza")      # Establece el título del eje y
        plt.legend()
        plt.show()

        plt.plot(nro_tirada_x,desvio1, color="Red" )
        plt.plot(nro_tirada_x,desvio2, color="blue")
        plt.plot(nro_tirada_x,desvio3, color="green")
        plt.plot(nro_tirada_x,desvio4, color="yellow")
        plt.plot(nro_tirada_x,desvio5, color="orange")
        plt.plot(nro_tirada_x,desvio_esperado)
        plt.title("Gráfica del Desvío de los valores de las tiradas")   # Establece el título del gráfico
        plt.xlabel("N° de tirada")   # Establece el título del eje x
        plt.ylabel("Desvío Estándar")       # Establece el título del eje y
        plt.legend()
        plt.show()
    else:
        print("Error, número introducido inválido.")
plt.show()
