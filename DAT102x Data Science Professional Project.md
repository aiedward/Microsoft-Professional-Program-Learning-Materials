# Objective
This project analyze the dataset from a global retailer, utilizing personal particulars of customer to predict:
1. Whether they are likely to be a bike buyer
2. Their Average Monthly Spend with the company

### Report: [link](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/report%20ver1.pdf)

### A concise description on dataset:
* AWCustomers.zip: information of customer
  * AWSales.csv: Sales info (y: labels)
  * AWCustomers.csv: Customer info (X: attributes)
* AWTest.zip: test data
  * AWTest-Classification.csv
  * AWTest-Regression.csv

### A concise description on python code:
* [pre-processing.py](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/pre-processing.py): read from raw customer data and drop duplicates
* [data-wrangling.py](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/data-wrangling.py):
  * Data transformation
  * Visualizations
  * Question answers
* [classification-model.py](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/classification-model.py):
  * Categorize data
  * Build Classification Model
* [regression-model.py](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/regression-model.py):
  * Categorize data
  * Build Regression Model

### Azure Work: [link](https://studio.azureml.net/Home/ViewWorkspaceCached/119ce0ee2f2d4e61b8ca08c17d603119?#Workspaces/Experiments/Experiment/119ce0ee2f2d4e61b8ca08c17d603119.f-id.1a0b8989efb74a10b6f595698a8021ea/ViewExperiment)

## How to inteprete Negative Feature Importance
A negative score is returned when a random permutation of a feature’s values results in a better performance metric (higher accuracy or a lower error, etc..) compared to the performance before a permutation is applied.

In general, features with higher importance scores are more sensitive to random shuffling of their values, which means they are more ‘important’ for prediction. Beware that the shuffling is performed for one feature at a time, and although a feature might seem unnecessary or less important because of its low (or negative) importance score, it could be the case that it is correlated to other features that can still produce a ‘good’ performance result.
