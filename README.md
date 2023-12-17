# NULL HYPOTHESIS AND ALTERNATE HYPOTHESIS
 
## Title: Detecting Anomalies in Student Test Scores

### Problem Statement:

A local educational institution wants to ensure the consistency of grading in a particular subject. To verify this, they collected a dataset of student test scores in a CSV file named 'test.csv'. The institution's expected mean score for this subject is 70.

## Introduction

This repository contains Python code demonstrating anomaly detection using a one-sample t-test. The code reads data from a CSV file, assumes a null hypothesis regarding the mean of the dataset, performs a one-sample t-test, and identifies potential anomalies based on a significance level.

## Contents

- `anomaly_detection.py`: Python script that performs anomaly detection using a one-sample t-test on student marks data.
- `test.csv`: Sample CSV file containing student names and marks.

## Code Explanation

- `import pandas as pd`: Imports the pandas library for data manipulation.
- `from scipy.stats import ttest_1samp`: Imports the one-sample t-test function.
- `file_path = 'test.csv'`: Specifies the path to the CSV file.
- `data = pd.read_csv(file_path)`: Reads the CSV file into a pandas DataFrame.
- `marks_data = data['marks']`: Extracts the 'marks' column from the DataFrame.
- `expected_mean = 70`: Assumed expected mean for the null hypothesis.
- `t_statistic, p_value = ttest_1samp(marks_data, expected_mean)`: Performs a one-sample t-test.
- `alpha = 0.05`: Significance level for hypothesis testing.
- If `p_value < alpha`:
    - Identifies potential anomalies based on the threshold.
    - Flags anomalies in the dataset.
- Else:
    - Indicates no significant evidence to reject the null hypothesis.

## Modifications

- Modify `test.csv`: Replace the provided CSV file with your own dataset.
- Adjust `expected_mean` and `alpha` as needed for your hypothesis testing.
