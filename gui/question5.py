import tkinter as tk
from gui.question6 import Question6


class Question5:
    def __init__(self, root):
        self.root = root
        self.root.title("Pytanie 5 - Oceny poznawcze i funkcjonalne")
        self.root.geometry("600x800")

        # Tytuł sekcji
        tk.Label(root, text="Oceny poznawcze i funkcjonalne", font=("Arial", 16, "bold")).pack(pady=10)

        # Skale ocen
        self.scales = {
            "MMSE (0-30)": (0, 30),
            "Ocena funkcjonalna (0-10)": (0, 10),
            "ADL - codzienne funkcjonowanie (0-10)": (0, 10)
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

        # Przycisk Dalej
        tk.Button(root, text="Dalej", font=("Arial", 14), command=self.next_question).pack(pady=20)

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