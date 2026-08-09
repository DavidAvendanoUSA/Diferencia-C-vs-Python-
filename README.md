# DIFERENCIA C vs PYTHON
## EXPERIMENTO NUMÉRICO



# EXPERIMENTO


### De qué trata

**Objetivo**: Demostrar experimentalmente las diferencias de rendimiento entre C y Python al ejecutar operaciones repetitivas, comparando el tiempo de ejecución y el consumo de memoria; mediante el ordenamiento de un arreglo de 10,000 números aleatorios (valores entre 1 y 100)

- Este proyecto realiza un análisis comparativo de rendimiento entre C y Python implementando el algoritmo de ordenamiento **Bubble Sort**.

- Evalúa:
  - Tiempo de ejecución
  - Consumo de memoria
Y genera una comparación visual con una gráfica de barras.  


### Resultados

- Gráfica:
<img width="1344" height="646" alt="image" src="https://github.com/user-attachments/assets/74cbd442-9b21-4a66-8a38-b3e5494aec1c" />

- Memoria y tiempo:
<img width="729" height="473" alt="image" src="https://github.com/user-attachments/assets/5cbe677f-1fea-498b-b6de-883234f0f42f" />

Los resultados muestran una diferencia considerable entre ambas implementaciones. Para este experimento, C tardó aproximadamente 35 veces menos que Python y utilizó aproximadamente 7 veces menos memoria.
*nota: Estos valores corresponden a una ejecución específica y pueden variar dependiendo del equipo y de las condiciones de ejecución.*


## Conclusiones

1. El experimento permite observar una diferencia significativa de rendimiento entre C y Python al ejecutar el mismo algoritmo de Bubble Sort sobre un arreglo de 10.000 números.
2. C presentó un menor tiempo de ejecución, con 0.25 segundos frente a los 8.68 segundos obtenidos por Python. Esto representa una diferencia aproximada de 35 veces en este experimento.
3. En memoria sucedió lo mismo, C utilizó aproximadamente 1380 KB, mientras que Python utilizó 10004 KB.
4. Para este tipo de operaciones repetitivas e intensivas, C puede ofrecer un mejor rendimiento que Python, debido entre otras cosas a que C se compila directamente a código máquina, mientras que Python requiere un intérprete para ejecutar el código.
5. Finalmente, el experimento permitió comprobar de manera práctica que la elección del lenguaje de programación puede tener un impacto significativo en el tiempo de ejecución y el consumo de memoria de un programa.



# CÓDIGO


### Técnico

- Código en C: *experimento_c.c*
- Código en Python: *experimento_python.py*
- Recopila y ejecuta los datos: *ejecutar.sh*
- Grafica los resultados: *graficar.py*


### Configuración en Linux

Instalación de GCC y time:
```
sudo apt install gcc time
gcc --version
time --version
```

Para instalar los paquetes necesarios en Python, se recomienda generar un entorno virtual, pues muchas veces no se permite instalar paquetes de Python directamente en el Python del sistema.
```
sudo apt install python3 python3-pip python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install matplotlib pandas
python -m pip list
```


### Configuración en MAC

MAC no viene GNU incorporado, ni time, así que toca instalarlos:
```
brew install gnu-time
```

También GCC:
```
xcode-select --install
```

Y las librerías de Python:
```
python3 -m pip install matplotlib pandas
```

*nota: el script usa "time" pero en mac se llama "gtime", toca cambiarlo en el .sh*


### Ejecución

- Cambiar a la dirección donde se encuentran los archivos con *cd ruta*.
- Una vez activado el entorno .venv (al inicio de la línea debe aparecer (.venv), algo como: *(.venv) usuario@computador:~/proyecto$*)
<img width="738" height="480" alt="image" src="https://github.com/user-attachments/assets/7326f783-9d33-4dd6-8e95-dffb87ad0252" />

1. Otorgar el permiso (solo una vez):
```
chmod +x ejecutar.sh
```

2. Ejecutar:
```
./ejecutar.sh
```

3. Si por alguna razón, Linux no soporta abrir en una ventana emergente la gráfica (pues plt.show() intentó abrir una ventana gráfica y el backend actual de Matplotlib no puede mostrarla de esa manera), ejecuta el comando para visualizar los resultados de memoria y tiempo:
```
cat resultados.csv
```
En la carpeta donde se guardó el proyecto, ahora debe existir un archivo llamado *grafica.png* y haz click en él.

- Esto compila el código en C, ejecuta ambas versiones, mide tiempo y memoria, además genera la gráfica de los resultados.

Al final, se debe tener los siguientes archivos:
- Código en C: *experimento_c.c*
- Código en Python: *experimento_python.py*
- Recopila y ejecuta los datos: *ejecutar.sh*
- Grafica los resultados: *graficar.py*
- Resultados: *resultados.scv*
- Gráfica: *grafica.py*
<img width="659" height="529" alt="image" src="https://github.com/user-attachments/assets/a45b63b2-1b51-4357-ba0a-1330c0151d0c" />



#### Integrantes:
- David Avendaño
- Laura Niño
- Brayan Paredes
