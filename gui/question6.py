import tkinter as tk

def previous_window(root):
    """Cofa do poprzedniego pytania"""
    root.destroy()
    from gui.question5 import Question5  # Opóźniony import (rozwiązuje circular import)
    new_root = tk.Tk()
    app = Question5(new_root)
    new_root.mainloop()

class Question6:
    def __init__(self, root):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x700")

        # Tytuł sekcji
        tk.Label(root, text="Objawy", font=("Arial", 16, "bold")).pack(pady=10)

        # Pytania binarne dotyczące objawów
        self.symptoms = {
            "Czy występuje stan zmieszania/zagubienia?": "confusion",
            "Czy występuje dezorientacja?": "disorientation",
            "Czy występują zmiany osobowości?": "personality_changes",
            "Czy masz trudności z wykonywaniem zadań?": "difficulty_completing_tasks",
            "Czy masz problemy z zapominaniem?": "forgetfulness"
        }

        self.answers = {}

        for question, var_name in self.symptoms.items():
            tk.Label(root, text=question, font=("Arial", 14)).pack(pady=5)
            self.answers[var_name] = tk.IntVar()
            tk.Radiobutton(root, text="Nie", variable=self.answers[var_name], value=0, font=("Arial", 12)).pack()
            tk.Radiobutton(root, text="Tak", variable=self.answers[var_name], value=1, font=("Arial", 12)).pack()

        # Przycisk Wstecz i Dalej
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Wstecz", font=("Arial", 14), command=lambda: previous_window(self.root)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Zakończ", font=("Arial", 14), command=self.next_question).pack(side="right", padx=10)

    def next_question(self):
        responses = {q: v.get() for q, v in self.answers.items()}
        print(responses)  # Można zapisać te wartości lub przekazać dalej
        self.root.destroy()
        # Tutaj można zaimportować i otworzyć kolejne okno np. Question7
