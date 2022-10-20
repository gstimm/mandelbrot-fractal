# mandelbrot-fractal

## Integração entre C e Pytho
O Objetivo desse repositório é integrar o código em C com o Python, para que possamos gerar o fractal de Mandelbrot. Para isso, utilizaremos a biblioteca [ctypes](https://docs.python.org/3/library/ctypes.html), que tem como objetivo permitir a chamada de funções em C a partir do Python.
## Como funciona
O arquivo `fractal.c` contém o código em C que gera o fractal de Mandelbrot. Esse código é compilado para gerar o arquivo `fractal.so`, que é utilizado pelo Python para gerar o fractal.

## Como executar
Para executar o código, basta executar o arquivo `interface.py` com o Python 3.6 ou superior.
Ao executar, uma janela será aberta com um botão para gerar o fractal e um input para definir o nome do arquivo gerado, porém não é necessário preencher o nome do arquivo, pois o padrão é `pic.ppm`.
Para executar, navegue até a pasta UI o arquivo `interface.py` e execute o comando `python3 interface.py`.

## Bibliotecas utilizadas
- [ctypes](https://docs.python.org/3/library/ctypes.html)
- [pyqt5](https://pypi.org/project/PyQt5/)


