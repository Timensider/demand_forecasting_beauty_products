# Modeling & Segment Evaluation (Notebook 2)

> Building and comparing multiple demand forecasting models across 300 SKUs (Product × Region × Channel), with performance evaluation by segment to simulate real-world volatility handling.

---

## Goals

- Build a forecasting pipeline using engineered features (lags, seasonality, promotions, lifecycle, etc.)
- Train and tune a range of models from simple baselines to advanced ML and deep learning
- Improve accuracy through regularization, hyperparameter tuning, and interpretability
- Compare model performance at both global and segment (SKU cluster) level
- Identify scalable forecasting strategies for production use

---

## View the Notebook
> **Notebook: Model Training & Evaluation**  
> - [Open in Colab](https://colab.research.google.com/github/Timensider/demand_forecasting_beauty_products/blob/main/notebooks/project_2_demand_forecasting_models.ipynb)  
> - [Try in nbviewer](https://nbviewer.org/url/raw.githubusercontent.com/Timensider/demand_forecasting_beauty_products/main/notebooks/project_2_demand_forecasting_models.ipynb)  
> - [View on GitHub](https://github.com/Timensider/demand_forecasting_beauty_products/blob/main/notebooks/project_2_demand_forecasting_models.ipynb)

---

## Table of Contents

1. **Statistical Models**
   - Naive Forecast  
   - Generalized Linear Model (GLM)  
   - ARIMA / SARIMA  

2. **Traditional Machine Learning**
   - Ridge, Lasso, ElasticNet  
   - LightGBM (Baseline → Regularized → Tuned)  
   - Hyperparameter tuning via Optuna  

3. **Deep Learning**
   - Multivariate LSTM  
   - Convolutional Neural Network (CNN)  
   - Tuned CNN architecture  

4. **Segment-Level Performance**
   - Compare model accuracy across SKU volatility clusters  
   - Identify strengths and weaknesses of each model type by segment  

---

## Model Evaluation Metrics

- **RMSE** – Root Mean Squared Error  
- **MAE** – Mean Absolute Error  
- **R²** – Coefficient of Determination  
- **MAPE** – Mean Absolute Percentage Error  

---

## Final Results (Test Set)

| Model              | RMSE   | MAE    | R²     |
|-------------------|--------|--------|--------|
| GLM               | 0.2018 | 0.1562 | 0.9216 |
| Ridge             | 0.1732 | 0.1347 | 0.9422 |
| LightGBM (Tuned)  | 0.0763 | 0.0615 | 0.9888 |
| LSTM              | 0.2006 | 0.1564 | 0.9479 |
| CNN               | 0.2937 | 0.2190 | 0.8883 |
| CNN (Tuned)       | 0.2916 | 0.2295 | 0.8899 |


**Best Model**: LightGBM (tuned)  
- Best generalization  
- Strong performance across stable & medium-demand SKUs  
- Efficient and explainable (with SHAP)

---

## Segment-Level Performance

Demand volatility segments were defined in Notebook 1 using clustering. Models were evaluated across:

| Demand Cluster              | Excellent | Good | Weak |
|----------------------------|-----------|------|------|
| Low Demand / Stable        | 129       | 36   | 7    |
| Medium Demand / Stable     | 104       | —    | —    |
| High Demand / Volatile     | 18        | —    | —    |
| Very High Demand / Volatile| 6         | —    | —    |

> Segment-based evaluation highlights model strengths in stable segments and exposes weaknesses in highly volatile demand — critical insight for real-world deployment.

---

## Key Takeaways

 - Basic statistical models like Naive Forecast and GLM gave us a decent starting point, but they couldn’t handle more complex patterns in the data.
 - Regularized models like Ridge, Lasso, and ElasticNet did better — but they were still limited compared to more flexible models like LightGBM.
 - LightGBM performed the best overall — especially when combined with engineered features and hyperparameter tuning.
 - Deep learning models (LSTM, CNN) were included, but didn’t match LightGBM’s performance on this structured, feature-rich dataset.
 - That’s not unexpected — deep learning tends to need more tuning and deeper input sequences to work well on tabular data.
 - At the segment level, LightGBM consistently did better in stable demand groups, making it a strong choice for real-world forecasting tasks.

---

## Next Step

👉 [Continue to: Deployment & Real-World Scoring →](README_deployment.md)
