# Time Series Sales Regional EDA Analysis on Retail Dataset

This repository contains a reproducible data analysis project centered on a Jupyter Notebook and a tabular dataset (`sales.xlsx`).

## What this project covers
- Exploratory Data Analysis (EDA) with charts
- Aggregation by product/region/time (groupby / pivot)
- Time-based analysis and resampling

## Repository structure
```
.
├── data
│   ├── raw
│   │   └── sales.xlsx
│   └── processed/
├── notebooks
│   └── sales_analysis.ipynb
├── reports
│   └── figures/
├── src
│   └── quick_summary.py
├── requirements.txt
└── .gitignore
```

## Dataset
- Rows: **525461**
- Columns: **8**
- Column names:
- `InvoiceNumber`
- `ProductCode`
- `ProductName`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerId`
- `Country`

## Getting started
```bash
python -m venv .venv
# activate ...
pip install -r requirements.txt
jupyter notebook notebooks/sales_analysis.ipynb
```
