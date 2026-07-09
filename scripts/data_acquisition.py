"""
data_acquisition.py

AML Multi-Omics Biomarker Discovery

This script loads processed TCGA-LAML datasets used in this project.
"""

from pathlib import Path
import pandas as pd

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data directory
DATA_DIR = PROJECT_ROOT / "data" / "processed"


def load_expression_data():
    """Load gene expression matrix."""
    file = DATA_DIR / "expression_matrix.csv"
    expression = pd.read_csv(file, index_col=0)
    return expression


def load_methylation_data():
    """Load DNA methylation matrix."""
    file = DATA_DIR / "methylation_matrix.csv"
    methylation = pd.read_csv(file, index_col=0)
    return methylation


def main():

    expression = load_expression_data()
    methylation = load_methylation_data()

    print("=" * 60)
    print("AML Multi-Omics Biomarker Discovery")
    print("=" * 60)

    print(f"Expression matrix shape : {expression.shape}")
    print(f"Methylation matrix shape: {methylation.shape}")

    print("\nExpression genes:", expression.shape[0])
    print("Expression samples:", expression.shape[1])

    print("\nMethylation genes:", methylation.shape[0])
    print("Methylation samples:", methylation.shape[1])


if __name__ == "__main__":
    main()
