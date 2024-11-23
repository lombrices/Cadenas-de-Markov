# Trabajo Cadenas de Markov

## Planteamiento de problema

Recientemente Mc Donalds realizo un  estudio sobre la preferencia de sus clientes en Chile, para poder saber en que producto invertir mas en el area de
marketing para tener mas ventas. El estudio se centró en sus 3 productos principales: 

- Hamburguesa **Big Mac**

- Helado **Mc Flurry**

- **Papas fritas** 

Los datos recopilados revelaron que la elección de los clientes en su próxima visita depende mayoritariamente de lo que eligieron en su visita anterior. A partir de esta información, se construyó la siguiente matriz de transición de probabilidades, que muestra las posibles elecciones de los clientes en su proxima visita. Al finalizar el estudio, se obtuvieron los siguientes resultados:
| Producto Actual   | Big Mac   | McFlurry | Papas Fritas |
|-------------------|-----------|----------|--------------|
| **Big Mac**       | 0.6       | 0.2      | 0.2          |
| **McFlurry**      | 0.3       | 0.5      | 0.2          |
| **Papas Fritas**  | 0.4       | 0.1      | 0.5          |

- Si un cliente eligió una Big Mac en su última visita, tiene un $60\%$ de probabilidad de volver a elegir Big Mac, un $20\%$ de elegir McFlurry, y un $20\%$ de elegir Papas Fritas.

- Si un cliente eligió un McFlurry, tiene un $30\%$ de probabilidad de elegir Big Mac, un $50\%$ de repetir McFlurry, y un $20\%$ de elegir Papas Fritas.

- Si un cliente eligió Papas Fritas, tiene un $40\%$ de probabilidad de cambiar a Big Mac, un $10\%$ de elegir McFlurry, y un $50\%$ de repetir Papas Fritas.
En base a esto calcular la probabilidad estacionaria de cada producto

## Ejecucion

El programa debe ser ejecutado como:
```bash
python3 main.py
```

## Requerimientos

- python3
    - Windows
        ```bash
        # Descargar el instalador desde la página oficial de Python:
        # https://www.python.org/downloads/
        # Durante la instalación, asegúrate de marcar la casilla "Add Python to PATH".
        ```
    - Debian
        ```bash
        sudo apt update
        sudo apt install -y python3
        ```
    - Arch
        ```bash
        sudo pacman -S python
        ```
    - Mac
        ```bash
        brew install python
        ```

- tkinter
    - Windows
        ```bash
        # Tkinter viene incluido en la instalación estándar de Python para Windows.
        # Asegúrate de haber instalado Python desde python.org.
        ```
    - Debian
        ```bash
        sudo apt update
        sudo apt install -y python3-tk
        ```
    - Arch
        ```bash
        sudo pacman -S tk
        ```
    - Mac
        ```bash
        brew install tcl-tk
        # Añade las rutas de tcl-tk al entorno si es necesario:
        export PATH="/usr/local/opt/tcl-tk/bin:$PATH"
        export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
        export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"
        ```

- numpy
    - Windows
        ```bash
        pip install numpy
        ```
    - Debian
        ```bash
        sudo apt update
        sudo apt install -y python3-numpy
        ```
    - Arch
        ```bash
        sudo pacman -S python-numpy
        ```
    - Mac
        ```bash
        pip install numpy
        ```