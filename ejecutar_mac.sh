#!/bin/bash
rm -f grafica.png
rm -f resulyados.csv
echo "lenguaje,tiempo,memoria" > resulyados.csv
gtime -f "Python,%e,%M" python3 experimento_python.py 2>> resultados.csv 
gcc experimento_c.c -o experimento_comp
gtime -f "C,%e,%M" ./experimento_comp 2>> resultados.csv
rm -f experimento_comp 
python3 graficar.py
