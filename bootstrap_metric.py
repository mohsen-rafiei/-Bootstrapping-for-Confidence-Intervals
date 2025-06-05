# Bootstrapping Confidence Interval for UX Metrics
# Author: Abigail Page-Rumsey using Gemini 2.5 Pro, adapted from R script by Mohsen Rafiei
# Description: General-purpose script for computing bootstrapped confidence intervals
#              for any numeric UX measure (e.g., SUS, satisfaction, trust, task time)

import numpy as np
import matplotlib.pyplot as plt
import statistics # For mean, median, stdev, etc.

# USER INPUT: Replace this with your own numeric data
metric_scores = np.array([82.5, 90, 72.5, 77.5, 85, 70, 65, 80, 92.5, 75])

# Define the statistic of interest (mean, median, etc.)
# You can use: np.mean, np.median, np.std, statistics.mean, statistics.median, statistics.stdev
statistic_function = np.mean  # Change to np.median, np.std, etc. if needed

# Bootstrap parameters
n_iterations = 10000
boot_stats = np.zeros(n_iterations) # Initialize an array to store bootstrapped statistics

# Perform bootstrapping
np.random.seed(123)  # for reproducibility
n_scores = len(metric_scores)

for i in range(n_iterations):
    # Sample with replacement from the original metric_scores
    # The size of the sample is the same as the original data
    sample_scores = np.random.choice(metric_scores, size=n_scores, replace=True)
    boot_stats[i] = statistic_function(sample_scores)

# Calculate confidence interval (95%)
# We use the 2.5th and 97.5th percentiles for a 95% CI
ci_lower = np.percentile(boot_stats, 2.5)
ci_upper = np.percentile(boot_stats, 97.5)
observed_stat = statistic_function(metric_scores)

# Print results
print(f"Observed Estimate: {observed_stat:.2f}")
print(f"95% Confidence Interval: [{ci_lower:.2f}, {ci_upper:.2f}]")

# Plot the bootstrap distribution
plt.figure(figsize=(10, 6)) # Set the figure size for better readability
plt.hist(boot_stats, bins=50, color="skyblue", edgecolor="black", alpha=0.7)

# Add vertical lines for the confidence interval and observed statistic
plt.axvline(ci_lower, color="red", linestyle="dashed", linewidth=1.5, label=f'95% CI Lower: {ci_lower:.2f}')
plt.axvline(ci_upper, color="red", linestyle="dashed", linewidth=1.5, label=f'95% CI Upper: {ci_upper:.2f}')
plt.axvline(observed_stat, color="green", linestyle="solid", linewidth=1.5, label=f'Observed: {observed_stat:.2f}')

# Add labels and title
plt.title("Bootstrapped Confidence Interval Distribution", fontsize=16)
plt.xlabel("Bootstrapped Estimates", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.legend() # Show the legend
plt.grid(axis='y', alpha=0.75) # Add a light grid for the y-axis
plt.style.use('seaborn-v0_8-whitegrid') # Using a seaborn style for a nicer look

# Show the plot
plt.show()