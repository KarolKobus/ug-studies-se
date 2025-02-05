import tkinter as tk
from gui.question5 import Question5

def previous_window(root):
    """Cofa do poprzedniego pytania"""
    root.destroy()
    from gui.question3 import Question3  # Opóźniony import (rozwiązuje circular import)
    new_root = tk.Tk()
    app = Question3(new_root)
    new_root.mainloop()

class Question4:
    def __init__(self, root):
        self.root = root
        self.root.title("Alzheimer Predictor")
        self.root.geometry("600x750")

        # Tytuł sekcji
        tk.Label(root, text="Pomiary kliniczne", font=("Arial", 16, "bold")).pack(pady=10)

        # Opis sekcji
        tk.Label(root, text="Uzupełnij najświeższe wyniki badań oraz pomiarów.", font=("Arial", 12)).pack(pady=5)

        # Pomiary kliniczne z suwakami
        self.measurements = {
            "Ciśnienie skurczowe (mmHg)": (90, 180),
            "Ciśnienie rozkurczowe (mmHg)": (60, 120),
            "Cholesterol całkowity (mg/dL)": (150, 300),
            "Cholesterol LDL (mg/dL)": (50, 200),
            "Cholesterol HDL (mg/dL)": (20, 100),
            "Trójglicerydy (mg/dL)": (50, 400)
        }

        self.values = {}

        for label, (min_val, max_val) in self.measurements.items():
            tk.Label(root, text=label, font=("Arial", 14)).pack(pady=5)
            var = tk.IntVar(value=min_val)
            self.values[label] = var
            tk.Scale(root, from_=min_val, to=max_val, orient="horizontal", variable=var, font=("Arial", 12)).pack()

        # Przycisk Wstecz i Dalej
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Wstecz", font=("Arial", 14), command=lambda: previous_window(self.root)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Dalej", font=("Arial", 14), command=self.next_question).pack(side="right", padx=10)

    def next_question(self):
        responses = {q: v.get() for q, v in self.values.items()}
        print(responses)  # Można zapisać te wartości lub przekazać dalej
        self.root.destroy()
        # Otwórz kolejne pytanie
        root = tk.Tk()
        app = Question5(root)
        root.mainloop()
