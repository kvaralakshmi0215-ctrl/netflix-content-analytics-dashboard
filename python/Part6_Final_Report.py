# ==========================================================
# Netflix Content Analytics
# Part 6 : Final Report
# Author : Varalakshmi
# ==========================================================

import pandas as pd

print("=" * 60)
print("NETFLIX CONTENT ANALYTICS PROJECT")
print("FINAL REPORT")
print("=" * 60)

# ==========================================================
# Load Clean Dataset
# ==========================================================

df = pd.read_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Netflix-Content-Analytics\dataset\Netflix_Cleaned.csv")

# ==========================================================
# KPI Calculations
# ==========================================================

total_titles = len(df)
movies = len(df[df["type"] == "Movie"])
tv_shows = len(df[df["type"] == "TV Show"])
countries = df["country"].nunique()
directors = df["director"].nunique()
genres = df["listed_in"].nunique()
ratings = df["rating"].nunique()

oldest = df["release_year"].min()
latest = df["release_year"].max()

top_country = df["country"].value_counts().idxmax()
top_director = df["director"].value_counts().idxmax()
top_rating = df["rating"].value_counts().idxmax()

# ==========================================================
# Display Final Report
# ==========================================================

print("\n")
print("=" * 60)
print("NETFLIX CONTENT ANALYTICS SUMMARY")
print("=" * 60)

print(f"Total Titles              : {total_titles}")
print(f"Movies                    : {movies}")
print(f"TV Shows                  : {tv_shows}")
print(f"Countries                 : {countries}")
print(f"Directors                 : {directors}")
print(f"Genres                    : {genres}")
print(f"Ratings                   : {ratings}")

print("\n")
print("=" * 60)
print("CONTENT INFORMATION")
print("=" * 60)

print(f"Oldest Release            : {oldest}")
print(f"Latest Release            : {latest}")

print("\n")
print("=" * 60)
print("TOP INSIGHTS")
print("=" * 60)

print(f"Top Country               : {top_country}")
print(f"Top Director              : {top_director}")
print(f"Most Common Rating        : {top_rating}")

print("\n")
print("=" * 60)
print("BUSINESS CONCLUSIONS")
print("=" * 60)

print("1. Netflix has a larger collection of Movies than TV Shows.")
print("2. The United States contributes the highest amount of content.")
print("3. Content production has increased significantly over the years.")
print("4. Drama and International genres are highly represented.")
print("5. Netflix serves audiences across many countries.")
print("6. The platform contains a wide variety of ratings suitable for different age groups.")
print("7. The dataset provides valuable insights into Netflix's global content library.")

# ==========================================================
# Save Summary Report
# ==========================================================

summary = pd.DataFrame({
    "Metric": [
        "Total Titles",
        "Movies",
        "TV Shows",
        "Countries",
        "Directors",
        "Genres",
        "Ratings",
        "Oldest Release",
        "Latest Release",
        "Top Country",
        "Top Director",
        "Top Rating"
    ],
    "Value": [
        total_titles,
        movies,
        tv_shows,
        countries,
        directors,
        genres,
        ratings,
        oldest,
        latest,
        top_country,
        top_director,
        top_rating
    ]
})

summary.to_csv("Netflix_Final_Report.csv", index=False)

print("\nNetflix_Final_Report.csv saved successfully!")

print("\n")
print("=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nThank you for using Netflix Content Analytics!")