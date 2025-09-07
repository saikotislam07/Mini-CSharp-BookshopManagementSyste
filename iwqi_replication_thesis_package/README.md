# IWQI Replication Thesis Package

This repository scaffolds a full replication of **"A hybrid machine learning approach for imbalanced irrigation water quality classification"** (Desalination and Water Treatment 321, 2025).

> This package is prepared as a thesis-grade, deterministic reproduction with pinned configs, modular code, smoke tests, and artifact provenance.

## Contents
- `facts-extract.csv` — machine-extracted facts with table/figure/section references to the paper.
- `configs/config.yml` — single source of truth for seeds, paths, transforms, CV, and models.
- `src/` — modular implementation (preprocessing, IWQI formulas, models, evaluation).
- `notebooks/` — Jupyter notebooks for EDA, preprocessing, training/evaluation.
- `docs/diagrams/` — Mermaid methodology diagrams.
- `tests/` — unit & smoke tests.
- `scripts/` — quick run scripts.

## Getting Started
1. Create a Python 3.9+ environment and install requirements (see `requirements.txt`).
2. Place raw data in `data/raw/` (USGS brackish groundwater extracts). See `experiments/USGS_ingest.md`.
3. Update any paths in `configs/config.yml` if needed.
4. Run the smoke test:
   ```bash
   bash scripts/run_smoke.sh
   ```
5. Run the full pipeline:
   ```bash
   python -m src.run_full --config configs/config.yml
   ```

## Reproducibility
- Deterministic seeds are set in `src/utils/seed.py` and respected in CV and resampling.
- All transformations are config-driven; outputs are versioned under `results/` and `figures/`.

## Citations
Please cite the original paper for all values and methods used in replication.
