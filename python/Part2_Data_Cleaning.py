# ==========================================================
# Netflix Content Analytics
# Part 2 : Data Cleaning
# Author : Varalakshmi
# ==========================================================

import pandas as pd

print("=" * 60)
print("NETFLIX CONTENT ANALYTICS")
print("PART 2 : DATA CLEANING")
print("=" * 60)

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Netflix-Content-Analytics\dataset\netflix_titles.csv")

# ==========================================================
# Dataset Shape Before Cleaning
# ==========================================================

print("\nDataset Shape Before Cleaning")
print(df.shape)

# ==========================================================
# Missing Values
# ==========================================================

print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

# ==========================================================
# Remove Duplicate Records
# ==========================================================

duplicates = df.duplicated().sum()

print("\nDuplicate Records :", duplicates)

df.drop_duplicates(inplace=True)

print("Duplicates Removed Successfully")

# ==========================================================
# Fill Missing Director
# ==========================================================

df["director"] = df["director"].fillna("Unknown")

# ==========================================================
# Fill Missing Cast
# ==========================================================

df["cast"] = df["cast"].fillna("Not Available")

# ==========================================================
# Fill Missing Country
# ==========================================================

df["country"] = df["country"].fillna("Unknown")

# ==========================================================
# Fill Missing Rating
# ==========================================================

mode_rating = df["rating"].mode()[0]

df["rating"] = df["rating"].fillna(mode_rating)

# ==========================================================
# Fill Missing Date Added
# ==========================================================

df["date_added"] = df["date_added"].fillna("Unknown")

# ==========================================================
# Fill Missing Duration
# ==========================================================

df["duration"] = df["duration"].fillna("Unknown")

# ==========================================================
# Fill Missing Listed In
# ==========================================================

df["listed_in"] = df["listed_in"].fillna("Unknown")

# ==========================================================
# Fill Missing Description
# ==========================================================

df["description"] = df["description"].fillna("No Description")

# ==========================================================
# Missing Values After Cleaning
# ==========================================================

print("\nMissing Values After Cleaning")

print(df.isnull().sum())

# ==========================================================
# Convert Date Added
# ==========================================================

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# ==========================================================
# Extract Month
# ==========================================================

df["Month_Added"] = df["date_added"].dt.month_name()

# ==========================================================
# Extract Year
# ==========================================================

df["Year_Added"] = df["date_added"].dt.year

# ==========================================================
# Extract Day
# ==========================================================

df["Day_Added"] = df["date_added"].dt.day_name()

# ==========================================================
# Content Age
# ==========================================================

current_year = 2026

df["Content_Age"] = current_year - df["release_year"]

# ==========================================================
# Movie / TV Count
# ==========================================================

print("\nContent Type Count")

print(df["type"].value_counts())

# ==========================================================
# Rating Count
# ==========================================================

print("\nRating Count")

print(df["rating"].value_counts())

# ==========================================================
# Country Count
# ==========================================================

print("\nTop Countries")

print(df["country"].value_counts().head(10))

# ==========================================================
# Save Clean Dataset
# ==========================================================

df.to_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Netflix-Content-Analytics\dataset\Netflix_Cleaned.csv", index=False)

print("\nNetflix_Cleaned.csv Saved Successfully")

print("\nDataset Shape After Cleaning")

print(df.shape)

print("\nPART 2 COMPLETED SUCCESSFULLY")