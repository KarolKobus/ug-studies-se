import tkinter as tk
from gui.question6 import Question6

def previous_window(root):
    """Cofa do poprzedniego pytania"""
    root.destroy()
    from gui.question4 import Question4  # Opóźniony import (rozwiązuje circular import)
    new_root = tk.Tk()
    app = Question4(new_root)
    new_root.mainloop()

class Question5:
    def __init__(self, root):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x700")

        # Tytuł sekcji
        tk.Label(root, text="Oceny poznawcze i funkcjonalne", font=("Arial", 16, "bold")).pack(pady=10)

        # Opis sekcji
        tk.Label(root, text="Uzupełnij na podstawie wywiadu psychologicznego.", font=("Arial", 12)).pack(pady=5)

        # Skale ocen
        self.scales = {
            "MMSE (0-30)": (0, 30),
            "Ocena funkcjonalna (0-10)": (0, 10),
            "Wynik ADL (skala Podstawowych Czynności Życia Codziennego, 0-10)": (0, 10)
        }

        self.values = {}

        for label, (min_val, max_val) in self.scales.items():
            tk.Label(root, text=label, font=("Arial", 14)).pack(pady=5)
            var = tk.IntVar(value=min_val)
            self.values[label] = var
            tk.Scale(root, from_=min_val, to=max_val, orient="horizontal", variable=var, font=("Arial", 12)).pack()

        # Pytania binarne
        self.binary_questions = {
            "Czy masz problemy z pamięcią?": "memory_complaints",
            "Czy występują problemy behawioralne?": "behavioral_problems"
        }

        self.binary_values = {}

        for question, var_name in self.binary_questions.items():
            tk.Label(root, text=question, font=("Arial", 14)).pack(pady=5)
            self.binary_values[var_name] = tk.IntVar()
            tk.Radiobutton(root, text="Nie", variable=self.binary_values[var_name], value=0, font=("Arial", 12)).pack()
            tk.Radiobutton(root, text="Tak", variable=self.binary_values[var_name], value=1, font=("Arial", 12)).pack()

        # Przycisk Wstecz i Dalej
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Wstecz", font=("Arial", 14), command=lambda: previous_window(self.root)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Dalej", font=("Arial", 14), command=self.next_question).pack(side="right", padx=10)

    def next_question(self):
        responses = {q: v.get() for q, v in self.values.items()}
        binary_responses = {q: v.get() for q, v in self.binary_values.items()}
        responses.update(binary_responses)
        print(responses)  # Można zapisać te wartości lub przekazać dalej
        self.root.destroy()
        # Otwórz kolejne pytanie
        root = tk.Tk()
        app = Question6(root)
        root.mainloop()