import tkinter as tk
import numpy as np
from model.prediction import load_model_and_scaler, predict_outcome


class ResultWindow:
    def __init__(self, root, responses):
        self.root = root
        self.root.title("Wyniki badania")
        self.root.geometry("800x800")

        # Mapa tłumaczeń zmiennych na polskie nazwy
        translations = {
            "Age": "Wiek",
            "Sex": "Płeć",
            "Ethnicity:": "Pochodzenie etniczne",
            "EducationLevel": "Poziom wykształcenia",
            "BMI": "BMI",
            "Smoking": "Palenie papierosów",
            "AlcoholConsumption": "Spożycie alkoholu (jednostki tygodniowo)",
            "PhysicalActivity": "Aktywność fizyczna (godziny tygodniowo)",
            "DietQuality": "Jakość diety",
            "SleepQuality": "Jakość snu",
            "FamilyHistoryAlzheimers": "Historia Alzheimera w rodzinie",
            "CardiovascularDisease": "Choroba sercowo-naczyniowa",
            "Diabetes": "Cukrzyca",
            "Depression": "Depresja",
            "HeadInjury": "Uraz głowy",
            "Hypertension": "Nadciśnienie",
            "SystolicBP": "Ciśnienie skurczowe (mmHg)",
            "DiastolicBP": "Ciśnienie rozkurczowe (mmHg)",
            "CholesterolTotal": "Cholesterol całkowity (mg/dL)",
            "CholesterolLDL": "Cholesterol LDL (mg/dL)",
            "CholesterolHDL": "Cholesterol HDL (mg/dL)",
            "CholesterolTriglycerides": "Trójglicerydy (mg/dL)",
            "MMSE": "Wynik MMSE (0-30)",
            "FunctionalAssessment": "Ocena funkcjonalna (0-10)",
            "MemoryComplaints": "Problemy z pamięcią",
            "BehavioralProblems": "Problemy behawioralne",
            "ADL": "Codzienne funkcjonowanie (0-10)",
            "Confusion": "Stan zmieszania/zagubienia",
            "Disorientation": "Dezorientacja",
            "PersonalityChanges": "Zmiany osobowości",
            "DifficultyCompletingTasks": "Trudności z wykonywaniem zadań",
            "Forgetfulness": "Zapominanie"
        }

        # Tytuł sekcji
        tk.Label(root, text="Podsumowanie wywiadu", font=("Arial", 16, "bold")).pack(pady=10)

        # Tworzenie raportu z odpowiedzi
        text_area = tk.Text(root, wrap="word", font=("Arial", 12))
        text_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        report_text = """Raport badania:
------------------------
"""

        for question, answer in responses.items():
            translated_question = translations.get(question, question)  # Jeśli brak tłumaczenia, użyj oryginału
            report_text += f"{translated_question}: {answer}\n"

        # Wczytanie modelu i skalera
        print("DEBUG - Próba wczytania modelu i skalera...")
        model, scaler = load_model_and_scaler()
        print("DEBUG - Model:", model)
        print("DEBUG - Skaler:", scaler)

        if model is not None and scaler is not None:
            model_features = [
                "MemoryComplaints", "BehavioralProblems", "EducationLevel",
                "Hypertension", "SleepQuality", "CholesterolLDL", "CholesterolHDL",
                "MMSE", "FunctionalAssessment", "ADL"
            ]
            print("Zapisane odpowiedzi w responses:", responses)

            input_data = np.array([[responses.get(feature, 0) for feature in model_features]])
            print("Dane przekazywane do modelu:", input_data)
            prediction = predict_outcome(model, scaler, input_data)[0]  # Predykcja

            result_label = tk.Label(root, font=("Arial", 14, "bold"))
            result_label.pack(pady=20)

            if prediction == 1:
<<<<<<< HEAD
                result_label.config(text="Istnieje wysokie prawdopodobieństwo, że chorujesz na chorobę Alzheimera",
                                    fg="red")
            else:
                result_label.config(text="Nie chorujesz na chorobę Alzheimera", fg="green")
=======
                result_label.config(
                    text="Wynik pozytywny\nIstnieje wysokie prawdopodobieństwo, że chorujesz na Alzheimera.",
                    fg="red", font=("Arial", 14, "bold"))
            else:
                result_label.config(text="Wynik negatywny.\nNie chorujesz na chorobę Alzheimera.",
                                    fg="green", font=("Arial", 14, "bold"))
>>>>>>> gui
        else:
            result_label = tk.Label(root, text="Błąd: Nie znaleziono modelu lub skalera.", font=("Arial", 14, "bold"),
                                    fg="red")
            result_label.pack(pady=20)

        text_area.insert(tk.END, report_text)
        text_area.config(state=tk.DISABLED)

        # Informacja o diagnozie
        disclaimer = tk.Label(root,
                              text="Diagnoza jest efektem działania modelu statystycznego i ma charakter orientacyjny.\nPełną diagnozę może postawić jedynie wykwalifikowany lekarz.",
                              font=("Arial", 10), fg="gray")
        disclaimer.pack(pady=10)

        # Przycisk zamknięcia
        tk.Button(root, text="Zamknij", font=("Arial", 14), command=root.destroy).pack(pady=20)
