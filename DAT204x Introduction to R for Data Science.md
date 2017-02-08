# DAT204x Introduction to R for Data Science

## Module 1 Basics & Data Types
```r
# vaiable assignment
var <- 3

# workspace
ls()

# view datatype
class()

# logical datatype:
TRUE - FALSE - NA

# integer
132L

# check datatype
is.numeric(3L) - is.integer()

# coercion
as.numeric("2") - as.character(233) - as.integer(2.5)
```

## Module 2 Vectors
```R
# Create a vector
card_name <- c("spade", "diamond", "heart", "club")
is.vector(vec)

# name a vector
card_count <- c(12,13,10,9)
names(card_count) <- card_name
# another way
card_count <- c(spade=12, diamond=13, heart=10, club=9) # do not have to quote the names
# use str() to show the information
str(card_count) 
# length function
length(card_count)

# Vectoes are homogeneous (atomic vectors) that can only hold a single type of data. <> lists


# Vector arithmetic: computations are in element-wise manner
sum(bank_account)
# this expresssion returns a boolean vector
earnings > expenses

# Subsetting vectors
remain <- card_count[c(1,4)]
remain <- card_count[c(4,1)]
remain <- card_count[c("spade","diamond"])
# remove the 1st element
remain <- card_count[-1]
remain <- card_count[-c(1,3)] # but minus does not work with names

# R perform recycling for the shorter vector if two vector lengths are different.
val <- c(12,13,10,9,8)
remain <- val[c(TRUE, FALSE, TRUE)] # result remain==c(12,10,9)
```
## Module 3 Matrices
```python
Create name matrices
Subsetting matrices
Matrix arithmetic
## Module 4
Factors
```
## Module 5 List
```python
Create name list
Subset and extend list
```
## Module 6 DataFrame
```python
Explore data frame
Subset, extend, and sort data frame
```
## Module 7 Graphics
```python
Basic graphics
Customizing plots
Multiple plots
```
