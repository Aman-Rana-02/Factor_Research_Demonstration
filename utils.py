import pandas as pd
import matplotlib.pyplot as plt

def plot_actual_vs_predicted(df, predicted, actual, bins=30, extreme_upper=1, extreme_lower=-1):
    # Scatter plot of predicted vs actual returns
    if extreme_upper and extreme_lower:
        df = df[(df[predicted] > extreme_lower) & (df[predicted] < extreme_upper)]
        df = df[(df[actual] > extreme_lower) & (df[actual] < extreme_upper)]

    num_buckets = bins

    # Create quantile-based buckets
    df['bucket'] = pd.qcut(df[predicted], num_buckets, labels=False)

    # Calculate the mean predicted and actual returns for each bucket
    bucket_means = df.groupby('bucket')[[predicted, actual]].mean()

    # Scatter plot of bucket means
    plt.scatter(bucket_means[predicted], bucket_means[actual], color='orange', label='Bucket Means')

    # Add a 45-degree line for reference
    min_val = min(bucket_means[predicted].min(), bucket_means[actual].min())
    max_val = max(bucket_means[predicted].max(), bucket_means[actual].max())
    plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='45-degree line')

    # Labeling the plot
    plt.xlabel('Predicted Returns')
    plt.ylabel('Actual Returns')
    plt.title('Predicted vs Actual Returns with Buckets and 45-degree Line')
    plt.legend()
    plt.show()

def plot_residuals(df, predicted, actual, bins=30, extreme_upper=1, extreme_lower=-1):
    # Scatter plot of residuals
    if extreme_upper and extreme_lower:
        df = df[(df[predicted] > extreme_lower) & (df[predicted] < extreme_upper)]
        df = df[(df[actual] > extreme_lower) & (df[actual] < extreme_upper)]

    num_buckets = bins

    # Create quantile-based buckets
    df['bucket'] = pd.qcut(df[predicted], num_buckets, labels=False)

    # Calculate the mean residuals for each bucket
    df['residual'] = df[actual] - df[predicted]
    bucket_means = df.groupby('bucket')['residual'].mean()

    # Scatter plot of bucket means
    plt.scatter(bucket_means.index, bucket_means, color='orange', label='Bucket Means')

    # Add a horizontal line at y=0 for reference
    plt.axhline(y=0, color='red', linestyle='--', label='Zero Residuals')

    # Labeling the plot
    plt.xlabel('Predicted Returns')
    plt.ylabel('Mean Residuals')
    plt.title('Mean Residuals vs Predicted Returns with Buckets and Zero Residuals Line')
    plt.legend()
    plt.show()
