# Bootstrapped Confidence Intervals for UX Metrics

This project demonstrates how to compute a 95% confidence interval using bootstrapping in R. While the example uses System Usability Scale (SUS) scores, the method can be applied to any numeric UX metric including task completion times, NPS scores, trust ratings, or average satisfaction levels. This technique is especially useful in small-sample UX studies or when your data deviate from normality.

## Project Files

- `bootstrap_metric.R`: The main R script that implements bootstrapping and plotting.
- `README.md`: This documentation file.

## Method Overview

Bootstrapping is a resampling-based method for estimating the sampling distribution of a statistic, such as the mean or median. It involves repeatedly sampling with replacement from your observed data and computing the desired statistic for each resample. This results in a distribution of bootstrap estimates, which can then be used to calculate confidence intervals empirically, without relying on normality assumptions.

This method is well-suited to UX research because user data often violate classical statistical assumptions. Bootstrapping provides a robust, flexible alternative that works well with small samples, ordinal or skewed data, and unknown distributions.

## Instructions

1. Ensure R (or RStudio) is installed on your system.
2. Open the `bootstrap_metric.R` file.
3. Replace the example vector with your own numeric data.
4. Adjust the statistic if desired (e.g., mean, median).
5. Run the script.

The script performs the following:
- Accepts a numeric vector of scores.
- Executes 10,000 bootstrap resamples (with replacement).
- Calculates the statistic (by default, the mean) for each resample.
- Computes the 95% confidence interval using the 2.5th and 97.5th percentiles.
- Generates a histogram showing the bootstrapped distribution and CI bounds.

## Customization

To adapt the script for your needs:
- Replace the `metric_scores` vector with your own data.
- Modify the `statistic_function` to use `median`, `sd`, or any custom function.
- Adjust the number of bootstrap iterations or confidence level as needed.

## Statistical Details

- **Statistic of Interest**: Default is the mean, but can be any function of the data.
- **Bootstrap Iterations**: 10,000 by default.
- **CI Method**: Percentile-based confidence interval.
- **Assumptions**: Only that the data are independently and identically distributed.
- **Interpretation**: The 95% confidence interval provides a plausible range for the true population parameter, based on the observed sample.

## Output

- Printed output includes:
  - Observed estimate of the metric
  - Lower and upper bounds of the 95% confidence interval
- A histogram of the bootstrapped estimates with CI boundaries is generated for visual interpretation.

## Use Cases in UX

This method is useful for estimating confidence intervals for:
- SUS or other usability scores
- Average satisfaction or trust ratings
- Task success rates or completion times
- Likert-based scale summaries
- Behavioral metrics collected during usability testing

## License
Developed by Mohsen Rafiei, Ph.D.

This project is released under the MIT License. Feel free to modify and reuse the code with appropriate attribution.
