'''
	Name: James Jacob Shaver
	Email: jjshaver@go.olemiss.edu
	Program Source File Name: README.md
	Last Edit Date: 11 November 2020
	Course Information: CSci 487
	Program Description: This is a readme file on how to use my NeuralNetwork
	Sources Consulted:
	Honor Code Statement: In keeping with the honor code policies of the
	University of Mississippi, the School of Engineering, and the Department of
	Computer and Information Science, I affirm that I have neither given nor
	received assistance on this programming assignment. This assignment
	represents my individual, original effort.
		...My Signature is on File.

			'Was wir für uns selbst tun, stirbt mit uns.
	Was wir für andere und die Welt tun, bleibt und ist unsterblich.'
'''
# club_durian
This is my Senior Project

Using a Windows Machine:
	To Download Python:
		Open a webbrowser and go to https://www.python.org/downloads/windows/
			Select the newest  stable release version and click Download
			Scroll to bottom of page and select 'Windows x86-64 executable installer'
	
		Run the .exe and checkmark Add python 3.9 to PATH
			Click Install Now and Yes to Allow Changes

	Once finished, open command prompt by pressing the windows key and typing cmd + enter
		With command prompt open type: 

				python --version 

			to verify that the installation has the correct PATH. 
		If the PATH is not correct follow guide: 

			https://geek-university.com/python/add-python-to-the-windows-path/

		Still in command prompt go to python program files using 

			cd \directory path\ 

		where directory path is the location of the python files

	To execute the Neural Network type: python NeuralNetwork.py 
		When prompted, select a file you would like to test against the Neural Network by typing the name. *this is not case sensative 

	If there is a desire to add more 3d objects to test against the Neural Network run: python thingiVerseScrape.py

	If there is ever a need to train the Neural Network further use: python PyTorch.py


Using Mac:
	Installing Python With Homebrew:

		Open Terminal and run:
			$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

		The script will explain what changes it will make and prompt you before the installation begins. Once you’ve installed Homebrew, insert the Homebrew directory at the top of your PATH environment variable. You can do this by adding the following line at the bottom of your ~/.profile file

			export PATH="/usr/local/opt/python/libexec/bin:$PATH"

		If you have OS X 10.12 (Sierra) or older use this line instead

			export PATH=/usr/local/bin:/usr/local/sbin:$PATH

		Now, we can install Python 3:

			$ brew install python

		This will take a minute or two.

		Verify python instillation:

			$ python --version

		Still in terminal go to python program files using cd \directory path\ where directory path is the location of the python files

	To execute the Neural Network type: 

			$ python NeuralNetwork.py 

		When prompted, select a file you would like to test against the Neural Network by typing the name. *this is not case sensative 

	If there is a desire to add more 3d objects to test against the Neural Network run: 

		$ python thingiVerseScrape.py

	If there is ever a need to train the Neural Network further use:
		$ python PyTorch.py

Using Linux:
	
	You're probably a professional programmer. If not don't worry. Linux comes with python pre installed 9 times out of ten. 

	Follow the guide post installation for Mac and you should do fine. 
