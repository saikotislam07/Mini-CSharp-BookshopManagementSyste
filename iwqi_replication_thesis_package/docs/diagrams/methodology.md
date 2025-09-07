# Methodology Diagrams (Mermaid)

> Recreated based on Mustapha et al., 2025 (Fig. 1; Sections 2.1–2.5)【7†source】

```mermaid
flowchart TD
  A[Raw Hydrochemical Data<br/>USGS Brackish Groundwater] --> B[Unit Harmonization<br/>(mg/L → meq/L)]
  B --> C[Impute Missing EC<br/>Random Forest (R²=0.98)]
  C --> D[Compute Derived: SAR]
  D --> E[Compute IWQI (Meireles)]
  E --> F{Class Imbalance Handling}
  F -->|class_weight| G[Stacked Ensemble (RF,DT,LR → LR meta)]
  F -->|ADASYN| H[Stacked Ensemble (RF,DT,LR → LR meta)]
  F -->|cost-sensitive| I[AMSVM (rbf, γ=0.1, C=0.1)]
  G --> J[10-fold CV & Metrics]
  H --> J
  I --> J
```
