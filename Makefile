SHELL := /bin/bash

Assemble:
	sudo apt update
	sudo apt install python3
	sudo apt install python3-pip -y
	sudo pip3 install virtualenv -y
	sudo apt -y install gcc

	virtualenv -p python3 venv
	source venv/bin/activate
	pip install -r requirements.txt

	gcc -o fractal/fractal fractal/fractal.c -lm

	gcc -shared -o fractal/fractal.so -fPIC fractal/fractal.c

	gcc -o fractal/fractal.o fractal/fractal.c -lm
	gcc -shared -o fractal/fractal.so -fPIC fractal/fractal.c
	pyinstaller --onefile --add-data 'fractal/fractal.so:.' UI/interface.py

	./dist/interface

	echo "Up and running!"