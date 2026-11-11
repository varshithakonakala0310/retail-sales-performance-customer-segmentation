# Retail Sales Performance & Customer Segmentation

## Business problem

A retailer needs to understand where revenue comes from over time and which customer groups are most valuable, so marketing and retention effort can be focused where it returns most.

## Questions

1. How does revenue trend month to month, and what is the average order value?
2. Which customers are most valuable (Recency, Frequency, Monetary)?
3. What distinct customer segments exist?

## Dataset

**Synthetic data only** — generated in `analysis.py` with a fixed seed (42): 5,000 orders from 800 customers, 2023-01-01 to 2024-12-30. Saved to `data/retail_orders_synthetic.csv`; RFM table saved to `data/customer_rfm_segments.csv`.

## Method

- Revenue trend and average order value in Python (pandas) and SQL (`sql/analysis.sql`)
- RFM features per customer
- KMeans clustering (k = 4, standardised RFM) for customer segmentation

## Key findings (actual run results)

From `results/results_summary.txt`:

- Total revenue: **£439,515.38** across 5,000 orders; average order value **£87.90**
- Peak month: **2024-06, £24,393.77**
- Highest-value segment: **Segment 0 — 142 customers, average monetary value £1,003.59, average frequency 9.93, average recency 72.9 days**
- Other segments: Segment 1 — 311 customers, £594.49 average monetary; Segment 2 — 250 customers, £310.88; Segment 3 — 96 customers, £358.33 with average recency 356.6 days (largely dormant — a win-back target)

## Tech stack

Python · pandas · NumPy · scikit-learn · SQL

## How to run

```bash
pip install -r requirements.txt
python3 analysis.py
```

## Repository structure

```
├── analysis.py
├── data/
├── sql/analysis.sql
├── results/results_summary.txt
├── requirements.txt
└── LICENSE
```

## License

MIT — see `LICENSE`. Copyright (c) 2026 Varshitha Konakala.
