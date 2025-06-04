
# Bootstrapped Confidence Interval for SUS Scores

This project demonstrates how to calculate a 95% confidence interval for System Usability Scale (SUS) scores using bootstrapping in R. It's designed for UX researchers working with small sample sizes or non-normal data.

## Files

- `bootstrap_sus.R`: The main R script that performs the analysis.
- `README.md`: Instructions and context.

## Instructions

1. Open R or RStudio.
2. Load the script `bootstrap_sus.R`.
3. Run the script.

It will:
- Resample your SUS scores 10,000 times using bootstrapping
- Calculate the average SUS score
- Generate a 95% confidence interval around that mean
- Plot the distribution of bootstrapped means with CI lines

## Why Use This?

Bootstrapping is ideal for UX research scenarios with small sample sizes or when assumptions of normality don't hold. It gives you robust estimates of variability without requiring large datasets.

## Output

The script will print:
- Mean SUS score
- 95% confidence interval

It also generates a histogram showing the bootstrapped mean distribution with CI boundaries.

## License

MIT License
