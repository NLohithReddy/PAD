import pandas as pd
from scipy.stats import ttest_1samp

file_path = 'test.csv'
data = pd.read_csv(file_path)
marks_data = data['marks']
expected_mean = 70
alternate_hypothesis = "The mean of the marks is not equal to the expected mean (70)."

t_statistic, p_value = ttest_1samp(marks_data, expected_mean)
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
else:
    print("No significant evidence to reject the null hypothesis.")
