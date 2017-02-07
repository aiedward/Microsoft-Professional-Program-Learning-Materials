# DAT208x Introduction to Python for Data Science

## Module 1 Hello Python!
```python
# Variables and Types
type(var)
```

## Module 2 Python Lists
```python
# a python list
['a','b',[1,2,3],['hey',21]]

# subsetting a list
list[0]
list[1:3] # [inclusive : exclusive]
list[:3]
list[5:]

# Manipulating Lists
list[1] = 'cool'
del(list[2])
list + [3,4,5]

# make a copy
list2 = list1[:] # list2=list1 will simply make "list2" a pointer to the first element of list1
```


## Module 3 Functions, Methods, and Packages
```python
# use help to check a function
help(pandas)

# Method: use dot notation
list.count(var)
string.replace('a','b')
```

## Module 4 Numpy
numpy is to perform <strong>element-wise computation</strong>
```python
# create an array
import numpy as np
arr = np.array([1, 2, 3])

# subsetting
arr2 = arr(arr > 1) # as the inner part returns a list of boolean results

# 2D Numpy Array
np_2d = np.array([[1,2,3],
                  [4,5,6]])
# use shape to see the dimension
np_2d.shape
# subsetting
np_2d[0]    # this reeturns the first row (as in array type)
np_2d[0][1] # this returns the single element
# other syntax
np_2d[0,2] np_2d[:,0:2] np_2d[1,:]

# Basic Statistics with Numpy
np.mean(np.array([1,2,3]))
np.median() 
np.corrcoef()
np.std()
```
## Module 5 Matplotlib
```python
Basic plot with matplotlib
Histograms
Customization
```
## Module 6
Boolean logic and control flow
Pandas

```python
python hello world!
```
