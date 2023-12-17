import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

file_path = 'test.csv'
data = pd.read_csv(file_path)
marks_data = data['marks']
expected_mean = 70
alternate_hypothesis = "The mean of the marks is not equal to the expected mean (70t_statistic, p_value = ttest_1samp(marks_data, expected_mean)
alpha = 0.05
if p_value < alpha:
    print("Null hypothesis rejected. There is significant evidence to support the alternate hypothesis:")
    print(alternate_hypothesis)
    anomaly_threshold = 2 * marks_data.std()
    anomalies = marks_data[abs(marks_data - expected_mean) > anomaly_threshold]
    print("Anomalies:")
    print(anomalies)
    data['is_anomaly'] = abs(data['marks'] - expected_mean) > anomaly_threshold
    print("\nData with Anomalies:")
    print(data)
    plt.figure(figsize=(8, 6))
    plt.scatter(data.index, data['marks'], label='Marks')
    plt.scatter(anomalies.index, anomalies, color='red', label='Anomalies')
    plt.axhline(y=expected_mean, color='green', linestyle='--', label='Expected Mean')
    plt.xlabel('Index')
    plt.ylabel('Marks')
    plt.title('Marks Data with Anomalies')
    plt.legend()
    plt.show()
else:
    print("No significant evidence to reject the null hypothesis.")
