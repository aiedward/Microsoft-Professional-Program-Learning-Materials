# Data Science Orientation

### Module 2: DS Fundamentals
What can data tell: descriptive, associative, comparative, predictive
What Excel can bring us simple visualization: Conditional Formatting -> Color Scales; Insert -> Line; PivotTable & PivotChart

<hr/>
### Module 3: Basic Statistics
* standard error (SE) = sample standard variance / sqrt(sample size)
* Hypothesis Testing: <br/>
  **T-test** (df=n-1) 
  
  ![T-test](https://wikimedia.org/api/rest_v1/media/math/render/svg/1063f91f450e9fd0094a38f1856eb11bd201d232)<br/>
  **Two-Sample T-Tests** (df=n1+n2-2)
  Equal or unequal sample sizes, equal variance
  
  ![Two-Sample T-Tests 1](https://wikimedia.org/api/rest_v1/media/math/render/svg/faf70034d0a3a686080b98b32f64f2cc62a5dbad)<br/>
    Equal sample sizes, equal variance
    
  ![Two-Sample T-Tests 2](https://wikimedia.org/api/rest_v1/media/math/render/svg/cad0574bf2031d40d0194bfbe427567367aab4a8)<br/>
  **Paired T-Tests** (df=n-1)<br/>
    When the samples are dependent, compare current values with historical values, or compare experimental values with control
    
  ![Paired T-Tests](https://wikimedia.org/api/rest_v1/media/math/render/svg/18eb62b7eb006088cfff7c9cbc58b718cf8dbd51)<br/>

What Excel can bring us for statistical analysis:
  1. Option -> Add-in -> Analysis ToolPack + VBA Pack
  2. Data -> Analysis -> Data Analysis -> Descriptive Statistics/Correlation/t-Test/ANOVA(Analysis of variance)/Regression
  3. Formula: Z.TEST(array, x, [sigma])
  
#### Kurtosis & Skewness
Two other measures provide additional information about the shape of the distribution and how closely it approximates a normal distribution:
- Kurtosis is a measure of peakedness. Is the distribution tall and narrow, or is it short and flat?
- Skewness is a measure of the symmetry of the data. The skewness value indicates the direction of the tail. If it is positive, the distribution is right skewed; if negative, the distribution is left skewed. A normal distribution has a skew of 0.

#### Measures of Association: Correlation
Correlations measure the strength of the relationship, or association, between two variables. One common misinterpretation is that correlations imply causation, but they do not. Correlations are **not tied to causation**.

![Corr Formula](http://www.stat.yale.edu/Courses/1997-98/101/cor.gif)

How to Interpret a Correlation Coefficient: <br>
The closer the absolute value is to 1, the stronger the linear relationship. The closer to 0, the weaker the relationship. Because we almost always mean a **Pearson correlation**, which is measure of **linear association**, a correlation near 0 doesn’t necessarily mean that there is no relationship; it only means that the relationship is not linear (it could be curvilinear or logarithmic, for example).

  
#### SOME ANOVA FACTS
Analysis of variance (ANOVA) is used to simultaneously test for differences between the means of two or more independent groups (many sources state that the minimum is three, but it can be used with two although it should be noted that this is technically a t-test). In the case of ANOVA, group membership is the “treatment” condition (also known as the “independent variable”) and is a categorical variable. The outcome of interest (known as the “dependent variable” because the result ‘depends’ on group membership) must be a continuous variable.

A two-way ANOVA allows for the comparison of multiple treatment conditions on an outcome of interest. For example, Rosie may wonder if she sells more lemonade at the beach or the park based on temperature. Two-way ANOVA analysis allows you to test not only for main effects but also for interactions between levels of the various treatment conditions.

A **main effect** occurs when the effect of one treatment on the outcome variable is the same across all levels of the other treatments. An **interaction** occurs when the effect that a treatment has on the outcome differs at some level(s) of the other independent variable.

ANOVA is an **omnibus** test statistic, meaning that the result will tell if there is at least one significant mean difference, but it will not tell you where it is. To identify which groups are statistically different, you will need to run a post hoc analysis. There are several different types of post hoc analyses that can be performed. The most common are **Bonferroni, Fisher’s Least Squared Differences, and Tukey**. Regardless of the method selected, they all control for the possibility of capitalizing on chance when multiple t-tests are performed as described in the next section.

The outcome of this analysis is a **f-statistic**. Unlike the t-statistic distribution, which is normally distributed, however, the f-statistic distribution right skewed.<br/>
![ALT TEXT](http://www.statisticshowto.com/wp-content/uploads/2013/09/f-table.jpg)

<hr/>
Check out [THIS LINK](https://github.com/MicrosoftLearning/Data-Science-Orientation/raw/master/Data%20Science%20101%20Statistics%20Overview.pdf) for more insights of statistics.

Some distribution [Tables](http://documents.software.dell.com/Statistics/Textbook/Distribution-Tables).
