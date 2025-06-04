
# Bootstrapping Confidence Interval for UX Metrics
# Author: Mohsen Rafiei
# Description: General-purpose script for computing bootstrapped confidence intervals
#              for any numeric UX measure (e.g., SUS, satisfaction, trust, task time)

# Load necessary library
if (!require(ggplot2)) install.packages("ggplot2", dependencies = TRUE)
library(ggplot2)

# USER INPUT: Replace this with your own numeric data
metric_scores <- c(82.5, 90, 72.5, 77.5, 85, 70, 65, 80, 92.5, 75)

# Define the statistic of interest (mean, median, etc.)
statistic_function <- mean  # Change to median, sd, etc. if needed

# Bootstrap parameters
n_iterations <- 10000
boot_stats <- numeric(n_iterations)

# Perform bootstrapping
set.seed(123)  # for reproducibility
for (i in 1:n_iterations) {
  sample_scores <- sample(metric_scores, size = length(metric_scores), replace = TRUE)
  boot_stats[i] <- statistic_function(sample_scores)
}

# Calculate confidence interval
ci_lower <- quantile(boot_stats, 0.025)
ci_upper <- quantile(boot_stats, 0.975)
observed_stat <- statistic_function(metric_scores)

# Print results
cat("Observed Estimate:", round(observed_stat, 2), "\n")
cat("95% Confidence Interval: [", round(ci_lower, 2), ",", round(ci_upper, 2), "]\n")

# Plot the bootstrap distribution
df <- data.frame(boot_stats = boot_stats)
ggplot(df, aes(x = boot_stats)) +
  geom_histogram(bins = 50, fill = "skyblue", color = "black") +
  geom_vline(xintercept = ci_lower, color = "red", linetype = "dashed") +
  geom_vline(xintercept = ci_upper, color = "red", linetype = "dashed") +
  labs(
    title = "Bootstrapped Confidence Interval",
    x = "Bootstrapped Estimates",
    y = "Frequency"
  ) +
  theme_minimal()
