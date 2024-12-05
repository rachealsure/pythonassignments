import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Dataset Exploration
try:
    # Load the Iris dataset
    iris_data = load_iris()
    df = pd.DataFrame(
        data=iris_data.data,
        columns=iris_data.feature_names
    )
    df['species'] = iris_data.target
    df['species'] = df['species'].apply(lambda x: iris_data.target_names[x])

    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nDataset Information:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean the dataset (in this case, there are no missing values)
    # If there were missing values, we could fill them or drop them like this:
    # df = df.dropna() or df = df.fillna(value)

except FileNotFoundError:
    print("Error: The dataset file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 2: Basic Data Analysis
try:
    # Basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    # Grouping by species and computing the mean of numerical columns
    grouped = df.groupby('species').mean()
    print("\nMean values by species:")
    print(grouped)

    # Identify patterns
    print("\nInteresting Findings:")
    print("1. Setosa has the smallest petal and sepal measurements.")
    print("2. Virginica has the largest petal length and width.")

except Exception as e:
    print(f"An error occurred during data analysis: {e}")

# Task 3: Data Visualization
try:
    # Line chart (for illustrative purposes, using sepal length of the first 30 samples)
    plt.figure(figsize=(8, 6))
    plt.plot(df.index[:30], df['sepal length (cm)'][:30], label='Sepal Length')
    plt.title('Trend of Sepal Length in First 30 Samples')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.show()

    # Bar chart (average petal length per species)
    plt.figure(figsize=(8, 6))
    sns.barplot(x=grouped.index, y='petal length (cm)', hue=grouped.index, data=grouped, palette='viridis', dodge=False)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.show()

    # Histogram (distribution of petal width)
    plt.figure(figsize=(8, 6))
    sns.histplot(df['petal width (cm)'], kde=True, bins=15, color='pink')
    plt.title('Distribution of Petal Width')
    plt.xlabel('Petal Width (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter plot (sepal length vs. petal length)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x='sepal length (cm)', 
        y='petal length (cm)', 
        hue='species', 
        data=df, 
        palette='deep'
    )
    plt.title('Sepal Length vs. Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.show()

except Exception as e:
    print(f"An error occurred during visualization: {e}")
