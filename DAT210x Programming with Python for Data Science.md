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
  * Data Cleansing
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

student_dataset = pd.read_csv("/Datasets/students.data", index_col=0) student_dataset.plot.scatter(x='G1', y='G3')
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

### PCA

### Isomap

### Data Cleansing

### Dive Deeper




## Data Modeling
### Clustering
### Spliting Data
### K-nearest Neighbors
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
