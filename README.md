![Luxury Cosmetics Banner](assets/beauty_products_.png)

# Beauty Product Demand Forecasting

> A real-world ML pipeline for forecasting weekly demand across global beauty product SKUs — from raw business data to deployable predictions.

This project simulates an end-to-end machine learning solution for forecasting demand for hundreds of global beauty product SKUs across regions and channels. It includes:

- Exploratory analysis & feature engineering
- Statistical, ML, and deep learning models
- Segment-aware evaluation
- Deployment-ready code

Built to reflect real-world business forecasting needs — including volatility, seasonality, promotional effects, and demand segmentation.

---

## Key Highlights

- **300 pseudo-SKUs** generated as combinations of product, region, and sales channel (50x3x2)
- **Best Model**: LightGBM with R² = **0.9888**
- Segment-level performance analysis across volatility clusters
- Real-time scoring pipeline included

---

## Dive Deeper into Each Stage

| Stage | Description | Link |
|-------|-------------|------|
| **EDA & Feature Engineering** | Time-based features, volatility clustering, lag/promo analysis | [View README_eda.md →](notebooks/README_eda.md) |
| **Modeling & Segment Evaluation** | LightGBM, CNN, LSTM, plus performance by SKU cluster | [View README_modeling.md →](notebooks/README_modeling.md) |
| **Deployment** | Model serialization, feature handling, production-ready `predict()` | [View README_deployment.md →](notebooks/README_deployment.md) |

---

## Dataset

**Source:**  
[Kaggle – Most Used Beauty Cosmetics Products](https://www.kaggle.com/datasets/waqi786/most-used-beauty-cosmetics-products-in-the-world)

> This dataset has been extended with synthetic demand signals, weekly sales, channel and promotion data, lifecycle indicators, and seasonal context.

⚠️ **Use**: Educational purposes only. Not for commercial use.

---

## Repository Structure

```bash
/data                  # Parquet-formatted processed data
/models                # Trained model + feature list
/notebooks             # Project notebooks + sub-READMEs
/pipeline              # Deployment script and init
README.md              # You're here
requirements.txt       # Runtime dependencies
LICENSE                # MIT License
🧑‍💻 Author
Eszter Varga – Data Scientist
GitHub: @Timensider

⚠️ Disclaimer
This is an educational project built from publicly available data and synthetic demand logic.   
It reflects an applied ML workflow, not production data or commercial models.