# mandelbrot-fractal

## Arquivos
- `fractal.c`:  Código fonte em C responsável por gerar a imagem do fractal de Mandelbrot.
- `fractal.so`: Biblioteca dinâmica gerada pelo `fractal.c`.
- `interface.py`: Código fonte em Python responsável por chamar a chamar a biblioteca dinâmica e gerar a imagem do fractal de Mandelbrot, ele também mostra o fractal gerado.
- `interface.ui`: Arquivo de interface gerado pelo `PyQt` que é compilado com o `PyUIC` para gerar o `interface.py`.
- `*.ppm`: Imagem gerada pelo `fractal.c`.

## Integração entre C e Python
O Objetivo desse repositório é integrar o código em C que é responsável por gerar o fractal de Mandelbrot, com o  um código em Python que tem a função de chamar o código em C e mostrar o fractal gerado. Para isso, utilizaremos a biblioteca [ctypes](https://docs.python.org/3/library/ctypes.html) que tem como objetivo permitir a chamada de funções em C a partir do Python.


## Como rodar o projeto
Ao rodar o projeto pela primeira vez, certifique-se de ter o comando `make` instalado em sua máquina.
Após certificar-se de ter o `make` instalado, exedcute o comando `make assemble`, este comando é necessário apenas na primeira execução do projeto, pois ele irá baixar as dependências do projeto assim como compilar o código em C e Python e por fim rodar a interface. 
Existe também outros 3 comandos que podem ser executados:
- `make compileC`: Compila o código em C e gera o `.so` utilizado pelo python. 
- `make compileUI`: Compila o arquivo `.ui` gerado pelo `PyQt` para gerar o arquivo `.py` que é utilizado pelo python e roda o executável.
- `make run`: Roda o executável gerado pelo `PyQt`.




## Bibliotecas utilizadas
- [ctypes](https://docs.python.org/3/library/ctypes.html)
- [pyqt5](https://pypi.org/project/PyQt5/)


