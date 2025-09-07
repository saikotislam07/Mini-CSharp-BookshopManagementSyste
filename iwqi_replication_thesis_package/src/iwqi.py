import numpy as np
from typing import Dict, Tuple

# Weights from Table 4
WEIGHTS = {"EC": 0.211, "Na": 0.204, "HCO3": 0.202, "Cl": 0.194, "SAR": 0.189}

# IQWI class thresholds from Table 5
IWQI_CLASSES = [
    ("NR", (85, 100)),
    ("LR", (70, 85)),
    ("MR", (55, 70)),
    ("HR", (40, 55)),
    ("SR", (0, 40)),
]

def mgL_to_meqL_ca(x): return x / 20.0    # Eq.(18)
def mgL_to_meqL_mg(x): return x / 12.15   # Eq.(19)
def mgL_to_meqL_na(x): return x / 22.99   # Eq.(20)
def mgL_to_meqL_cl(x): return x / 35.45   # Eq.(21)
def mgL_to_meqL_hco3(x): return x / 61.02 # Eq.(22)

def compute_sar(na_meq, ca_meq, mg_meq):
    # Eq.(1)
    return na_meq / np.sqrt((ca_meq + mg_meq)/2.0 + 1e-12)

# Table 3 qi bands per parameter
QI_BANDS = {
    "EC": [(200,750, (85,100)), (750,1500, (60,85)), (1500,3000, (35,60)), (None, None, (0,35))],
    "SAR": [(2,3, (85,100)), (3,6, (60,85)), (6,12, (35,60)), (None, None, (0,35))],
    "Na": [(2,3, (85,100)), (3,6, (60,85)), (6,9, (35,60)), (None, None, (0,35))],
    "Cl": [(1,4, (85,100)), (4,7, (60,85)), (7,10, (35,60)), (None, None, (0,35))],
    "HCO3": [(1,1.5, (85,100)), (1.5,4.5, (60,85)), (4.5,8.5, (35,60)), (None, None, (0,35))],
}

def _qi_value(param, x):
    # Piecewise mapping per Table 3; Eq.(3) is formal, here we map to class maxima
    bands = QI_BANDS[param]
    for lo, hi, (q_lo, q_hi) in bands:
        if lo is None:
            # out of band (EC<200 or EC>=3000 etc.)
            return q_hi
        if x >= lo and x < hi:
            return q_hi
    return 35  # default to lowest band upper value

def compute_iwqi(features: Dict[str, float]) -> float:
    # features: {"EC":..., "Na":..., "Cl":..., "HCO3":..., "SAR":...}
    q = {}
    for k in ["EC","SAR","Na","Cl","HCO3"]:
        q[k] = _qi_value(k, float(features[k]))
    iwqi = sum(q[k]*WEIGHTS[k if k in WEIGHTS else k] for k in q)
    return float(iwqi)

def label_iwqi(iwqi: float) -> str:
    for name, (lo, hi) in IWQI_CLASSES:
        if iwqi >= lo and iwqi <= hi:
            return name
    return "SR"
