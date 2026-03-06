# TripAdvisor NLP Recommendation System

> Content-based place recommendation using only review text — no metadata.
> Built for the Information Retrieval & NLP course (ESILV A4 DIA6).

## Overview

Given the reviews of a TripAdvisor place (hotel, restaurant, or attraction), 
this system recommends the most similar places — relying exclusively on review 
text, not metadata. The core hypothesis: **similar experiences are described 
with similar words**.

## Approach

| Model | Description |
|---|---|
| **BM25** | Baseline sparse retrieval |
| **TF-IDF** (50k vocab) | Best-performing model |
| **TF-IDF variants** | Ablation across vocab sizes & weighting |
| **Linear Fusion** | Interpolation of BM25 + TF-IDF scores |
| **RRF Fusion** | Reciprocal Rank Fusion of BM25 + TF-IDF |
| **Sentence-Transformers** | `all-MiniLM-L6-v2` semantic embeddings |

## Evaluation

Two-level ranking error metric (lower = better):

- **L1** — Does the retrieved place share the same type? (Hotel / Restaurant / Attraction / AP)
- **L2** — Does it share the same subcategory? (cuisine, attraction subtype, price range...)

Evaluated on a 50/50 train-test split of places, with per-type breakdowns.

## Key Results

- TF-IDF (50k vocab) outperformed BM25 and Sentence-Transformers across both levels
- Sentence-Transformers underperformed, likely due to domain mismatch on short, noisy review text
- Attractions showed notably higher L2 error than hotels and restaurants

## Stack

- Python, Jupyter Notebook
- `rank-bm25`, `scikit-learn`, `sentence-transformers`
- `pandas`, `seaborn`, `matplotlib`

## Repository Structure
```
├── notebook.ipynb       # Full pipeline: preprocessing → models → evaluation
├── report.pdf           # Written report with methodology & analysis
└── README.md
```

## Authors

Alvaro SERERO & Leo Winter — ESILV A4 DIA6, 2026