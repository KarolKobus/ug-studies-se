import tkinter as tk


class Question1:
    def __init__(self, root):
        self.root = root
        self.root.title("Pytanie 1")
        self.root.geometry("600x400")

        # Pytanie o płeć
        tk.Label(root, text="1. Proszę wybrać płeć:", font=("Arial", 14)).pack(pady=10)
        self.sex_var = tk.IntVar()

        tk.Radiobutton(root, text="Mężczyzna", variable=self.sex_var, value=1, font=("Arial", 12)).pack()
        tk.Radiobutton(root, text="Kobieta", variable=self.sex_var, value=0, font=("Arial", 12)).pack()

        # Pytanie o wiek
        tk.Label(root, text="2. Proszę wybrać wiek:", font=("Arial", 14)).pack(pady=10)
        self.age_var = tk.IntVar(value=60)

        self.age_slider = tk.Scale(root, from_=60, to=100, orient="horizontal", variable=self.age_var,
                                   font=("Arial", 12))
        self.age_slider.pack()

        # Przycisk Dalej
        tk.Button(root, text="Dalej", font=("Arial", 14), command=self.next_question).pack(pady=20)

    def next_question(self):
        sex = self.sex_var.get()
        age = self.age_var.get()
        print(f"Płeć: {sex}, Wiek: {age}")  # Można zapisać te wartości lub przekazać dalej
        self.root.destroy()
        # Tutaj można zaimportować i otworzyć kolejne okno np. Question2
