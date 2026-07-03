from bottradenc.features.feature_builder import FeatureBuilder


def test_ratio():
    assert FeatureBuilder.ratio(2000, 100000) == 0.02


def test_e_pct():
    assert round(FeatureBuilder.e_pct(1.05, 1.00), 2) == 5.00
