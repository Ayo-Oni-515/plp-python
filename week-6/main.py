# Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from IPython.display import display

# Load the Iris dataset
try:
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df["species"] = [iris.target_names[i] for i in iris.target]

    # Display first few rows
    print("First 5 rows of the dataset:")
    display(iris_df.head())

    # Check data types and missing values
    print("\nDataset structure:")
    print(iris_df.info())

    # Check for missing values
    print("\nMissing values:")
    print(iris_df.isnull().sum())

    # Clean data (no missing values in Iris dataset, but for demonstration)
    iris_df.dropna(inplace=True)  # Drop if any missing values
    print("\nData cleaned successfully!")

except Exception as e:
    print(f"Error loading dataset: {e}")

# Compute basic statistics
print("\nBasic statistics for numerical columns:")
display(iris_df.describe())

# Group by species and compute mean
print("\nMean sepal length by species:")
display(iris_df.groupby("species")["sepal length (cm)"].mean())

# Additional interesting findings
print("\nInteresting findings:")
print("- Setosa has the shortest petals but widest sepals.")
print("- Virginica has the longest petals on average.")

plt.figure(figsize=(10, 5))
plt.plot(iris_df["sepal length (cm)"], label="Sepal Length")
plt.title("Sepal Length Trend Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(
    data=iris_df, x="species", y="petal length (cm)", estimator=np.mean)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=iris_df, x="sepal width (cm)", kde=True, bins=15)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=iris_df, x="sepal length (cm)", y="petal length (cm)", hue="species"
)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
