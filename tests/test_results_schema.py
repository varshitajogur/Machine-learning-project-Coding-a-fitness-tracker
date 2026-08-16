from pathlib import Path
import csv

RESULTS = Path("results")

def test_result_files_exist():
    expected = [
        "classification_metrics.csv",
        "regression_metrics.csv",
        "clustering_metrics.csv",
        "model_comparison.csv",
        "feature_importance.csv",
        "error_analysis.csv",
        "confusion_matrix.csv",
    ]
    for name in expected:
        assert (RESULTS / name).exists()

def test_classification_columns_exist():
    with open(RESULTS / "classification_metrics.csv", newline="", encoding="utf-8") as f:
        cols = next(csv.reader(f))
    required = {"model", "accuracy", "precision_macro", "recall_macro", "f1_macro"}
    assert required.issubset(set(cols))
