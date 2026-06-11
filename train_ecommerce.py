# STEP 1: IMPORT LIBRARIES

import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth


# STEP 2: LOAD DATA

df = pd.read_csv("ecommerce customer segmentation_unsupervised.csv")

print("Initial Shape:", df.shape)

# STEP 3: DATA CLEANING


# Remove duplicates
df.drop_duplicates(inplace=True)

# Fix country format
df['Country'] = df['Country'].astype(str).str.strip().str.title()

# Fix date
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce')

# Fill missing dates
df['TransactionDate'] = df['TransactionDate'].ffill()
df['TransactionDate'] = df['TransactionDate'].bfill()

# Handle all missing values (STRONG FIX)
df = df.ffill()
df = df.bfill()
df.fillna(0, inplace=True)

# Verify no nulls
print("Remaining NaN:", df.isnull().sum().sum())


# STEP 4: FEATURE ENGINEERING


# Convert date to numeric
df['DaysSinceTransaction'] = (pd.Timestamp.now() - df['TransactionDate']).dt.days
df.drop('TransactionDate', axis=1, inplace=True)

# Fix Rating (important for visualization clarity)
df['Rating'] = df['Rating'].astype(float).round(1)

# Encode categorical
le = LabelEncoder()

cat_cols = df.select_dtypes(include=['object', 'string']).columns

for col in cat_cols:
    df[col] = le.fit_transform(df[col].astype(str))


# STEP 5: EDA


plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=30)
plt.title("Price Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Rating'].round(), y='Price', data=df)
plt.title("Price vs Rating")
plt.show()


# STEP 6: SCALING


features = df.columns.tolist()   # Save feature names

scaler = StandardScaler()
X = scaler.fit_transform(df)


# STEP 7: CLUSTERING MODELS


models = {
    "KMeans": KMeans(n_clusters=4, random_state=42),
    "Hierarchical": AgglomerativeClustering(n_clusters=4),
    "DBSCAN": DBSCAN(eps=0.5, min_samples=5),
    "GMM": GaussianMixture(n_components=4)
}

scores = {}
labels_dict = {}

for name, model in models.items():
    
    if name == "GMM":
        labels = model.fit_predict(X)
    else:
        labels = model.fit_predict(X)

    labels_dict[name] = labels

    if len(set(labels)) > 1:
        score = silhouette_score(X, labels)
    else:
        score = -1

    scores[name] = score
    print(f"{name} Silhouette Score:", score)


# STEP 8: BEST MODEL SELECTION


best_cluster_model_name = max(scores, key=scores.get)
print("\nBest Clustering Model:", best_cluster_model_name)

# Train best model again
if best_cluster_model_name == "KMeans":
    final_cluster_model = KMeans(n_clusters=4, random_state=42).fit(X)

elif best_cluster_model_name == "Hierarchical":
    final_cluster_model = AgglomerativeClustering(n_clusters=4)
    final_cluster_model.fit(X)

elif best_cluster_model_name == "DBSCAN":
    final_cluster_model = DBSCAN(eps=0.5, min_samples=5)
    final_cluster_model.fit(X)

else:
    final_cluster_model = GaussianMixture(n_components=4, random_state=42).fit(X)


# STEP 9: ASSOCIATION RULE LEARNING + RECOMMENDATION ENGINE


# Create basket data
basket = pd.get_dummies(df[['Device','Browser','ShippingType']].astype(str))

# Apply Apriori
freq_items = apriori(basket, min_support=0.02, use_colnames=True)

rules = association_rules(freq_items, metric="lift", min_threshold=1)

# Sort rules by confidence (important for recommendations)
rules = rules.sort_values(by='confidence', ascending=False)

print("\nTop Association Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']].head())
print("Total Rules:", len(rules))


# CREATE RECOMMENDATION FUNCTION


def recommend_products(user_items, rules, top_n=5):
    recommendations = []

    for _, row in rules.iterrows():
        antecedents = list(row['antecedents'])
        consequents = list(row['consequents'])

        # Relax condition: partial match
        match_count = sum([1 for item in antecedents if item in user_items])

        if match_count > 0:
            for item in consequents:
                recommendations.append((item, row['confidence']))

    # Sort
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)

    # Remove duplicates
    seen = set()
    final = []
    for item, conf in recommendations:
        if item not in seen:
            seen.add(item)
            final.append((item, conf))

    return final[:top_n]


# SAVE MODEL + RULES


pickle.dump(
    (final_cluster_model, scaler, features, rules),
    open("model.pkl", "wb")
)

print("\nModel + Rules saved successfully!")