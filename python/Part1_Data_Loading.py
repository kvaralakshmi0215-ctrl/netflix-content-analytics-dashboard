# ==========================================================
# Netflix Content Analytics
# Part 1 : Data Loading & Data Inspection
# Author : Varalakshmi
# ==========================================================

import pandas as pd

print("=" * 60)
print("NETFLIX CONTENT ANALYTICS")
print("PART 1 : DATA LOADING & DATA INSPECTION")
print("=" * 60)

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Netflix-Content-Analytics\dataset\netflix_titles.csv")

print("\nDataset Loaded Successfully!\n")

# ==========================================================
# Display First 10 Records
# ==========================================================

print("=" * 60)
print("FIRST 10 RECORDS")
print("=" * 60)

print(df.head(10))

# ==========================================================
# Display Last 10 Records
# ==========================================================

print("\n")
print("=" * 60)
print("LAST 10 RECORDS")
print("=" * 60)

print(df.tail(10))

# ==========================================================
# Dataset Shape
# ==========================================================

print("\n")
print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

# ==========================================================
# Column Names
# ==========================================================

print("\n")
print("=" * 60)
print("COLUMN NAMES")
print("=" * 60)

print(df.columns.tolist())

# ==========================================================
# Dataset Information
# ==========================================================

print("\n")
print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()

# ==========================================================
# Data Types
# ==========================================================

print("\n")
print("=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)

# ==========================================================
# Missing Values
# ==========================================================

print("\n")
print("=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# ==========================================================
# Duplicate Records
# ==========================================================

print("\n")
print("=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print("Duplicate Rows :", df.duplicated().sum())

# ==========================================================
# Statistical Summary
# ==========================================================

print("\n")
print("=" * 60)
print("STATISTICAL SUMMARY")
print("=" * 60)

print(df.describe(include='all'))

# ==========================================================
# Unique Values
# ==========================================================

print("\n")
print("=" * 60)
print("UNIQUE VALUES")
print("=" * 60)

print("Content Types :", df["type"].unique())
print("Ratings :", df["rating"].unique())
print("Countries :", df["country"].nunique())
print("Directors :", df["director"].nunique())
print("Genres :", df["listed_in"].nunique())

# ==========================================================
# Total Movies and TV Shows
# ==========================================================

print("\n")
print("=" * 60)
print("CONTENT COUNT")
print("=" * 60)

print(df["type"].value_counts())

# ==========================================================
# Release Year Range
# ==========================================================

print("\n")
print("=" * 60)
print("RELEASE YEAR RANGE")
print("=" * 60)

print("Oldest Content :", df["release_year"].min())
print("Latest Content :", df["release_year"].max())

# ==========================================================
# Save Copy
# ==========================================================

df.to_csv("Netflix_Loaded.csv", index=False)

print("\nNetflix_Loaded.csv saved successfully!")

print("\n")
print("=" * 60)
print("PART 1 COMPLETED SUCCESSFULLY")
print("=" * 60)