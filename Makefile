installDependencies:
	sudo apt update
	sudo apt install python3
	sudo apt install python3-pip
	sudo pip3 install virtualenv
	sudo apt -y install gcc

installPythonDependencies:
	virtualenv -p python3 venv
	source venv/bin/activate
	pip install -r requirements.txt

compileFractal: 
	fractal.c
	gcc -o fractal fractal.c -lm

generateFractal:
	gcc -shared -o fractal.so -fPIC fractal.c

generateExecutableLinux:
	gcc -o fractal fractal.c -lm
	gcc -shared -o fractal.so -fPIC fractal.c
	pyinstaller --onefile --add-data 'fractal.so:.' fractal.py

run:
	python3 UI/interface.py