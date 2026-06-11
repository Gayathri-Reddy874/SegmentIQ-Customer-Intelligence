# SegmentIQ: AI-Powered Customer Segmentation & Recommendation Engine

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-KMeans-orange)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow)
![Apriori](https://img.shields.io/badge/Association%20Rules-Apriori-green)

### Customer Intelligence Platform using Machine Learning and Market Basket Analysis

</div>

---

## Overview

SegmentIQ is an end-to-end Machine Learning application that analyzes customer behavior, automatically segments customers into meaningful groups, and generates intelligent recommendations using Association Rule Mining.

The project combines:

- Customer Segmentation using Unsupervised Machine Learning
- Market Basket Analysis using Apriori Algorithm
- Interactive Streamlit Dashboard
- Automated Model Selection using Silhouette Score
- Real-Time Customer Analysis and Recommendations

This solution helps businesses identify customer groups, understand behavioral patterns, and improve personalization strategies.

---

## Business Problem

E-commerce companies generate massive amounts of customer data but often struggle to:

- Identify customer segments
- Understand purchasing behavior
- Personalize recommendations
- Improve customer engagement
- Increase retention and conversion rates

SegmentIQ addresses these challenges by automatically grouping similar customers and generating data-driven recommendations.

---

## Features

### Customer Segmentation
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Gaussian Mixture Models (GMM)
- Automatic Best Model Selection

### Recommendation Engine
- Apriori Algorithm
- Association Rule Mining
- Confidence-Based Recommendations
- Behavioral Pattern Discovery

### Data Processing
- Missing Value Handling
- Feature Engineering
- Label Encoding
- Standard Scaling
- Duplicate Removal

### Interactive Dashboard
- Modern Streamlit Interface
- Real-Time Predictions
- Customer Profile Visualization
- Recommendation Display
- Responsive UI

---

## Machine Learning Workflow

```text
Raw Customer Data
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Encoding & Scaling
        │
        ▼
Multiple Clustering Models
        │
        ▼
Best Model Selection
        │
        ▼
Customer Segmentation
        │
        ▼
Association Rule Mining
        │
        ▼
Recommendation Generation
        │
        ▼
Streamlit Dashboard
```

---

## Tech Stack

### Programming Language
- Python

### Data Processing
- Pandas
- NumPy

### Machine Learning
- Scikit-Learn
- MLxtend

### Visualization
- Matplotlib
- Seaborn

### Deployment & UI
- Streamlit

### Model Persistence
- Pickle

---

## Algorithms Used

### Clustering Algorithms

#### K-Means Clustering
Used for customer segmentation by grouping similar customer behavior patterns.

#### Hierarchical Clustering
Creates nested customer groups based on similarity.

#### DBSCAN
Density-based clustering for identifying complex customer distributions.

#### Gaussian Mixture Model (GMM)
Probabilistic clustering approach for customer segmentation.

---

### Association Rule Mining

#### Apriori Algorithm

Used to discover relationships among:

- Device Type
- Browser Preference
- Shipping Method

Metrics Used:

- Support
- Confidence
- Lift

---

## Project Structure

```text
CUSTOMER_SEGMENTATION/
│
├── Screenshots/
│   ├── dashboard.png
│   └── results.png
│
├── app_ecommerce.py
├── train_ecommerce.py
├── model.pkl
├── ecommerce_customer_segmentation_unsupervised.csv
├── requirements.txt
│
└── README.md
```

---

## Dataset Features

The dataset contains customer behavioral and transaction-related information such as:

- Price
- Quantity
- Discount Applied
- Rating
- Session Duration
- Device Type
- Browser
- Shipping Type
- Country
- Transaction Date

Additional engineered features include:

- Days Since Transaction
- Encoded Behavioral Features

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/SegmentIQ-Customer-Intelligence.git

cd SegmentIQ-Customer-Intelligence
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Linux/Mac

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

Run:

```bash
python train_ecommerce.py
```

This will:

- Clean and preprocess data
- Train clustering models
- Evaluate models
- Select the best clustering algorithm
- Generate association rules
- Save model artifacts

Output:

```text
model.pkl
```

---

## Running the Application

Start the Streamlit dashboard:

```bash
streamlit run app_ecommerce.py
```

The application will open in your browser.

---

## Dashboard Preview

### Main Dashboard

Place your screenshot here:

```text
Screenshots/dashboard.png
```

### Results Screen

Place your screenshot here:

```text
Screenshots/results.png
```

---

## Model Evaluation

The project evaluates multiple clustering models using:

### Silhouette Score

Measures:

- Cluster Cohesion
- Cluster Separation

Best-performing model is automatically selected for deployment.

---

## Recommendation Engine Logic

The recommendation engine uses Apriori Association Rules to discover customer behavior patterns.

Example:

```text
If User Uses:
Mobile + Chrome

Recommended:
Express Shipping
```

Recommendations are ranked by:

- Confidence Score
- Rule Strength
- User Behavior Similarity

---

## Key Skills Demonstrated

### Machine Learning
- Unsupervised Learning
- Clustering
- Model Evaluation
- Feature Engineering

### Data Analytics
- Data Cleaning
- Exploratory Data Analysis
- Statistical Analysis

### Recommendation Systems
- Market Basket Analysis
- Association Rule Mining
- Customer Intelligence

### Software Development
- Python Development
- Streamlit Applications
- Model Serialization
- End-to-End ML Pipelines

---

## Resume Highlights

- Built an AI-powered customer segmentation platform using K-Means, GMM, DBSCAN, and Hierarchical Clustering.
- Developed a recommendation engine using Apriori Association Rule Mining for customer behavior analysis.
- Implemented automated model selection using Silhouette Score evaluation.
- Designed an interactive Streamlit dashboard for real-time customer segmentation and recommendations.
- Created an end-to-end machine learning pipeline including preprocessing, clustering, recommendation generation, and deployment.

---

## Future Enhancements

- XGBoost-based customer value prediction
- RFM Analysis
- Customer Lifetime Value (CLV)
- Deep Learning-based Recommendations
- Cloud Deployment (AWS/Azure)
- Real-Time Data Streaming
- API Integration

---

## Author

### Mallareddygari Gayathri

AI & Machine Learning Engineer

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
