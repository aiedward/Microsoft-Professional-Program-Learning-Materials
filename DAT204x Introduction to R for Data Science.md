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


# Vector arithmetic


# Subsetting vectors
```
## Module 3
Create name matrices
Subsetting matrices
Matrix arithmetic
## Module 4
Factors
## Module 5
Create name list
Subset and extend list
## Module 6
Explore data frame
Subset, extend, and sort data frame
## Module 7
Basic graphics
Customizing plots
Multiple plots
