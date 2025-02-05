import tkinter as tk
from gui.question4 import Question4

def previous_window(root):
    """Cofa do poprzedniego pytania"""
    root.destroy()
    from gui.question2 import Question2  # Opóźniony import (rozwiązuje circular import)
    new_root = tk.Tk()
    app = Question2(new_root)
    new_root.mainloop()

class Question3:
    def __init__(self, root):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x800")

        # Tytuł sekcji
        tk.Label(root, text="Historia medyczna", font=("Arial", 16, "bold")).pack(pady=10)

        # Lista pytań binarnych
        self.questions = {
            "Czy w rodzinie występowała choroba Alzheimera?": "family_history",
            "Czy masz chorobę sercowo-naczyniową?": "cardiovascular_disease",
            "Czy masz cukrzycę?": "diabetes",
            "Czy masz depresję?": "depression",
            "Czy doznałeś kiedyś urazu głowy?": "head_injury",
            "Czy masz nadciśnienie?": "hypertension"
        }

        self.answers = {}

        for question, var_name in self.questions.items():
            tk.Label(root, text=question, font=("Arial", 14)).pack(pady=5)
            self.answers[var_name] = tk.IntVar()
            tk.Radiobutton(root, text="Nie", variable=self.answers[var_name], value=0, font=("Arial", 12)).pack()
            tk.Radiobutton(root, text="Tak", variable=self.answers[var_name], value=1, font=("Arial", 12)).pack()

        # Przycisk Wstecz i Dalej
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Wstecz", font=("Arial", 14), command=lambda: previous_window(self.root)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Dalej", font=("Arial", 14), command=self.next_question).pack(side="right", padx=10)

    def next_question(self):
        responses = {q: v.get() for q, v in self.answers.items()}
        print(responses)  # Można zapisać te wartości lub przekazać dalej
        self.root.destroy()
        # Otwórz kolejne pytanie
        root = tk.Tk()
        app = Question4(root)
        root.mainloop()
