# mandelbrot-fractal

## Arquivos
- `fractal.c`:  Código fonte em C responsável por gerar a imagem do fractal de Mandelbrot.
- `fractal.so`: Biblioteca dinâmica gerada pelo `fractal.c`.
- `interface.py`: Código fonte em Python responsável por chamar a chamar a biblioteca dinâmica e gerar a imagem do fractal de Mandelbrot, ele também mostra o fractal gerado.
- `interface.ui`: Arquivo de interface gerado pelo `PyQt`.
- `*.ppm`: Imagem gerada pelo `fractal.c`.

## Integração entre C e Python
O Objetivo desse repositório é integrar o código em C com o Python, para que possamos gerar o fractal de Mandelbrot. Para isso, utilizaremos a biblioteca [ctypes](https://docs.python.org/3/library/ctypes.html), que tem como objetivo permitir a chamada de funções em C a partir do Python.

## Como compilar o código em C
Caso você não possua o comando `cc` instalado, você pode instalar o compilador `gcc` com o seguinte comando:
- Linux: 
```bash
sudo apt install gcc
```
- Windows: [Download](https://sourceforge.net/projects/mingw-w64/files/latest/download)
- Mac:
```bash
brew install gcc
```

Após a instalação do compilador, você pode compilar o código em C com o seguinte comando:
- `cc -fPIC -shared -o fractal.so fractal.c`
  
Isso irá gerar a biblioteca dinâmica `fractal.so`, que será utilizada pelo código em Python.

## Como executar o código em Python
Para executar o código em Python, você deve ter o Python 3 instalado em sua máquina. Caso você não possua o Python 3 instalado, você pode instalar com o seguinte comando:
- Linux:
```bash
sudo apt install python3
```
- Windows: [Download](https://www.python.org/downloads/windows/)
- Mac:
```bash
brew install python3
```

Após a instalação do Python 3, você pode executar o código em Python com o seguinte comando:
- `python3 interface.py`



## Bibliotecas utilizadas
- [ctypes](https://docs.python.org/3/library/ctypes.html)
- [pyqt5](https://pypi.org/project/PyQt5/)


