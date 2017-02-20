# DAT210x: Programming with Python for Data Science

## Course Map
* Big Picture
  * Data Science and Analysis
  * Machine Learning
  * The Possibilities
  * Dive Deeper
* Data and Features
  * Features Premiere
  * Determine Features
  * Manipulate Data
  * Feature Representation
  * Wrangling Data
  * Dive Deeper
*  Exploring Data
  * Visualizations
  * Basic Plots
  * Higher Dimensionality
  * Dive Deeper
* Transforming Data
  * PCA
  * Isomap
  * Pre-processing
  * Dive Deeper
* Data Modeling
  * Clustering
  * Spliting Data
  * K-nearest Neighbors
  * Regression
  * Dive Deeper
* Data Modeling II
  * SVC
  * Decision Trees
  * Random Forest
  * Dive Deeper
* Evaluating Data
  * Confusion
  * Cross Validation
  * Power Tuning
  * Dive Deeper



## Data and Features

### Features Premiere
There are many synonymous names for features. The background of the speaker, as well as the context of the conversation usually dictates which term is used:

* Attribute - Features are a quantitative attributes of the samples being observed
* Axis - Features are orthogonal axes of their feature space, if they are linearly independent
* Column - Features are represented as columns in your dataset
* Dimension - A dataset's features, grouped together can be treated as a n-dimensional coordinate space
* Input - Feature values are the input of data-driven, machine learning algorithms
* Predictor - Features used to predict other attributes are called predictors
* View - Each feature conveys a quantitative trait or perspective about the sample being observed
* Independent Variable - Autonomous features used to calculate others are like independent variables in algebraic equations

### Determine Features
### Manipulate Data
#### A Quick Peek
```python
df.head(10)
df.describe() # give statistical info
df.var() # variance
df.dtypes
```
* numeric-type: int32, float32, float64.
* date-type: datetime64, timedelta[ns].
* object-type: object (string), category

#### Column Indexing
One difference you'll notice is that some of the methods take in a list of parameters, e.g.: df[['recency']], df.loc[:, ['recency']], and df.iloc[:, [0]]. By passing in a list of parameters, you can select more than one column to slice. Please be aware that if you use this syntax, even if you only specify a single column, the data type that you'll get back is a dataframe as opposed to a series. This will be useful for you to know once you start machine learning, so be sure to take down that note.
```python

#
# Produces a series object:
>>> df.recency
>>> df['recency']
>>> df.loc[:, 'recency']
>>> df.iloc[:, 0]
>>> df.ix[:, 0]

0        10
1         6
2         7
3         9
4         2
5         6
Name: recency, dtype: int64

#
# Produces a dataframe object:
>>> df[['recency']]
>>> df.loc[:, ['recency']]
>>> df.iloc[:, [0]]

       recency
0           10
1            6
2            7
3            9
4            2
5            6

[64000 rows x 1 columns]

>>> df[0:2]
>>> df.iloc[0:2, :]
```
#### Boolean Indexing
```python
>>> df.recency < 7

0        False
1         True
2        False
3        False
4         True
5         True

Name: recency, dtype: bool

>>> df[ df.recency < 7 ]

       recency   history_segment  history  mens  womens   zip_code  newbie
1            6    3) $200 - $350   329.08     1       1      Rural       1
4            2      1) $0 - $100    45.34     1       0      Urban       0
5            6    2) $100 - $200   134.83     0       1  Surburban       0

>>> df[ (df.recency < 7) & (df.newbie == 0) ]

       recency history_segment  history  mens  womens   zip_code  newbie
4            2    1) $0 - $100    45.34     1       0      Urban       0
5            6  2) $100 - $200   134.83     0       1  Surburban       0
```

### Feature Representation

#### Textual Categorical-Features
If you have a categorical feature, the way to represent it in your dataset depends on if it's ordinal or nominal. For **ordinal features**, map the order as increasing integers in a single numeric feature. 
```python
>>> ordered_satisfaction = ['Very Unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
>>> df = pd.DataFrame({'satisfaction':['Mad', 'Happy', 'Unhappy', 'Neutral']})
>>> df.satisfaction = df.satisfaction.astype("category",
  ordered=True,
  categories=ordered_satisfaction
).cat.codes

>>> df
   satisfaction
0            -1
1             3
2             1
3             2
```
On the other hand, if your feature is **nominal** (and thus there is no obvious numeric ordering), then you have two options.
```python
# Data Source
>>> df = pd.DataFrame({'vertebrates':[
...  'Bird',
...  'Bird',
...  'Mammal',
...  'Fish',
...  'Amphibian',
...  'Reptile',
...  'Mammal',
... ]})


# Method 1)
>>> df['vertebrates'] = df.vertebrates.astype("category").cat.codes

>>> df
  vertebrates  vertebrates
0        Bird            1
1        Bird            1
2      Mammal            3
3        Fish            2
4   Amphibian            0
5     Reptile            4
6      Mammal            3

# Method 2)

>>> df = pd.get_dummies(df,columns=['vertebrates'])

>>> df
   vertebrates_Amphibian  vertebrates_Bird  vertebrates_Fish  \
0                    0.0               1.0               0.0   
1                    0.0               1.0               0.0   
2                    0.0               0.0               0.0   
3                    0.0               0.0               1.0   
4                    1.0               0.0               0.0   
5                    0.0               0.0               0.0   
6                    0.0               0.0               0.0   

   vertebrates_Mammal  vertebrates_Reptile  
0                 0.0                  0.0  
1                 0.0                  0.0  
2                 1.0                  0.0  
3                 0.0                  0.0  
4                 0.0                  0.0  
5                 0.0                  1.0  
6                 1.0                  0.0  
```
### NLP Tokenization
```python
>>> from sklearn.feature_extraction.text import CountVectorizer

>>> corpus = [
...  "Authman ran faster than Harry because he is an athlete.",
...  "Authman and Harry ran faster and faster.",
... ]

>>> bow = CountVectorizer()
>>> X = bow.fit_transform(corpus) # Sparse Matrix

>>> bow.get_feature_names()
['an', 'and', 'athlete', 'authman', 'because', 'faster', 'harry', 'he', 'is', 'ran', 'than']

>>> X.toarray()
[[1 0 1 1 1 1 1 1 1 1 1]
 [0 2 0 1 0 2 1 0 0 1 0]]
 ```
#### Graphical Features
 ```python
 # Uses the Image module (PIL)
from scipy import misc

# Load the image up
img = misc.imread('image.png')

# Is the image too big? Resample it down by an order of magnitude
img = img[::2, ::2]

# Scale colors from (0-255) to (0-1), then reshape to 1D array per pixel, e.g. grayscale
# If you had color images and wanted to preserve all color channels, use .reshape(-1,3)
X = (img / 255.0).reshape(-1)

# To-Do: Machine Learning with X!
#
```

#### Audio Features
```python
import scipy.io.wavfile as wavfile

sample_rate, audio_data = wavfile.read('sound.wav')
print audio_data

# To-Do: Machine Learning with audio_data!
#
```
### Wrangling Data

#### fill Nans
```pyhthon
df.my_feature.fillna( df.my_feature.mean() )
df.fillna(0)
df.fillna(method='ffill')  # fill the values forward
df.fillna(method='bfill')  # fill the values in reverse
df.fillna(limit=5)
df.interpolate(method='polynomial', order=2)
```
#### Drop Data
```python
# Dropna()
df = df.dropna(axis=0)  # remove any row with nans
df = df.dropna(axis=0, thresh=4) # Drop any row that has at least 4 NON-NaNs within it

# Drop row/column(s)
df = df.drop(labels=['Features', 'To', 'Delete'], axis=1) # Axis=1 for columns

# Drop Duplicates
df = df.drop_duplicates(subset=['Feature_1', 'Feature_2'])
df = df.reset_index(drop=True)

# Chain them together
df = df.dropna(axis=0, thresh=2).drop(labels=['ColA', axis=1]).drop_duplicates(subset=['ColB', 'ColC']).reset_index()
```
However there may be times where you want these operations to work in-place on the dataframe calling them, rather than returning a new dataframe. Pass **inplace=True** as a parameter to any of the above methods to get that working.

#### Change data types
If your data types don't look the way you expected them, explicitly convert them to the desired type using the .to_datetime(), .to_numeric(), and .to_timedelta() methods:
```python
>>> df.Date = pd.to_datetime(df.Date, errors='coerce')
array([7, 33, 27, 40, 22], dtype=int64)
>>> df.Height = pd.to_numeric(df.Height, errors='coerce')
7      1
22     5
27     1
33     2
40     2
dtype: int64

df[['height']] =df[['height']].astype("float64")
df[['height']] =df[['height']].astype("int64")
```
The **errors='coerce'** parameter instructs Pandas to enter a NaN at any field where the conversion fails.

#### Check data constitution
```python
>>> df.Age.unique()
>>> df.Age.value_counts()
```

### [Dive Deeper](https://courses.edx.org/courses/course-v1:Microsoft+DAT210x+6T2016/courseware/12621a4064aa4d92874a9d8a953734c5/e43e044ae9c045298766ece7d3881386/)



## Exploring Data
### Basic Plots
#### Histogram Plots
```python
import pandas as pd
import matplotlib
matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead

student_dataset = pd.read_csv("/Datasets/students.data", index_col=0)

my_series = student_dataset.G3
my_dataframe = student_dataset[['G3', 'G2', 'G1']] 

my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5)
```

#### Scatter Plot
```python
import pandas as pd
import matplotlib

matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead

student_dataset = pd.read_csv("/Datasets/students.data", index_col=0) 
student_dataset.plot.scatter(x='G1', y='G3')
```

#### 3D plot
```python
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pandas as pd
matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead

student_dataset = pd.read_csv("/Datasets/students.data", index_col=0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')

ax.scatter(student_dataset.G1, student_dataset.G3, student_dataset['Dalc'], c='r', marker='.')
plt.show()
```


### Higher Dimensionality
#### Parallel Coordinates
Parallel coordinates are useful because polylines belonging to similar records tend to cluster together.
To graph them with Pandas and MatPlotLib, you have to specify a feature to group by (it can be non-numeric) - like legend
```python
from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')
# If the above line throws an error, use plt.style.use('ggplot') instead

# Load up SKLearn's Iris Dataset into a Pandas Dataframe
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names) 

df['target_names'] = [data.target_names[i] for i in data.target]

# Parallel Coordinates Start Here:
plt.figure()
parallel_coordinates(df, 'target_names')
plt.show()
```
Pandas' parallel coordinates interface is extremely easy to use, but use it with care. It only supports a **single scale** for all your axes. If you have some features that are on a small scale and others on a large scale, you'll have to deal with a compressed plot. For now, your only three options are to:
* **Normalize** your features before charting them
* Change the scale to a **log scale**
* Or create **separate, multiple parallel coordinate charts**. Each one only plotting features with similar domains scales plotted

#### Andrew's Curves
An Andrews plot, also known as Andrews curve, helps you visualize higher dimensionality, multivariate data by plotting each of your dataset's observations as a curve. The feature values of the observation act as the coefficients of the curve, so observations with similar characteristics tend to group closer to each other. Due to this, Andrews curves have some use in outlier detection.
```python
from sklearn.datasets import load_iris
from pandas.tools.plotting import andrews_curves

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')
# If the above line throws an error, use plt.style.use('ggplot') instead

# Load up SKLearn's Iris Dataset into a Pandas Dataframe
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target_names'] = [data.target_names[i] for i in data.target]

# Andrews Curves Start Here:
plt.figure()
andrews_curves(df, 'target_names')
plt.show()
```
One of the current weaknesses with the Pandas implementation (and this goes for Parallel Coordinates as well) is that every single observation is charted. In the MATLAB version, you can specify a quantile or probability distribution cutoff. 

#### Imshow and Corr
.imshow() generates an image based off of the normalized values stored in a matrix, or rectangular array of float64s. The properties of the generated image will depend on the dimensions and contents of the array passed in:
* An [X, Y] shaped array will result in a grayscale image being generated
* A [X, Y, 3] shaped array results in a full-color image: 1 channel for red, 1 for green, and 1 for blue
* A [X, Y, 4] shaped array results in a full-color image as before with an extra channel for alpha

Besides being a **straightforward way to display .PNG and other images**, the .imshow() method has quite a few other use cases. When you use the .corr() method on your dataset, Pandas calculates a correlation matrix for you that measures how close to being linear the relationship between any two features in your dataset are.
```python 
>>> df = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
>>> df.corr()

          a         b         c         d         e
a  1.000000  0.007568  0.014746  0.027275 -0.029043
b  0.007568  1.000000 -0.039130 -0.011612  0.082062
c  0.014746 -0.039130  1.000000  0.025330 -0.028471
d  0.027275 -0.011612  0.025330  1.000000 -0.002215
e -0.029043  0.082062 -0.028471 -0.002215  1.000000

import matplotlib.pyplot as plt

plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()
```

### [Dive Deeper](https://courses.edx.org/courses/course-v1:Microsoft+DAT210x+6T2016/courseware/dfb4bc13bab749ceb87191a9185cb111/94a6eca559df4cd482e379d5e9bcbad7/)


## Transforming Data

### Principal Component Analysis (PCA)
Principal Component Analysis (PCA), a transformation that attempts to convert your possibly correlated features into a set of linearly uncorrelated ones, is the first unsupervised learning algorithm you'll study.

PCA falls into the group of **dimensionality reduction algorithms**. In many real-world datasets and the problems they represent, you aren't aware of what specifically needs to be measured to succinctly address the issue driving your data collection.
If you have reason to believe your question has a simple answer, or that the features you've collected are actually many indirect observations of some inherent source you either cannot or do not know how to measure, then dimensionality reduction applies to your needs.
PCA's approach to dimensionality reduction is to derive a set of degrees of freedom that can then be used to reproduce most of the variability of your data. It accesses your dataset's **covariance** structure directly using matrix calculations and eigenvectors to compute **the best unique features** that describe your samples.

PCA ensures that each newly computed view (feature) is **orthogonal or linearly independent to all previously computed ones**, minimizing these overlaps. PCA also orders the features by importance, assuming that the **more variance expressed in a feature, the more important it is**.

![pic_example_PCA](http://courses.edx.org/asset-v1:Microsoft+DAT210x+4T2016+type@asset+block@PCA1.jpg)

```python
>>> from sklearn.decomposition import PCA
>>> pca = PCA(n_components=2)
>>> pca.fit(df)
PCA(copy=True, n_components=2, whiten=False)

>>> T = pca.transform(df)

>>> df.shape
(430, 6) # 430 Student survey responses, 6 questions..
>>> T.shape
(430, 2) # 430 Student survey responses, 2 principal components.
```
you can recover your original feature values using **.inverse_transform()** so long as you don't drop any components. 
a few other interesting model attribute with the **.fit()** method:
* components_ These are your principal component vectors and are linear combinations of your original features. As such, they exist within the feature space of your original dataset.
* explained_variance_ This is the calculated amount of variance which exists in the newly computed principal components.
* explained_variance_ratio_ Normalized version of explained_variance_ for when your interest is with probabilities.

Some other things to pay attention:
* PCA is sensitive to the scaling of features. Unless need to respect the specific scaling, should always **standardize** first.
* *RandomizedPCA* is a faster training process with accuracy a bit affected. Will be useful for very large dataset.
* PCA is a **linear transformation** only, therefore cannot discern any complex, nonlinear intricacies. For such cases, you will have to make use different dimensionality reduction algorithms, such as Isomap.

### Isomap
Its goal: to uncover the intrinsic, geometric-nature of your dataset, as opposed to simply capturing your datasets most variant directions.
Isomap operates by first computing each record's nearest neighbors. Only a sample's K-nearest samples qualify for being included in its nearest-neighborhood samples list. A neighborhood graph is then constructed by linking each sample to its K-nearest neighbors.
Just as you would drive waypoint to waypoint in order to navigate to a final destination, so too does Isomap travel from sample to sample, taking the shortest neighborhood paths between any two distant samples in your dataset. The straightforward, e.g. high-dimensional, direct Euclidean distance between any two records fails to properly account for any intrinsic, nonlinear geometry present within your dataset's features.

![example_pic_isomap](http://courses.edx.org/asset-v1:Microsoft+DAT210x+4T2016+type@asset+block@isomap_replace.png)


Isomap is better than linear methods when dealing with almost all types of real image and motion tracking. If you're dataset comes from images captured in a natural way, or your data is characterized by similar types of motions, consider using isomap. 
```python
>>> from sklearn import manifold
>>> iso = manifold.Isomap(n_neighbors=4, n_components=2)
>>> iso.fit(df)
Isomap(eigen_solver='auto', max_iter=None, n_components=2, n_neighbors=4,
    neighbors_algorithm='auto', path_method='auto', tol=0)
>>> manifold = iso.transform(df)

>>> df.shape
(430, 6)
>>> manifold.shape
(430, 2)
```
Isomap is also a bit more **sensitive to noise** than PCA. Noisy data can actually act as a conduit to short-circuit the nearest neighborhood map, cause isomap to prefer the 'noisy' but shorter path between samples that lie on the real geodesic surface of your data that would otherwise be well separated.

When using unsupervised dimensionality reduction techniques, be sure to use the feature scaling on all of your features because the nearest-neighbor search that Isomap bases your manifold on will do poorly if you don't, and PCA will prefer features with larger variances. As explained within the labs' source code, **SciKit-Learn's StandardScaler** is a good-fit for taking care of  scaling your data before performing dimensionality reduction.


### Pre-processing
For a great overview on a few of the normalization methods supported in SKLearn, please check out: [link]( https://stackoverflow.com/questions/30918781/right-function-for-normalizing-input-of-sklearn-svm)

#### StandardScaler
It assumes that your features are normally distributed (each feature with a different mean and standard deviation), and scales them such that each feature's Gaussian distribution is now centered around 0 and it's standard deviation is 1.
#### Normalizer
It looks at all the feature values for a given data point as a vector and normalizes that vector by dividing it by it's magnitude. For example, let's say you have 3 features. The values for a specific point are [x1, x2, x3]. If you're using the default 'l2' normalization, you divide each value by sqrt(x1^2 + x2^2 + x3^2). If you're using 'l1' normalization, you divide each by x1+x2+x3.
#### MinMaxScaler
For each feature, this looks at the minimum and maximum value. This is the range of this feature. Then it shrinks or stretches this to the same range for each feature (the default is 0 to 1).
```python
from sklearn import preprocessing

T = preprocessing.StandardScaler().fit_transform(df)
T = preprocessing.MinMaxScaler().fit_transform(df)
T = preprocessing.MaxAbsScaler().fit_transform(df)
T = preprocessing.Normalizer().fit_transform(df)
```


### [Dive Deeper](https://courses.edx.org/courses/course-v1:Microsoft+DAT210x+6T2016/courseware/1aabc1638cb64c699ddc447d16e3cfea/d2dd5efbb36c4632af42178081be1c71/?child=first)



## Data Modeling

### Clustering - KMeans
```python
>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=5)
>>> kmeans.fit(df)
KMeans(copy_x=True, init='k-means++', max_iter=300, n_clusters=5, n_init=10,
    n_jobs=1, precompute_distances='auto', random_state=None, tol=0.0001,
    verbose=0)

>>> labels = kmeans.predict(df)
>>> centroids = kmeans.cluster_centers_


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(df.Longitude, df.Latitude, marker='.', alpha=0.3)

kmeans_model = KMeans(n_clusters = 7)
kmeans_model.fit(df)

centroids = kmeans_model.cluster_centers_
ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
print centroids
plt.show()
```
**Two** other key characteristics of K-Means are that it assumes your samples are **length normalized**, and as such, is sensitive to feature scaling. It also assumes that the cluster sizes are **roughly spherical and similar**; this way, the nearest centroid is always the correct assignment.

[An example for visualization of PCA in K-means](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT210x%20Programming%20with%20Python%20for%20Data%20Science/kmeans_PCA.py), and [the data source file](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT210x%20Programming%20with%20Python%20for%20Data%20Science/Wholesale%20customers%20data.csv)

![pic_demo](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT210x%20Programming%20with%20Python%20for%20Data%20Science/kmeans_PCA_demo.png)

### Spliting Data
A short summary and outlook:
Every single machine learning class, or estimator as SciKit-Learn call them, implements the .fit() method as you've seen. This will continue to hold true for the supervised one's as well. The unsupervised estimators also allowed you to make use of the following methods:
* .transform() : without changing the number of samples, alters the value of each existing feature by changing its units
* .predict() : only with clustering, you could predict the label of the specified sample.

What you'll now see is that supervised learning estimators implement a slightly different set of distinct methods:
* .predict() : After training your machine learning model, you can predict the labels of new and never seen samples
* .predict_proba() : For some estimators, you can further see what the probability of the new sample belonging to each label is
* .score(): The ability to score how well your model fit the training data

```python
>>> from sklearn.model_selection import train_test_split
>>> data_train, data_test, label_train, label_test = train_test_split(data, labels, test_size=0.5, random_state=7)

from sklearn.metrics import accuracy_score

# Returns an array of predictions:
>>> predictions = my_model.predict(data_test) 
>>> predictions
[0, 0, 0, 1, 0]

# The actual answers:
>>> label_train
[1, 1, 0, 1, 0]

>>> accuracy_score(label_train, predictions)
0.59999999999999998

>>> accuracy_score(label_train, predictions, normalize=False)
3
```


### Classification - K-nearest Neighbors


### Regression



### Dive Deeper



## Data Modeling II
### SVC
### Decision Trees
### Random Forest
### Dive Deeper
## Evaluating Data
### Confusion
### Cross Validation
### Power Tuning
### Dive Deeper
