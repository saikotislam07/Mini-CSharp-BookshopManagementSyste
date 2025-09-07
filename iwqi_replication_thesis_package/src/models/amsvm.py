from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

def build_amsvm_approx() -> Pipeline:
    # Approximation: class-weighted SVC with RBF kernel; true AMSVM uses apportioned margins.
    svc = SVC(kernel="rbf", gamma=0.1, C=0.1, class_weight="balanced", probability=True, random_state=42)
    return Pipeline([("clf", svc)])
