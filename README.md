# Dice Simulator 3000 – Python 

The **Dice Simulator 3000** is an interactive Python program that simulates rolling a six-sided die multiple times.  
It calculates the **empirical mean** of all rolls and compares it to the **theoretical mean** of 3.5.  
The user can choose how many times the die should be rolled and repeat the simulation as often as desired.

---

## Features

- Simulates any number of dice rolls using `randint(1, 6)`
- Computes the **empirical average** of all rolls
- Displays the **theoretical mean** for comparison
- Input validation for integer values
- Repeatable simulation loop
- Clean, simple console interaction

---

## Program Logic

The program consists of:

- A helper function `ist_int()` to validate whether user input is an integer  
- A function `wuerfeln(n)` that:
  - rolls the die `n` times  
  - stores results in a list  
  - calculates and prints the empirical mean  
- A main loop that:
  - asks the user how many rolls to simulate  
  - validates the input  
  - calls the simulation function  
  - allows repeated runs  


