from pathlib import Path

import pandas as pd


def get_data_paths(base_path: Path | str = ".") -> dict[str, Path]:
    """Build canonical project data paths from a base directory."""
    root = Path(base_path)
    return {
        "train": root / "train_images" / "train_images",
        "test": root / "leaderboard_test_data" / "leaderboard_test_data",
        "holdout": root / "leaderboard_holdout_data" / "leaderboard_holdout_data",
        "sample_sub": root / "SampleSubmission.csv",
        "labels": root / "traininglabels.csv",
    }


def load_label_data(base_path: Path | str = ".") -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load training labels and sample submission files."""
    paths = get_data_paths(base_path)
    df = pd.read_csv(paths["labels"])
    df_sample = pd.read_csv(paths["sample_sub"])
    return df, df_sample
