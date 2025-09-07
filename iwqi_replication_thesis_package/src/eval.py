import numpy as np
from dataclasses import dataclass
from typing import Dict, Any, Tuple
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

@dataclass
class CVConfig:
    n_splits: int = 10
    shuffle: bool = True
    random_state: int = 42

def evaluate_cv(model, X, y, cv_cfg: CVConfig) -> Dict[str, Any]:
    skf = StratifiedKFold(n_splits=cv_cfg.n_splits, shuffle=cv_cfg.shuffle, random_state=cv_cfg.random_state)
    accs, p_w, r_w, f1_w, p_m, r_m, f1_m = [],[],[],[],[],[],[]
    cms = []
    for train, test in skf.split(X, y):
        model_ = model
        model_.fit(X[train], y[train])
        yhat = model_.predict(X[test])
        accs.append(accuracy_score(y[test], yhat))
        p_w.append(precision_score(y[test], yhat, average="weighted", zero_division=0))
        r_w.append(recall_score(y[test], yhat, average="weighted", zero_division=0))
        f1_w.append(f1_score(y[test], yhat, average="weighted", zero_division=0))
        p_m.append(precision_score(y[test], yhat, average="macro", zero_division=0))
        r_m.append(recall_score(y[test], yhat, average="macro", zero_division=0))
        f1_m.append(f1_score(y[test], yhat, average="macro", zero_division=0))
        cms.append(confusion_matrix(y[test], yhat))
    return {
        "accuracy_mean": float(np.mean(accs)),
        "precision_weighted_mean": float(np.mean(p_w)),
        "recall_weighted_mean": float(np.mean(r_w)),
        "f1_weighted_mean": float(np.mean(f1_w)),
        "precision_macro_mean": float(np.mean(p_m)),
        "recall_macro_mean": float(np.mean(r_m)),
        "f1_macro_mean": float(np.mean(f1_m)),
        "confusion_matrices": [cm.tolist() for cm in cms],
    }
