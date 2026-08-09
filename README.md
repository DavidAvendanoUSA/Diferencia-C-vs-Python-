# DIFERENCIA C vs PYTHON
## EXPERIMENTO NUMÉRICO

:)
## Contenido

- experimento_c.c -> codigo en C
- experimento_python.py -> lo mismo pero en python
- ejecutar.sh -> compila y corre todo, saca los tiempos
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

nota: el script usa "time" pero en mac se llama "gtime", toca cambiarlo en el .sh

## Como correr

primero darle permiso (solo una vez):

```
chmod +x ejecutar.sh
```

y ya, correrlo:

```
./ejecutar.sh
```

eso compila el C, corre las dos versiones, mide tiempo/memoria y saca la grafica.
