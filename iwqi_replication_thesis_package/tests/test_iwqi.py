from src.iwqi import WEIGHTS, mgL_to_meqL_ca, mgL_to_meqL_mg, mgL_to_meqL_na, mgL_to_meqL_cl, mgL_to_meqL_hco3

def test_weight_sum():
    assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9

def test_conversions():
    assert abs(mgL_to_meqL_ca(20.0) - 1.0) < 1e-9
    assert abs(mgL_to_meqL_mg(12.15) - 1.0) < 1e-9
    assert abs(mgL_to_meqL_na(22.99) - 1.0) < 1e-6
    assert abs(mgL_to_meqL_cl(35.45) - 1.0) < 1e-6
    assert abs(mgL_to_meqL_hco3(61.02) - 1.0) < 1e-6
