#!/bin/bash
rm grafica.png
rm resultados.csv
echo "Lenguaje,Tiempo,Memoria" > resultados.csv

/usr/bin/time -f "Python,%e,%M" python3 experimento_python.py 2>>resultados.csv

gcc experimento_c.c -o experimento_comp
/usr/bin/time -f "C,%e,%M" ./experimento_comp 2>>resultados.csv
rm experimento_comp

python3 graficar.py
