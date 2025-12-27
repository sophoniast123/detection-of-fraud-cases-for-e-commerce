# Fraud Detection - Data Prep & Feature Engineering

This repository contains preprocessing, feature engineering, and utility scripts used for preparing fraud detection datasets and experiments.

**Project**
- **Purpose:** Prepare and clean transactional datasets, map geolocation data, handle class imbalance, and provide a preprocessing pipeline for model development.

**Datasets**
- Raw data files are in the `data/raw/` directory (e.g. `creditcard.csv`, `Fraud_Data.csv`).
- Processed outputs are written to `data/processed/`.

**Repository Structure**
- `src/`: Core preprocessing and utility modules (data loading, cleaning, feature engineering, geo IP mapping, imbalance handling, pipeline orchestration).
- `notebooks/`: EDA and preprocessing notebooks.
- `scripts/`: Helper scripts and entry points.
- `models/`: Trained model artifacts (not tracked here).
- `tests/`: Unit tests.
- `requirements.txt`: Python dependencies.

Key `src` modules:
- `src/data_loader.py`: dataset loading helpers.
- `src/data_cleaner.py`: cleaning and validation routines.
- `src/feature_engineer.py`: feature construction.
- `src/geo_ip_mapper.py`: IP-to-country mapping utilities.
- `src/imbalance_handler.py`: class-imbalance handling methods.
- `src/preprocessing_pipeline.py`: pipeline orchestration.

Setup

1. Create a Python environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. If you prefer conda:

```bash
conda create -n fraud-prep python=3.10
conda activate fraud-prep
pip install -r requirements.txt
```

Usage

- Run the preprocessing pipeline from `src/preprocessing_pipeline.py` or open `notebooks/data_preprocessing.ipynb` to run steps interactively.
- Example (script):

```powershell
python -m src.preprocessing_pipeline
```

Testing

- Run unit tests in `tests/` with `pytest`:

```powershell
pip install pytest
pytest -q
```

Development notes

- Keep raw data files in `data/raw/` and don't commit sensitive data.
- Add new data transforms to `src/feature_engineer.py` and wire them into `src/preprocessing_pipeline.py`.

License & Contributing

- Add a license file if you plan to open-source this repository.
- Open issues and pull requests for improvements.

Contact

- For questions about these scripts, check the docstrings in the `src/` modules or open an issue in the repo.
