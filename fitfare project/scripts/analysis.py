import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned/final_cleaned.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# -----------------------------------
# 1. Rating Distribution Histogram
# -----------------------------------

if 'Rating' in df.columns:

    plt.figure(figsize=(8,5))

    plt.hist(df['Rating'], bins=10)

    plt.title("Rating Distribution")

    plt.xlabel("Ratings")

    plt.ylabel("Number of Fitness Centres")

    plt.savefig("visuals/rating_distribution.png")

    plt.close()

    print("rating_distribution.png saved!")

# -----------------------------------
# 2. Top Categories Analysis
# -----------------------------------

if 'Category' in df.columns:

    category_counts = df['Category'].value_counts()

    plt.figure(figsize=(10,6))

    category_counts.plot(kind='bar')

    plt.title("Fitness Categories Count")

    plt.xlabel("Category")

    plt.ylabel("Count")

    plt.xticks(rotation=45)

    plt.savefig("visuals/category_analysis.png")

    plt.close()

    print("category_analysis.png saved!")

# -----------------------------------
# 3. Top Areas Analysis
# -----------------------------------

if 'Area' in df.columns:

    top_areas = df['Area'].value_counts().head(10)

    plt.figure(figsize=(10,6))

    top_areas.plot(kind='bar')

    plt.title("Top 10 Fitness Areas")

    plt.xlabel("Area")

    plt.ylabel("Number of Centres")

    plt.xticks(rotation=45)

    plt.savefig("visuals/top_areas.png")

    plt.close()

    print("top_areas.png saved!")

# -----------------------------------
# 4. Reviews vs Ratings
# -----------------------------------

if 'Rating' in df.columns and 'Number_of_Reviews' in df.columns:

    plt.figure(figsize=(8,5))

    plt.scatter(df['Number_of_Reviews'], df['Rating'])

    plt.title("Reviews vs Ratings")

    plt.xlabel("Number of Reviews")

    plt.ylabel("Rating")

    plt.savefig("visuals/review_vs_rating.png")

    plt.close()

    print("review_vs_rating.png saved!")

print("Analysis Completed Successfully!")

# -----------------------------------
# 2. Category Analysis
# -----------------------------------

if 'Category' in df.columns:

    category_counts = df['Category'].value_counts()

    plt.figure(figsize=(10,6))

    category_counts.plot(kind='bar')

    plt.title("Fitness Categories Count")

    plt.xlabel("Category")

    plt.ylabel("Count")

    plt.xticks(rotation=45)

    plt.savefig("visuals/category_analysis.png")

    plt.close()

    print("category_analysis.png saved!")

# -----------------------------------
# 3. Top Areas
# -----------------------------------

if 'Area' in df.columns:

    top_areas = df['Area'].value_counts().head(10)

    plt.figure(figsize=(10,6))

    top_areas.plot(kind='bar')

    plt.title("Top 10 Areas")

    plt.xlabel("Area")

    plt.ylabel("Number of Fitness Centres")

    plt.xticks(rotation=45)

    plt.savefig("visuals/top_areas.png")

    plt.close()

    print("top_areas.png saved!")

# -----------------------------------
# 4. Reviews vs Ratings
# -----------------------------------

if 'Rating' in df.columns and 'Number_of_Reviews' in df.columns:

    plt.figure(figsize=(8,5))

    plt.scatter(df['Number_of_Reviews'], df['Rating'])

    plt.title("Reviews vs Ratings")

    plt.xlabel("Number of Reviews")

    plt.ylabel("Rating")

    plt.savefig("visuals/review_vs_rating.png")

    plt.close()

    print("review_vs_rating.png saved!")