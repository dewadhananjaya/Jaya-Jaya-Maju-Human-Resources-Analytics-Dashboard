import pandas as pd
import joblib
import sys

# ======================================
# 1. Load Model dan Scaler
# ======================================
try:
    model = joblib.load('best_attrition_model.pkl')
    scaler = joblib.load('scaler.pkl')
except FileNotFoundError:
    print("File model atau scaler tidak ditemukan!")
    sys.exit()
except Exception as e:
    print("Terjadi kesalahan saat loading:", e)
    sys.exit()

# ======================================
# 2. Data Baru (Harus Lengkap & Sesuai Training)
# ======================================
data_baru = pd.DataFrame([{
    "EmployeeId": 9999,   
    "Age": 35,
    "BusinessTravel": 1,
    "DailyRate": 800,
    "Department": 1,
    "DistanceFromHome": 10,
    "Education": 3,
    "EducationField": 2,
    "EnvironmentSatisfaction": 3,
    "Gender": 1,
    "HourlyRate": 60,
    "JobInvolvement": 3,
    "JobLevel": 1,
    "JobRole": 2,
    "JobSatisfaction": 3,
    "MaritalStatus": 1,
    "MonthlyIncome": 4000,
    "MonthlyRate": 12000,
    "NumCompaniesWorked": 2,
    "OverTime": 1,
    "PercentSalaryHike": 15,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 3,
    "StockOptionLevel": 1,
    "TotalWorkingYears": 10,
    "TrainingTimesLastYear": 2,
    "WorkLifeBalance": 3,
    "YearsAtCompany": 5,
    "YearsInCurrentRole": 3,
    "YearsSinceLastPromotion": 1,
    "YearsWithCurrManager": 2
}])

# ======================================
# 3. Samakan Urutan Kolom dengan Training
# ======================================
try:
    data_baru = data_baru[scaler.feature_names_in_]
except Exception as e:
    print("Kolom tidak sesuai dengan saat training:", e)
    sys.exit()

# ======================================
# 4. Scaling 
# ======================================
data_scaled = scaler.transform(data_baru)

data_siap_prediksi = pd.DataFrame(
    data_scaled,
    columns=scaler.feature_names_in_
)

# ======================================
# 5. Prediksi
# ======================================
prediksi = model.predict(data_siap_prediksi)
probabilitas = model.predict_proba(data_siap_prediksi)[:, 1]

# ======================================
# 6. Output
# ======================================
hasil = "Leave" if prediksi[0] == 1 else "Stay"

print("=" * 45)
print("        HASIL PREDIKSI ATTRITION")
print("=" * 45)
print(f"Hasil Prediksi     : {hasil}")
print(f"Tingkat Keyakinan  : {probabilitas[0]:.2%}")
print("=" * 45)