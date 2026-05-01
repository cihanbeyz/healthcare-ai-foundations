import pandas as pd
df = pd.read_csv("vitals.csv")
print(df.describe())
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())
print("\n=== ABNORMOL HEART RATE (<60 or >100) ===")
abnormal_hr = (df["heart_rate"] < 60) | (df["heart_rate"] > 100)
print(df[abnormal_hr][["patient_id","heart_rate"]])

print("\n== ABNORMAL SpO2 (<90) ===")
abnormal_spo2 = df["spo2"] < 90
print(df[abnormal_spo2][["patient_id","spo2"]])

def hr_category(hr):
    if hr < 60:
        return "Bradycardia"
    elif hr > 100:
        return "Tachycardia"
    else:
        return "Normal"
    
df["hr_category"] = df["heart_rate"].apply(hr_category)
print("\n=== HEART RATE CATEGORIES COUNT ===")
print(df["hr_category"].value_counts())



