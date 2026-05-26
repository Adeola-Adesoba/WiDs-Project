# Repository Map, Risk Review, and 30-Minute Cleanup Plan

## Current Repository Map

Top-level files:

1. `WiDS project - Keras.ipynb`
   - Keras-based experiment notebook.
   - 11 code cells, no markdown narrative cells.
2. `WiDS attempt 1-checkpoint.ipynb`
   - Earlier experiment checkpoint notebook.
   - 12 code cells, no markdown narrative cells.
3. `WiDS attempt 3-checkpoint.ipynb`
   - Another experiment checkpoint notebook.
   - 10 code cells, no markdown narrative cells.

Observed characteristics across notebooks:
- Python kernel metadata indicates Python `3.6.5`.
- Data file references include `traininglabels.csv` and `SampleSubmission.csv`.
- Mixed libraries: scikit-learn, matplotlib, scipy, and keras.

## Key Risks

1. **Reproducibility risk (high)**
   - Notebooks contain execution outputs and non-sequential historic execution counts.
   - No environment lock file (`requirements.txt`, `environment.yml`, or `pyproject.toml`) exists.

2. **Maintainability risk (high)**
   - Repository currently has no README, no project structure, and no modular Python package/scripts.
   - Work exists only in notebooks, making review and reuse difficult.

3. **Legacy runtime risk (medium-high)**
   - Notebook metadata points to Python `3.6.5`, now long past end-of-life.
   - Likely incompatibilities with modern package versions.

4. **Version-control hygiene risk (medium)**
   - Checkpoint notebooks are committed (`*-checkpoint.ipynb`).
   - Outputs in notebooks can create noisy diffs and merge conflicts.

5. **Experiment tracking risk (medium)**
   - No explicit run configuration, seed policy, or artifact naming conventions.
   - Difficult to compare attempts or reproduce best score.

## 30-Minute Cleanup Plan (No Model Changes)

> Scope explicitly excludes any ML model architecture/algorithm changes.

### Minute 0–10: Documentation and structure baseline

1. Add `README.md` with:
   - Project purpose.
   - Expected input files (`traininglabels.csv`, `SampleSubmission.csv`).
   - Quick-start steps.
2. Add `CONTRIBUTING.md` lightweight workflow:
   - Notebook naming convention.
   - Output-clearing before commit.
3. Create folders:
   - `notebooks/` (active notebooks)
   - `data/` (local, gitignored datasets)
   - `artifacts/` (predictions/models, gitignored)

### Minute 10–20: Notebook and git hygiene

1. Move notebooks into `notebooks/` with clean names:
   - `wids_keras_baseline.ipynb`
   - `wids_attempt_01.ipynb`
   - `wids_attempt_03.ipynb`
2. Strip cell outputs from committed notebooks.
3. Add/update `.gitignore`:
   - `.ipynb_checkpoints/`
   - `data/*` (except placeholders like `.gitkeep`)
   - `artifacts/*` (except placeholders)

### Minute 20–30: Reproducibility guardrails

1. Add `requirements.txt` (or `environment.yml`) pinning currently used package majors.
2. Add `scripts/validate_notebooks.py` (simple check):
   - Ensures no cell outputs.
   - Flags checkpoint files.
3. Add a one-command pre-commit check in README:
   - `python scripts/validate_notebooks.py`

## Suggested “Definition of Done” for this cleanup

- Repo has clear README and folder structure.
- No checkpoint notebooks tracked.
- Notebook outputs removed before commit.
- Dependencies declared.
- Basic validation script exists and passes.
