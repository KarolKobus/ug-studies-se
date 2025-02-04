import tkinter as tk
from gui.question5 import Question5


class Question4:
    def __init__(self, root):
        self.root = root
        self.root.title("Pytanie 4 - Pomiary kliniczne")
        self.root.geometry("600x800")

        # Tytuł sekcji
        tk.Label(root, text="Pomiary kliniczne", font=("Arial", 16, "bold")).pack(pady=10)

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

        # Przycisk Dalej
        tk.Button(root, text="Dalej", font=("Arial", 14), command=self.next_question).pack(pady=20)

    def next_question(self):
        responses = {q: v.get() for q, v in self.values.items()}
        print(responses)  # Można zapisać te wartości lub przekazać dalej
        self.root.destroy()
        # Otwórz kolejne pytanie
        root = tk.Tk()
        app = Question5(root)
        root.mainloop()
