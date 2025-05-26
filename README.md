![Luxury Cosmetics Banner](assets/beauty_products_.png)

# Beauty Product Demand Forecasting
A Multi-Model Pipeline for Predicting Product Demand

This project builds a full machine learning pipeline to forecast weekly demand for global beauty products. It includes traditional models, deep learning, and deployment-ready code — all designed to reflect a real-world ML workflow from raw data to predictions.

---

## Dataset

**Source:**  
[Most Used Beauty Cosmetics Products in the World](https://www.kaggle.com/datasets/waqi786/most-used-beauty-cosmetics-products-in-the-world) by [@waqi786](https://www.kaggle.com/waqi786)

> This dataset has been extended with synthetic time-series and business features such as weekly sales, region, channel, promotion flag, lifecycle stages, seasonality, etc.  
> **Use: Educational only — not for commercial purposes.**

---

## Project Overview

### 1. EDA & Preprocessing

- Explored demand across product, region, and channel
- Created `Pseudo_SKU_ID` to track product-region-channel combinations
- Engineered features for modeling:  
- Lag features, rolling stats, seasonality, promo interactions
- Applied clustering to segment SKUs by demand volatility

### 2. Model Training & Comparison

**Models evaluated:**

| Type         | Models                                      |
|--------------|---------------------------------------------|
| Statistical  | Naive Forecast, GLM, ARIMA, SARIMA          |
| ML           | Ridge, Lasso, ElasticNet, LightGBM (Tuned)  |
| Deep Learning| Multivariate LSTM, CNN, Tuned CNN           |

Metrics used:
- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)
- R² (Coefficient of Determination)
- MAPE (Mean Absolute Percentage Error)

**Best model**: `LightGBM (combined + tuned)`

### 3. Deployment

- Saved LightGBM model + feature column list
- Built `predict()` function for real-world scoring
- Simulated predictions as they would occur in production

---

## Model Performance (Test Set)

| Model              | RMSE   | MAE    | R²     |
|-------------------|--------|--------|--------|
| GLM               | 0.2018 | 0.1562 | 0.9216 |
| LightGBM (Final)  | 0.0763 | 0.0615 | 0.9888 |
| LSTM              | 20.89  | 12.49  | 0.9253 |
| CNN               | 40.88  | 20.48  | 0.7139 |
| CNN (Tuned)       | 29.05  | 16.94  | 0.8555 |

LightGBM showed best generalization with low test error and minimal overfitting.

## Segment-Level Evaluation  

### Forecastability of SKUs by Demand Clusters

| Demand Cluster              | Excellent | Good | Weak |
|-------------------------------------|-----------|------|------|
| Low Demand / Stable                 | 129       | 36   | 7    |
| Medium Demand / Stable              | 104       | —    | —    |
| High Demand / Volatile              | 18        | —    | —    |
| Very High Demand / Highly Volatile | 6         | —    | —    |

*SKU = Product ID x Region x Channel*

## Repository Layout   
/data  
    beauty_dataset_2yr_smoothed_realistic  
    train_encoded.parquet  
    test_encoded.parquet  
    train_featured_raw.parquet  
    test_featured_raw.parquet  
    train_featured_start.parquet  
    test_featured_start.parquet  
    train_reduced.parquet  
    test_reduced.parquet  
    X_test_lgb_comb.parquet  

/models  
    lgb_comb_features.json   
    lgb_comb_model.pkl    

/notebooks  
    project_1_eda_preprocessing.ipynb  
    project_2_demand_forecasting_models.ipynb  
    project_3_deployment.ipynb  

/pipeline  
    predict.py  
    __init__.py      

README.md   
requirements.txt   
requirements_experiment.txt   
LICENSE   

## Author   
Eszter Varga – Data Scientist    
GitHub: @Timensider   
 
Disclaimer   
This project is for educational purposes only.   
It uses synthetic enhancements and artificial demand logic to simulate a real-world ML scenario.   
