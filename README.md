# Grade Calculator

Welcome to the Grade Calculator!

This is a simple Python grade calculator that runs in the terminal.

## What it does

The program asks the user to enter their scores. It then determines the average, highest score, lowest score, and letter grade. It also checks if the user enters something that is not a valid score.

## How to run it

1. Open the terminal.
2. Go to the project folder.
3. Run:

python main.py

## What I would add with another week

I would add the ability to save the grades and add grades for multiple students.



\## Refactoring



I changed the grade calculator by moving the main functions into a GradeCalculator class. The class keeps the grade calculator functions together and makes the program more organized. The first version had separate functions and more of the program logic outside of them. Using a class makes it easier to keep the grade calculator's functions together and reuse them. One thing that became harder was having to use self when calling the functions inside the class.

