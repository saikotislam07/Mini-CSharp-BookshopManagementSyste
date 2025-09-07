from typing import Tuple
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import ADASYN
from imblearn.pipeline import Pipeline as ImbPipeline

def build_stacking_class_weight() -> Pipeline:
    base = [
        ("rf", RandomForestClassifier(n_estimators=300, class_weight="balanced", random_state=42)),
        ("dt", DecisionTreeClassifier(class_weight="balanced", random_state=42)),
        ("lr", LogisticRegression(max_iter=1000, class_weight="balanced", n_jobs=None))
    ]
    meta = LogisticRegression(max_iter=1000, class_weight="balanced")
    stack = StackingClassifier(estimators=base, final_estimator=meta, passthrough=False, n_jobs=None)
    pipe = Pipeline([("clf", stack)])
    return pipe

def build_stacking_adasyn() -> ImbPipeline:
    base = [
        ("rf", RandomForestClassifier(n_estimators=300, random_state=42)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("lr", LogisticRegression(max_iter=1000, n_jobs=None))
    ]
    meta = LogisticRegression(max_iter=1000)
    stack = StackingClassifier(estimators=base, final_estimator=meta, passthrough=False, n_jobs=None)
    pipe = ImbPipeline([("adasyn", ADASYN(random_state=42)), ("clf", stack)])
    return pipe
