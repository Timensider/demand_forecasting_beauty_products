# Deployment & Inference (Notebook 3)

> Final stage of the forecasting pipeline: turning the trained LightGBM model into a reusable prediction module, ready for real-world scenarios.

---

## Goals

- Load the best-performing LightGBM model from storage  
- Create a modular, scalable `predict()` function  
- Ensure consistency with saved feature column order  
- Structure logic for easy reuse, testing, and future integration  

---

## View the Notebook
👉 
> **Notebook: Deployment & Inference Logic**  
> - [Open in Colab](https://colab.research.google.com/github/Timensider/beauty-product-demand-forecasting/blob/main/notebooks/project_3_deployment.ipynb)  
> - [Try in nbviewer](https://nbviewer.org/url/raw.githubusercontent.com/Timensider/beauty-product-demand-forecasting/main/notebooks/project_3_deployment.ipynb)  
> - [View on GitHub](https://github.com/Timensider/beauty-product-demand-forecasting/blob/main/notebooks/project_3_deployment.ipynb)

---

## What This Notebook Does

- Loads the final model: `lgb_comb_model.pkl`
- Loads the corresponding feature list: `lgb_comb_features.json`
- Builds a `predict(df)` function that:
  - Accepts new data in the same structure as training
  - Reorders columns to match training schema
  - Handles missing columns gracefully
- Simulates how the model would be used in production
  - Example: weekly forecasting updates using live data

---

## Supporting Files

| File                                | Purpose                        |
|-------------------------------------|--------------------------------|
| `lgb_comb_model.pkl`                | Trained LightGBM model         |
| `lgb_comb_features.json`            | Ordered list of feature columns |
| `pipeline/predict.py`               | Reusable prediction function   |

---

## Next Steps

This structure supports:
- Deployment in a batch pipeline or REST API
- Version-controlled model updates
- Easy extension to other SKUs, regions, or business rules

---

## Summary

This notebook closes the loop on the demand forecasting workflow by moving from experimentation to deployment. The focus is on **scalability**, **modularity**, and **real-world readiness** — all key to making data science work in production.

