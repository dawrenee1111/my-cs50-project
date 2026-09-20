# CS50P Final Project: Calculator
Hello, this is my final presentation for my final project on CS50P Introduction to Programming with Python. My name is Renee Lee and I live in Auckland, New Zealand. I am a thirteen year old learning python.
#### Video Demo:  <(https://www.youtube.com/watch?v=AipzmyfgeGA)>
#### Description:
This program performs as a calculator that asks for an expression to calculate infinitely until you ask it to exit. So basically it is a infinite calculator

#### Structure of the project / The different components that make up the project:
 1. `project.py`
 2. `README.md`
 3. `test_project.py`
 3. `requirements.txt`

#### `project.py`
Firstly, this is a program that will print out the instructions on how to use the calculator. Next, it will ask for an input of a 2-number arithmetic expression to calculate with spaces between each number and operator. Then it will print out a list of ascii fonts to choose from and ask for your input of ascii fonts. And after that, this program will print out the answer of the inputted expression in the inputted ASCII font as well as in normal text so it is easier to read.

I used the `regular expression` module to validate the input of the expression to calculate. The validation I made was to be any integer with one decimal digit. It can calculate addition expressions, and it can calculate subtraction expressions, and it can calculate multiplication expressions and it can also calculate division expressions. I also used the `sys` module to exit the program in the case of `ValueERROR` when the user inputs a font that is not on the list that has been printed or an expression that does not fit the criteria of the regular expression. Additionally, I used the `sys` module to exit the program when the user wants it to. What is even more, I used the `pyfiglet` module to print out the answer in an ASCII font that is in the list printed which the user inputted.

#### `README.md`
This mark down file is this file that you are currently reading right now. `README.md` says the project's purpose and how or what it performs. `README.md` says the different components or files that make up the project like `project.py`, `test_project.py`, `requirements.txt`, and `README.md`. More over, `README.md` describes the program in `project.py` in detail saying how it was made and what libraries were used and what its functions are. `README.md` also describes what the test program `test_project.py` tests. And finally, it also has a file called `requirements.txt` that tells what libraries were used in the program.

#### `test_project.py`
This program tests the four different funtions in the `project.py` program, it tests the four different functions in the `project.py` program if they work, or if they are vaild. The four different functions that it tests is the addition funtion, and the multiplication function, and the subraction function, and lastly the division function.

#### `requirements.txt`
This text file tells what libraries I have used in my `project.py` program. I used the regular expression library, the pyfiglet library, and I used the sys module.

#### Thank you
This marks the end of this project, thank you for reading this even though this program is probably going to be checked by the computer, not a real human. Bye bye.
