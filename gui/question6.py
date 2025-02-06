import tkinter as tk
from gui.result import ResultWindow

def previous_window(root, responses):
    """Cofa do poprzedniego pytania"""
    root.destroy()
    from gui.question5 import Question5  # Opóźniony import (rozwiązuje circular import)
    new_root = tk.Tk()
    app = Question5(new_root, responses)
    new_root.mainloop()

class Question6:
    def __init__(self, root, responses):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x700")
        self.responses = responses  # Przechowywanie odpowiedzi z poprzedniego pytania

        # Tytuł sekcji
        tk.Label(root, text="Objawy", font=("Arial", 16, "bold")).pack(pady=10)

        # Pytania binarne dotyczące objawów
        self.symptoms = {
            "Czy występuje stan zmieszania/zagubienia?": "Confusion",
            "Czy występuje dezorientacja?": "Disorientation",
            "Czy występują zmiany osobowości?": "PersonalityChanges",
            "Czy masz trudności z wykonywaniem zadań?": "DifficultyCompletingTasks",
            "Czy masz problemy z zapominaniem?": "Forgetfulness"
        }

        self.answers = {}

        for question, var_name in self.symptoms.items():
            tk.Label(root, text=question, font=("Arial", 14)).pack(pady=5)
            self.answers[var_name] = tk.IntVar()
            tk.Radiobutton(root, text="Nie", variable=self.answers[var_name], value=0, font=("Arial", 12)).pack()
            tk.Radiobutton(root, text="Tak", variable=self.answers[var_name], value=1, font=("Arial", 12)).pack()

        # Przycisk Wstecz i Zakończ
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Wstecz", font=("Arial", 14), command=lambda: previous_window(self.root, self.responses)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Zakończ", font=("Arial", 14), command=self.finish_survey).pack(side="right", padx=10)

    def finish_survey(self):
        for q, v in self.answers.items():
            self.responses[q] = v.get()

        self.root.destroy()
        # Otwórz okno z wynikami
        root = tk.Tk()
        app = ResultWindow(root, self.responses)
        root.mainloop()
