import pandas as pd 
import matplotlib.pyplot as plt 
datos_resultados = pd.read_csv("resultados.csv")
plt.figure(figsize = (10,6))
plt.subplot(1,2,1)
plt.bar(datos_resultados["lenguaje"],datos_resultados["tiempo"],color="blue", alpha=0.8)
plt.xlabel("Lenguaje")
plt.ylabel("Tiempo (S)")
plt.title("Comparativa tiempo de ejecucion")

plt.subplot(1,2,2)
plt.bar(datos_resultados["lenguaje"],datos_resultados["memoria"],color="red",alpha=0.8)
plt.xlabel("lenguaje")
plt.ylabel("Memoria (KB)")
plt.title("Comparativa memoria maxima utilizada")
plt.savefig("grafica.png")
plt.show()
