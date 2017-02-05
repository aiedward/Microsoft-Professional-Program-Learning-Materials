# DS101X: Statistical Thinking for Data Science and Analytics

[Course Syllabus](https://d37djvu3ytnwxt.cloudfront.net/assets/courseware/v1/33ad7c92b39bbaea35b505415788ea87/asset-v1:ColumbiaX+DS101X+1T2016+type@asset+block/DS101X_Course_Syllabus.pdf)

## Week 1: Introduction to Data Science

### Introduction to Data Science
What is Data Science?<br>
What questions can Data Science answer?<br>
Why is there an explosion of data?<br>
What role does data visualization play in Data Science?<br>
How did you become interested in Data Science?<br>
What do you predict will happen in Data Science in 5 years?<br>
What are the most important skills for a Data Scientist?<br>
What should a non-Data Scientist know about Data Science?<br>
What should a non-Data Scientist know about Data Science?<br>


## Week 2: Statistics and Probability I

Statistical Thinking for Data Science<br>
Numerical Data 1 Simple Visualization and Summaries<br>
Numerical Data 2 Simple Visualization and Summaries<br>
### Numerical Data 3 Association
![association and causation](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/association%20and%20causation.jpg)

### Data Collection - Sampling
![bias in samples estimate](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/bias%20in%20sample%20estimate.PNG)

### Introduction to Probability
### Statistical Inference - Confidence Intervals
### Statistical Inference - Significance tests

[But P-value is intrinsically cofusing!](http://www.nature.com/news/scientific-method-statistical-errors-1.14700#/cause)
This article suggested the following:
> Most scientists would look at his original P value of 0.01 and say that there was just a 1% chance of his result being a false alarm. But they would be wrong. The P value cannot say this: all it can do is summarize the data assuming a specific null hypothesis. It cannot work backwards and make statements about the underlying reality.

> According to one widely used calculation5, a P value of 0.01 corresponds to a false-alarm probability of at least 11%, depending on the underlying probability that there is a true effect; a P value of 0.05 raises that chance to at least 29%. So Motyl's finding had a greater than one in ten chance of being a false alarm. Likewise, the probability of replicating his original result was not 99%, as most would assume, but something closer to 73% — or only 50%, if he wanted another 'very significant' result6, 7. In other words, his inability to replicate the result was about as surprising as if he had called heads on a coin toss and it had come up tails.

![P-value graph](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/p-graphic.jpg)

### Status of Current Observational Health Studies
### Statistical Terms Explained

Some Assumptions: <br>
- No measurement error;
- No selection bias;
- No unmeasured confounders.

### Unknown Characteristics of Observational Health Studies
### Lessons Learnt from OMOP Experiments
### P-value Calibration

![Empirical Calibration of P value](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/Empirical%20Calibration%20of%20P%20value.png)

Safe below the dased line.

## Week 3: Statistics and Probability II

### Conditional Probability
### Bayes' Formula

![conditional prob and Bayes formula](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/conditional%20prob%20and%20Bayes%20formula.jpg)

### Studying Association: Two-way Table
### Studying Association: Chi-square Test of Independence

![chi-square formula](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/chi-square.png)

### Studying Association: One-way Analysis of Variance
![source of variation](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/source%20of%20variation.png)

### Regression Analysis 1 and 2
### Regression Analysis 3 and 4
### Regression Analysis 4 and Concluding Remarks

![regression variance](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/Regression%20and%20variance.jpg)

### Types of Data Analytics

![text analytics intro](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/text%20analytics%20intro.jpg)

### Clustering Text
![text cluster procedure](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/text%20cluster%20procedure.jpg)

* Preprocessing:
  * Stopwords removing
  * Stemming
* Simple Metrics
  * Word count
  * Entity matching
  * Collocation
* Clustering
  * Summerize content
  * Create feature for supervised methods
  * Labeling (sometimes labels are given, other times should be inferred)
* Clustering algorithm
  * K-Means
* Vectorization
  * Normalize count on TF-IDF
  * Cosine Similarity<br>
 

### Topic Modeling

![Topic Modeling](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/Topic%20Modeling.jpg)

#### Mixed Membership Models
> Latent Dirichlet Allocation

Basically, it is a **Dirichlet** distribution of **topic over words** and **documents over topics**; and **Multinomial** distribution of **words over topics**.

Some useful pictures for illustration.

![pic1](http://www.karinabunyik.com/content/images/2014/Oct/Screen-Shot-2014-10-17-at-15-32-05.png)
![pic2](https://cdn-images-1.medium.com/max/800/0*II7wZlKViCt4ssBm.png)
![pic3](http://salsahpc.indiana.edu/b649proj/images/proj3_LDA%20structure.png)
![pic4](https://mollermara.com/blog/lda/lda-tikz.png)


### Metrics for Label Description

![Metrics for Label Description](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/Metrics%20for%20Label%20Description.jpg)


> PMI (Pointwise Multual Information)

> MI (Mutual Information): PMI averaged over all events

## Week 4: Exploratory Data Analysis and Visualization
Graphs Are Comparisons<br>
Use Data To Answer Questions<br>
A Case Example<br>
Decision Making Process of Data Visualization 1<br>
Decision Making Process of Data Visualization 2<br>
Decision Making Process Main Worked Example<br>
Why Visualize Data Worked Example 1<br>
Why Visualize Data Worked Example 2<br>
Dashboards<br>
Dashboards Worked Example 1<br>
Dashboards Worked Example 2<br>

## Week 5: Introduction to Bayesian Modeling

Introduction to Bayesian Modeling<br>
Probability Calibration<br>
Probability As Measurement of Uncertainty<br>

### Bayesian Inference

![bayesian inference](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/bayesian%20inference.jpg)

How To Use Prior Information<br>
### Bayesian Modeling in Practice
![Bayesian Modeling in Practice](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DS101X%20Statistical%20Thinking%20for%20Data%20Science%20and%20Analytics/Bayesian%20Modeling%20in%20Practice.jpg)


Business Applications in Bayesian Statistics Introduction<br>
Data Collection and Model Building 1<br>
Data Collection and Model Building 2<br>
Model Building Review<br>
Model Insights 1<br>
Model Insights 2<br>
Example Modeling Museum Membership Renewal<br>
Example Modeling User Behavior on a Deals Website<br>
