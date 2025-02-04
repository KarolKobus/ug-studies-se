import tkinter as tk
from gui.question4 import Question4


class Question3:
    def __init__(self, root):
        self.root = root
        self.root.title("Pytanie 3 - Historia medyczna")
        self.root.geometry("600x800")

        # Tytuł sekcji
        tk.Label(root, text="Historia medyczna", font=("Arial", 16, "bold")).pack(pady=10)

        # Lista pytań binarnych
        self.questions = {
            "Czy w rodzinie występowało Alzheimera?": "family_history",
            "Czy masz chorobę sercowo-naczyniową?": "cardiovascular_disease",
            "Czy masz cukrzycę?": "diabetes",
            "Czy masz depresję?": "depression",
            "Czy doznałeś urazu głowy?": "head_injury",
            "Czy masz nadciśnienie?": "hypertension"
        }

        self.answers = {}

        for question, var_name in self.questions.items():
            tk.Label(root, text=question, font=("Arial", 14)).pack(pady=5)
            self.answers[var_name] = tk.IntVar()
            tk.Radiobutton(root, text="Nie", variable=self.answers[var_name], value=0, font=("Arial", 12)).pack()
            tk.Radiobutton(root, text="Tak", variable=self.answers[var_name], value=1, font=("Arial", 12)).pack()

        # Przycisk Dalej
        tk.Button(root, text="Dalej", font=("Arial", 14), command=self.next_question).pack(pady=20)

    def next_question(self):
        responses = {q: v.get() for q, v in self.answers.items()}
        print(responses)  # Można zapisać te wartości lub przekazać dalej
        self.root.destroy()
        # Otwórz kolejne pytanie
        root = tk.Tk()
        app = Question4(root)
        root.mainloop()
