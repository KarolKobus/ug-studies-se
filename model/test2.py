import joblib
import pickle

# Wczytaj skaler z oryginalnego pliku
scaler = joblib.load("C:/Users/wrons/ug-studies-se/model/scalar.pkl")

# Zapisz go ponownie w nowym formacie
with open("C:/Users/wrons/ug-studies-se/model/scalar_new.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Skaler został zapisany w nowym formacie jako scalar_new.pkl!")
