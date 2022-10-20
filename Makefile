SHELL := /bin/bash

assemble:
# Install dependencies
	sudo apt update
	sudo apt install python3
	sudo apt install python3-pip -y
	sudo pip3 install virtualenv
	sudo apt -y install gcc

# Install Python dependencies
	virtualenv -p python3 venv
	source venv/bin/activate
	pip install -r requirements.txt
	
# compiling C library
	gcc -o fractal/fractal.o fractal/fractal.c -lm
	gcc -shared -o fractal/fractal.so -fPIC fractal/fractal.c
	
# compiling python with C and running
	pyinstaller --onefile --add-data 'fractal/fractal.so:.' UI/interface.py
	./dist/interface
	echo "Up and running!"

compileC:
	gcc -o fractal/fractal.o fractal/fractal.c -lm
	gcc -shared -o fractal/fractal.so -fPIC fractal/fractal.c

compileUI:
	pyinstaller --onefile --add-data 'fractal/fractal.so:.' UI/interface.py
	./dist/interface
	echo "Up and running!"

run:
	./dist/interface