from tkinter import Tk, StringVar, Listbox, END
from tkinter import ttk
from random import randint, choice
import winsound

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Number Guessing Game")
        self.master.geometry("440x420")
        self.master.configure(bg="#eaf6fb")
        self.number_to_guess = randint(1, 100)
        self.attempts = 0
        self.previous_guesses = []
        self.facts = [
            "Did you know? The number 73 is the 21st prime number!",
            "Fun fact: 100 is a square number (10x10)!",
            "Keep going! Every guess is a step closer.",
            "Motivation: Even the best guessers started as beginners!",
            "Tip: Try to use the feedback to narrow your range!"
        ]

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#eaf6fb", font=("Helvetica", 14))
        style.configure('Title.TLabel', font=("Helvetica", 22, "bold"), foreground="#2d6cdf", background="#eaf6fb")
        style.configure('TButton', font=("Helvetica", 14), padding=6)
        style.configure('TEntry', font=("Helvetica", 14))
        style.configure('Fact.TLabel', font=("Helvetica", 11, "italic"), foreground="#888", background="#eaf6fb")

        title_label = ttk.Label(master, text="🎯 Number Guessing Game", style='Title.TLabel')
        title_label.pack(pady=(18, 8))

        input_frame = ttk.Frame(master, style='TFrame')
        input_frame.pack(pady=(5, 0))

        instruction_label = ttk.Label(input_frame, text="Enter your guess:", font=("Helvetica", 14), background="#eaf6fb")
        instruction_label.grid(row=0, column=0, columnspan=2, pady=(0, 5))

        self.guess_var = StringVar()
        self.guess_entry = ttk.Entry(input_frame, textvariable=self.guess_var, width=18)
        self.guess_entry.grid(row=1, column=0, padx=(0, 10), pady=5)
        self.guess_entry.bind("<Return>", self.submit_guess)
        self.guess_entry.bind("<Key>", self.clear_feedback)

        self.submit_button = ttk.Button(input_frame, text="Submit", command=self.submit_guess)
        self.submit_button.grid(row=1, column=1, pady=5)

        self.restart_button = ttk.Button(input_frame, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        self.feedback_label = ttk.Label(master, text="", font=("Helvetica", 13, "italic"), foreground="#e74c3c", background="#eaf6fb")
        self.feedback_label.pack(pady=(16, 6))

        self.attempts_label = ttk.Label(master, text="Attempts: 0", font=("Helvetica", 12), background="#eaf6fb", foreground="#888")
        self.attempts_label.pack(pady=(0, 2))

        # Previous guesses section (horizontal)
        prev_frame = ttk.Frame(master, style='TFrame')
        prev_frame.pack(pady=(8, 0))
        prev_label = ttk.Label(prev_frame, text="Previous guesses:", font=("Helvetica", 12, "bold"), background="#eaf6fb")
        prev_label.pack(anchor='w')
        self.guess_canvas = ttk.Frame(prev_frame, style='TFrame')
        self.guess_canvas.pack(pady=(2, 0), fill='x')

        # Fun fact/motivation label
        self.fact_label = ttk.Label(master, text="", style='Fact.TLabel', wraplength=380, justify='center')
        self.fact_label.pack(pady=(10, 0))

    def submit_guess(self, event=None):
        try:
            guess = int(self.guess_var.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")
            self.previous_guesses.append(guess)
            # Add guess as a horizontal label
            guess_label = ttk.Label(self.guess_canvas, text=str(guess), font=("Consolas", 12, "bold"), background="#d1eaff", foreground="#2d6cdf", borderwidth=2, relief='groove', padding=4)
            guess_label.pack(side='left', padx=4, pady=2)
            if guess < self.number_to_guess:
                self.feedback_label.config(text="Your guess is too low!", foreground="#e67e22")
                winsound.MessageBeep(winsound.MB_ICONHAND)
            elif guess > self.number_to_guess:
                self.feedback_label.config(text="Your guess is too high!", foreground="#e67e22")
                winsound.MessageBeep(winsound.MB_ICONHAND)
            else:
                self.feedback_label.config(text=f"🎉 Congratulations! You guessed it in {self.attempts} attempts.", foreground="#27ae60")
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
            self.fact_label.config(text=choice(self.facts))
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", foreground="#e74c3c")
            self.fact_label.config(text="")
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        self.guess_var.set("")
        self.guess_entry.focus()

    def clear_feedback(self, event=None):
        self.feedback_label.config(text="")

    def restart_game(self):
        self.number_to_guess = randint(1, 100)
        self.attempts = 0
        self.previous_guesses.clear()
        for widget in self.guess_canvas.winfo_children():
            widget.destroy()
        self.feedback_label.config(text="", foreground="#e74c3c")
        self.attempts_label.config(text="Attempts: 0")
        self.fact_label.config(text="New game started! Good luck!")
        self.guess_var.set("")
        self.guess_entry.focus()

if __name__ == "__main__":
    root = Tk()
    game = NumberGuessingGame(root)
    root.mainloop()