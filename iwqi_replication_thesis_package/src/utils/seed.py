import os, random, numpy as np

def set_global_seed(seed: int = 42):
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    try:
        import sklearn
        # scikit-learn uses numpy's RNG for most ops; set in CV splits as needed
    except Exception:
        pass
