from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import poisson


def main() -> None:
    """Analyse background-radiation measurements."""

    repository_root = Path(__file__).resolve().parent.parent
    data_file = repository_root / "data" / "background_counts.csv"
    output_file = repository_root / "figures" / "experimental_vs_poisson.png"

    if not data_file.exists():
        raise FileNotFoundError(f"Dataset not found: {data_file}")

    data = pd.read_csv(data_file)

    required_columns = {"trial", "background_count"}
    missing_columns = required_columns.difference(data.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    counts = pd.to_numeric(
        data["background_count"],
        errors="raise"
    )

    mean_count = counts.mean()
    sample_variance = counts.var(ddof=1)
    standard_deviation = counts.std(ddof=1)
    variance_mean_ratio = sample_variance / mean_count

    print(f"Number of observations: {len(counts)}")
    print(f"Mean count: {mean_count:.2f}")
    print(f"Sample variance: {sample_variance:.2f}")
    print(f"Standard deviation: {standard_deviation:.2f}")
    print(f"Variance-to-mean ratio: {variance_mean_ratio:.3f}")
    print(f"Minimum count: {counts.min()}")
    print(f"Maximum count: {counts.max()}")

    minimum = int(counts.min())
    maximum = int(counts.max())

    x_values = np.arange(minimum, maximum + 1)
    bin_edges = np.arange(minimum - 0.5, maximum + 1.5, 1)

    plt.figure(figsize=(10, 6))

    plt.hist(
        counts,
        bins=bin_edges,
        density=True,
        alpha=0.6,
        edgecolor="black",
        label="Experimental data",
    )

    plt.plot(
        x_values,
        poisson.pmf(x_values, mean_count),
        marker="o",
        linestyle="--",
        label=f"Poisson distribution (mean={mean_count:.2f})",
    )

    plt.title(
        "Background Radiation: Experimental Counts vs Poisson Distribution"
    )
    plt.xlabel("Counts per 60-second interval")
    plt.ylabel("Probability")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    output_file.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file, dpi=300)

    print(f"Graph saved to: {output_file}")


if __name__ == "__main__":
    main()
