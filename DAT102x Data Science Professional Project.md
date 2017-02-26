# DAT102x: Data Science Professional Project

#### Update: 26-Feb-2017
## Kick Off

#### The complete map for the current model:
![complete model](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/All%20Process%20View.png)

Basically, two part: preprocessing + modeling. While modeling part contains several experiment on:
* SMOTE percentage (100% vs. 200%)
* Boosted deision tree vs. Deicision Forest (two best performed models)
* PCA vs. No PCA

#### The pre-processing part:
![preprocessing](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/Pre-processing.png)

* Removes col with too many NaNs: Months since last delinquent, Years in current job
* Removes col that prove useless using "Permutation Feature Importance": Bankrupcies & Tax Liens
* Removes Identity cols: Customer ID, Loan ID

* Invalid value transformations: remove special chracters($), nan notation(!VALUE, 99999999), typo error(Credit Score)
* Conversion of datatypes: string -> Categorical/Numerical
* Remove Nans (Credit Score, Annual Income)
* Remove Duplicates
* Mapping to reduce categorical features (Purpose)

* Normalization

#### The left branch: Model Comparison
![left branch](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/left_branch_Model_Exploration.png)

Observation:
* Boosted Decision Tree generally performed better.
* Tuning Hyperparameter:
  * Random Sweep gives over-fitted training model
  * Sweep thorugh entire grid give perfect model for the metric choose (say choose Recall), but tend to generalize poorly.
  
![left model evaluation](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/left_model_evaluation.jpg)

#### The right branch: SMOTE change & PCA
![right branch](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/right_branch_Vary_SMOTE_and_PCA.png)

Observations:
* SMOTE percentage decreased from 200% to 100%, without PCA version generalized better
* PCA configured 4 features out of 8, and the accuracy score is ridiculous.

![right model evaluation](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT102x%20Data%20Science%20Professional%20Project/right_model_evaluation.jpg)


<hr>
### What to do Next
When competition is launched, deploy as web service to check how much overfitted the model is and change accordingly.
Parameters to tune include:
* Decision Tree Hyperparameters (Parameter range (train model) + parameter sweeping mode (Tune model hyperparameter))
* PCA: number of feature space
* SMOTE module: how many percentage to choose
* Split Data percentage
* CROSS-VALIDATION to see the generalization of model

[THIS LINK](http://money.usnews.com/money/personal-finance/articles/2016-03-17/beyond-credit-scores-7-factors-that-affect-a-loan-application) shows the general guidelines for accessing a person's credibility for loan application. Some take away may be:
* Debt-to-income ratio: combine "annual income" with "monthly debt"
* Employment history: may think about reverting back "years of current work"
* Recent payment history: "month since last delinquency" could be crucial, but should think about how to tackle the NaNs.



