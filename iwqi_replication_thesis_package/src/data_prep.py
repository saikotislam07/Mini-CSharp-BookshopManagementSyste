from dataclasses import dataclass
import pandas as pd
import numpy as np
from .iwqi import compute_sar, compute_iwqi, label_iwqi, mgL_to_meqL_ca, mgL_to_meqL_mg, mgL_to_meqL_na, mgL_to_meqL_cl, mgL_to_meqL_hco3

@dataclass
class DataPreprocessor:
    def convert_units(self, df: pd.DataFrame) -> pd.DataFrame:
        # Assume inputs may be mg/L, convert to meq/L for cations/anions
        out = df.copy()
        if "Ca" in out.columns: out["Ca"] = out["Ca"].astype(float).map(mgL_to_meqL_ca)
        if "Mg" in out.columns: out["Mg"] = out["Mg"].astype(float).map(mgL_to_meqL_mg)
        if "Na" in out.columns: out["Na"] = out["Na"].astype(float).map(mgL_to_meqL_na)
        if "Cl" in out.columns: out["Cl"] = out["Cl"].astype(float).map(mgL_to_meqL_cl)
        if "HCO3" in out.columns: out["HCO3"] = out["HCO3"].astype(float).map(mgL_to_meqL_hco3)
        return out

    def add_sar(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        out["SAR"] = compute_sar(out["Na"], out["Ca"], out["Mg"])
        return out

    def compute_iwqi_and_label(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        out["IWQI"] = df.apply(lambda r: compute_iwqi({"EC": r["EC"], "Na": r["Na"], "Cl": r["Cl"], "HCO3": r["HCO3"], "SAR": r["SAR"]}), axis=1)
        out["IWQI_Class"] = out["IWQI"].map(label_iwqi)
        return out
