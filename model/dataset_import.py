# Zbiór danych pochodzi z: https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data
# Autor: Rabie El Kharoua
# Digital Object Identifier: 10.34740/kaggle/dsv/8668279
# License: Attribution 4.0 International (CC BY 4.0)
#---------------------------------------------------------------------#

#----------------------Importowanie bibliotek-------------------------#
import os
import pandas as pd
import numpy as np
import joblib # Do zapisu danych w formacie .pkl
from sklearn.feature_selection import chi2 # Test istotności chi-kwadrat
from scipy.stats import shapiro, levene, f_oneway, mannwhitneyu # Testy na normalność rozkładu i istotności (ANOVA, Umanna-Withney'a)
from sklearn.preprocessing import StandardScaler  # Skalowanie cech (standaryzacja)
from sklearn.model_selection import train_test_split  # Podział zbioru danych na zbiór treningowy i testowy

#------------------Wczytanie zbioru danych-----------------------------#
# Ważne: plik .csv musi znajdować się w tym samym katalogu co plik .py

# Pobranie katalogu, w którym znajduje się ten skrypt
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ścieżka do pliku CSV w tym samym folderze co skrypt
file_path = os.path.join(script_dir, "alzheimers_disease_data.csv")

# Sprawdzenie, czy plik istnieje
if not os.path.exists(file_path):
    print(f"Plik nie istnieje: {file_path}")
else:
    print(f"Odczyt danych z: {file_path}")

#---------------Wczytanie pliku CSV----------------------------#
dataset = pd.read_csv(file_path)

#---------------Pozbywamy się braków danych---------------------#

# Usuwanie kolumn z więcej niż 50% brakujących wartości
threshold = 0.5  # 50% brakujących danych

# Obliczenie procentu brakujących wartości w każdej kolumnie
missing_percentage = dataset.isna().sum() / len(dataset)

# Lista kolumn do usunięcia
columns_to_drop = missing_percentage[missing_percentage > threshold].index

# Usunięcie tych kolumn oraz 'PatientID' i 'DoctorInCharge'
a = dataset.drop(columns=columns_to_drop)
b = a.drop(columns=['PatientID','DoctorInCharge'])
dataset = b

#----------------------Testy statystyczne dla sprawdzenia istotności zmiennych-------------------------#
# Próg istotności
alpha = 0.15
#----------------------Zmienne kategoryczne (nominalne)------------------------------------------------#
X_cat = dataset[["Gender", "Ethnicity", "EducationLevel", "Smoking", "FamilyHistoryAlzheimers", 
                 "CardiovascularDisease", "Diabetes", "Depression", "HeadInjury", "Hypertension",
                 "MemoryComplaints", "BehavioralProblems", "Confusion", "Disorientation", 
                 "PersonalityChanges", "DifficultyCompletingTasks", "Forgetfulness"]]
y = dataset["Diagnosis"]

# Test chi-kwadrat
chi2_scores, p_values = chi2(X_cat, y)

# Tworzenie DataFrame z wynikami
chi2_results = pd.DataFrame({"Feature": X_cat.columns, "p-value": p_values})
chi2_results = chi2_results.sort_values(by="p-value")

# Wybór istotnych zmiennych (p-value <= 0.05)
significant_categorical = chi2_results[chi2_results["p-value"] <= alpha]["Feature"].tolist()

#----------------------Zmienne liczbowe-----------------------------------------------------------------#
numerical_features = ["Age", "BMI", "AlcoholConsumption", "PhysicalActivity", "DietQuality", 
                      "SleepQuality", "SystolicBP", "DiastolicBP", "CholesterolTotal", 
                      "CholesterolLDL", "CholesterolHDL", "CholesterolTriglycerides", 
                      "MMSE", "FunctionalAssessment", "ADL"]

significant_numerical = []

for feature in numerical_features:
    group1 = dataset[dataset["Diagnosis"] == 0][feature]
    group2 = dataset[dataset["Diagnosis"] == 1][feature]
    
    # Test normalności
    p_shapiro1 = shapiro(group1).pvalue
    p_shapiro2 = shapiro(group2).pvalue
    
    # Test homogeniczności wariancji
    p_levene = levene(group1, group2).pvalue
    
    # Wybór testu
    if p_shapiro1 > alpha and p_shapiro2 > alpha and p_levene > alpha:
        test_name = "ANOVA"
        p_value = f_oneway(group1, group2).pvalue
    else:
        test_name = "Mann-Whitney"
        p_value = mannwhitneyu(group1, group2, alternative='two-sided').pvalue
    
    # Jeśli zmienna jest istotna, dodajemy ją do listy
    if p_value <= alpha:
        significant_numerical.append(feature)

# Złączenie finalnego datasetu - wybór zmiennych istotnych statystycznie
selected_features = significant_categorical + significant_numerical + ["Diagnosis"]
cleaned_dataset = dataset[selected_features]
dataset = cleaned_dataset
#print(dataset.columns)

#------------------Dzielimy zbiór na zmienne zależne i niezależne-----------------#

# Musimy to formatować do obiektu typu numpy.array
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#------------------Standaryzacja zmiennych----------------------------------------#
# Tak aby różnorodne zmienne dało się ze sobą porównywać
sc = StandardScaler()
X = sc.fit_transform(X)

#------------------Dzielimy zbiór na testowy i treningowy-------------------------#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

#------------------Zapisujemy zbiory i standard scalar do plików .pkl---------------------------------#
dataset_file_path = os.path.join(script_dir, "dataset.pkl")
scalar_path = os.path.join(script_dir, "scalar.pkl")

joblib.dump((X_train, X_test, y_train, y_test), dataset_file_path)
joblib.dump(sc,scalar_path)

print(f"Zapisano plik: {dataset_file_path}")
print(f"Zapisano plik: {scalar_path}")

if os.path.exists(dataset_file_path):
    print("Plik dataset.pkl został pomyślnie zapisany!")
else:
    print("Błąd: plik dataset.pkl nie został znaleziony po zapisie!")

if os.path.exists(scalar_path):
    print("Plik scalar.pkl został pomyślnie zapisany!")
else:
    print("Błąd: plik scalar.pkl nie został znaleziony po zapisie!")