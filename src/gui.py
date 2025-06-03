from tkinter import Tk, Label, Entry, Button, StringVar
from random import randint

class NumberGuessingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        
        self.number_to_guess = randint(1, 100)
        self.attempts = 0
        
        self.guess_var = StringVar()
        
        self.label = Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=20)
        
        self.entry = Entry(master, textvariable=self.guess_var)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_guess)
        self.entry.bind("<FocusIn>", self.clear_output)
        
        self.result_label = Label(master, text="", fg="blue")
        self.result_label.pack(pady=20)
        
        self.reset_button = Button(master, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def check_guess(self, event):
        try:
            guess = int(self.guess_var.get())
            self.attempts += 1
            
            if guess < self.number_to_guess:
                self.result_label.config(text="Your guess is too low!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Your guess is too high!")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def clear_output(self, event):
        self.result_label.config(text="")
        self.guess_var.set("")

    def reset_game(self):
        self.number_to_guess = randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.guess_var.set("")