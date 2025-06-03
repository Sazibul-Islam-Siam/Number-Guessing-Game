from tkinter import Tk, StringVar
from tkinter import ttk
from random import randint

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f4f8")
        self.number_to_guess = randint(1, 100)
        self.attempts = 0

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#f0f4f8", font=("Helvetica", 14))
        style.configure('Title.TLabel', font=("Helvetica", 20, "bold"), foreground="#2d6cdf", background="#f0f4f8")
        style.configure('TButton', font=("Helvetica", 14), padding=6)
        style.configure('TEntry', font=("Helvetica", 14))

        title_label = ttk.Label(master, text="🎯 Number Guessing Game", style='Title.TLabel')
        title_label.pack(pady=(20, 10))

        instruction_label = ttk.Label(master, text="Enter your guess:", font=("Helvetica", 14), background="#f0f4f8")
        instruction_label.pack(pady=(5, 0))

        self.guess_var = StringVar()
        self.feedback_label = ttk.Label(master, text="", foreground="#e74c3c")
        self.feedback_label.pack(pady=10)

        self.guess_entry = ttk.Entry(master, textvariable=self.guess_var, width=20)
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", self.submit_guess)
        self.guess_entry.bind("<Key>", self.clear_feedback)  # Clear feedback on typing

        self.submit_button = ttk.Button(master, text="Submit", command=self.submit_guess)
        self.submit_button.pack(pady=10)

    def submit_guess(self, event=None):
        try:
            guess = int(self.guess_var.get())
            self.attempts += 1
            if guess < self.number_to_guess:
                self.feedback_label.config(text="Your guess is too low!", foreground="#e67e22")
            elif guess > self.number_to_guess:
                self.feedback_label.config(text="Your guess is too high!", foreground="#e67e22")
            else:
                self.feedback_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.", foreground="#27ae60")
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", foreground="#e74c3c")
        
        self.guess_var.set("")  # Clear the input field
        self.guess_entry.focus()  # Focus back on the input field

    def clear_feedback(self, event=None):
        self.feedback_label.config(text="")

if __name__ == "__main__":
    root = Tk()
    game = NumberGuessingGame(root)
    root.mainloop()