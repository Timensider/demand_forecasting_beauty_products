# EDA & Feature Engineering (Notebook 1)

> First step of the forecasting pipeline: cleaning, transforming, and enriching global beauty product demand data to prepare it for traditional and machine learning models.

---

## Goals

- Understand the structure and contents of the raw dataset
- Explore demand patterns across products, regions, and sales channels
- Engineer meaningful features for both statistical and ML-based forecasting
- Segment SKUs by demand behavior to inform later model evaluation

---

## View the Notebook

👉 [Open in nbviewer](https://nbviewer.org/url/raw.githubusercontent.com/Timensider/your-repo-name/main/notebooks/project_1_eda_preprocessing.ipynb)

---

## Table of Contents

1. **Setup** – Imports & Data Loading  
2. **EDA** – Overview, Trends, Column Exploration  
3. **Preprocessing** – Data Split, `Pseudo_SKU_ID`, Clustering  
4. **Feature Engineering** – New Features, Missing Values, Skewness  
5. **Data Cleanup** – Rare Categories, Encoding, Dropping Columns  
6. **Final Steps** – Column Checks & Exporting Processed Data  

---

## Key Steps

### 1. Data Exploration
- Examined raw structure and column meanings
- Visualized demand trends across time
- Explored demand behavior across region and sales channels
- Investigated distribution of numeric and categorical fields

### 2. Preprocessing & Identification
- Split into training and test datasets
- Created `Pseudo_SKU_ID` from `Product_ID × Region × Channel`  
  → **300 total SKUs** (50 products × 3 regions × 2 channels)
- Created a time-indexed panel dataset

### 3. Feature Engineering
- Lag-based features (e.g., sales last 1–3 weeks)
- Rolling stats (mean, std, trend)
- Promo interactions and seasonality flags
- Handling missing values and skewed columns
- One-hot encoding for categorical fields
- Dropped low-variance and unused columns

### 4. Volatility Clustering
- Grouped SKUs by demand behavior:
  - Stable / Low
  - Stable / Medium
  - Volatile
  - Highly Volatile
- Used for **segment-based evaluation in Notebook 2**

---

## Outputs for Modeling

Featured datasets exported to:
/data/train_featured_start.parquet
/data/test_featured_start.parquet

These are used directly for training models in the next stage.

---

## Next Step

👉 [Continue to: Modeling & Segment Evaluation →](README_modeling.md)