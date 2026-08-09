# DIFERENCIA C vs PYTHON
## EXPERIMENTO NUMÉRICO

:)

Solo falta lo de explicar bubbel sort que es GNU time y porque la diferencia de como se ejecuta GNU time en linux y mac y ya :)
## Contenido

- experimento_c.c -> codigo en C
- experimento_python.py -> codigo en Python
- ejecutar.sh -> compila y corre todo y saca los datos
- graficar.py -> hace la grafica con los resultados

## Instalar (linux)
```
sudo apt install gcc time
python3 -m pip install matplotlib pandas
```
## Instalar (mac)
En mac no viene GNU time entonces toca instalarlo:
```
brew install gnu-time
```
tambien gcc:
```
xcode-select --install
```
y las librerias de python:
```
python3 -m pip install matplotlib pandas
```
## Como correr
primero darle permiso (solo una vez):

en linux:
```
chmod +x ejecutar_linux.sh
```
en mac:
```
chmod +x ejecutar_mac.sh
```
y ya, correrlo:

en linux:
```
./ejecutar_linux.sh
```
en mac:
```
./ejecutar_mac.sh
```
eso compila el C, corre las dos versiones, mide tiempo/memoria y saca la grafica.
