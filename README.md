# mandelbrot-fractal

## Arquivos
- `fractal.c`:  Código fonte em C responsável por gerar a imagem do fractal de Mandelbrot.
- `fractal.so`: Biblioteca dinâmica gerada pelo `fractal.c`.
- `interface.py`: Código fonte em Python responsável por chamar a chamar a biblioteca dinâmica e gerar a imagem do fractal de Mandelbrot, ele também mostra o fractal gerado.
- `interface.ui`: Arquivo de interface gerado pelo `PyQt`.
- `*.ppm`: Imagem gerada pelo `fractal.c`.

## Integração entre C e Python
O Objetivo desse repositório é integrar o código em C com o Python, para que possamos gerar o fractal de Mandelbrot. Para isso, utilizaremos a biblioteca [ctypes](https://docs.python.org/3/library/ctypes.html), que tem como objetivo permitir a chamada de funções em C a partir do Python.
## Como funciona
O arquivo `fractal.c` contém o código em C que gera o fractal de Mandelbrot. Esse código é compilado para gerar o arquivo `fractal.so`, que é utilizado pelo Python para gerar o fractal.

## Como executar
Para executar, navegue até a pasta UI o arquivo `interface.py` e execute o comando `python3 interface.py`.


## Bibliotecas utilizadas
- [ctypes](https://docs.python.org/3/library/ctypes.html)
- [pyqt5](https://pypi.org/project/PyQt5/)


