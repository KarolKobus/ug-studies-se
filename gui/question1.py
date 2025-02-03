import tkinter as tk

question_history = []  # Historia pytań


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

        # Przycisk "Dalej"
        tk.Button(root, text="Dalej", font=("Arial", 14), command=self.next_question).pack(pady=10)

        # Przycisk "Wstecz"
        tk.Button(root, text="Wstecz", font=("Arial", 12), command=self.go_back).pack(pady=5)

    def next_question(self):
        """Zapisuje dane i przechodzi do kolejnego okna"""
        sex = self.sex_var.get()
        age = self.age_var.get()
        print(f"Płeć: {sex}, Wiek: {age}")  # Możesz zapisać do pliku
        self.root.destroy()

        # Import kolejnego pytania
        from gui.question2 import Question2
        root = tk.Tk()
        question_history.append(self.__class__)  # Dodajemy okno do historii
        app = Question2(root)
        root.mainloop()

    def go_back(self):
        """Cofa do poprzedniego okna (ekran startowy)"""
        self.root.destroy()

        if question_history:
            prev_window = question_history.pop()
            root = tk.Tk()
            app = prev_window(root)
            root.mainloop()
        else:
            from gui.main_window import MainWindow  # Opóźniony import (rozwiązuje circular import)
            root = tk.Tk()
            app = MainWindow(root)
            root.mainloop()
