#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
from src.utils.seed import set_global_seed
from src.iwqi import compute_iwqi, label_iwqi
set_global_seed(42)
row = {"EC": 1000.0, "Na": 3.0, "Cl": 4.0, "HCO3": 2.0, "SAR": 3.0}
iwqi = compute_iwqi(row)
print("IWQI:", iwqi, "Class:", label_iwqi(iwqi))
PY
echo "Smoke test OK."
