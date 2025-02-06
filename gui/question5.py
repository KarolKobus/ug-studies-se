import tkinter as tk
from gui.question6 import Question6

def previous_window(root, responses):
    """Cofa do poprzedniego pytania"""
    root.destroy()
    from gui.question4 import Question4  # Opóźniony import (rozwiązuje circular import)
    new_root = tk.Tk()
    app = Question4(new_root, responses)
    new_root.mainloop()

class Question5:
    def __init__(self, root, responses):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x700")
        self.responses = responses  # Przechowywanie odpowiedzi z poprzedniego pytania

        # Tytuł sekcji
        tk.Label(root, text="Oceny poznawcze i funkcjonalne", font=("Arial", 16, "bold")).pack(pady=10)

        # Opis sekcji
        tk.Label(root, text="Uzupełnij na podstawie wywiadu psychologicznego.", font=("Arial", 12)).pack(pady=5)

        # Skale ocen
        self.scales = {
            "MMSE": ("Proszę podać wynik MMSE (0-30)", 0, 30),
            "FunctionalAssessment": ("Proszę podać ocenę funkcjonalną (0-10)", 0, 10),
            "ADL": ("Proszę podać wynik ADL - codzienne funkcjonowanie (0-10)", 0, 10)
        }

        self.values = {}

        for key, (label_text, min_val, max_val) in self.scales.items():
            tk.Label(root, text=label_text, font=("Arial", 14)).pack(pady=5)
            var = tk.IntVar(value=min_val)
            self.values[key] = var
            tk.Scale(root, from_=min_val, to=max_val, orient="horizontal", variable=var, font=("Arial", 12)).pack()

        # Pytania binarne
        self.binary_questions = {
            "MemoryComplaints": "Czy masz problemy z pamięcią?",
            "BehavioralProblems": "Czy występują problemy behawioralne?"
        }

        self.binary_values = {}

        for key, label_text in self.binary_questions.items():
            tk.Label(root, text=label_text, font=("Arial", 14)).pack(pady=5)
            self.binary_values[key] = tk.IntVar()
            tk.Radiobutton(root, text="Nie", variable=self.binary_values[key], value=0, font=("Arial", 12)).pack()
            tk.Radiobutton(root, text="Tak", variable=self.binary_values[key], value=1, font=("Arial", 12)).pack()

        # Przycisk Wstecz i Dalej
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Wstecz", font=("Arial", 14),
                  command=lambda: previous_window(self.root, self.responses)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Dalej", font=("Arial", 14), command=self.next_question).pack(side="right",
                                                                                                   padx=10)

    def next_question(self):
        for q, v in self.values.items():
            self.responses[q] = v.get()
        for q, v in self.binary_values.items():
            self.responses[q] = v.get()

        self.root.destroy()
        # Otwórz kolejne pytanie
        root = tk.Tk()
        app = Question6(root, self.responses)
        root.mainloop()
