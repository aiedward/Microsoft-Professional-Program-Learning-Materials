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
#Create name matrices
matrix(1:6, nrow=2)
matrix(LETTERS[1:6], ncol=2)
matrix(1:6, nrow=2, byrow=TRUE)
# R also do recycling for creating matrices
matrix(1:3, nrow=3, ncol=3) 
# cbind & rbind
cbind(1:3, 1:3)
rbind(m, c(1,2,3))

# naming matrices
rownames()
colnames(m) <- c('col1','col2','col3') 
m <- matrix(1:6, byrow=TRUE, nrow=2, 
            dimnames=list(c('row1','row2'),
                          c('col1','col2','col3')))
                          
#Subsetting matrices
m[1,3] # R's index starts at 1
m[2,]
m[4] # count by column the 4th element
m[c(1,2),c("row2","row3")]
m["row1",c(TRUE, FALSE)]

#Matrix arithmetic
colSums() - rowSums()
```
## Module 4 Factors
```python
# Factors are for categorical values
blood_factor <- factor(blood_data)
str(blood_facto) # use string to check the info
# manually state the order
blood_factor <- factor(blood_data,
                       levels=c('A','B','AB','O')) # if not, automatically based on alphabet.
# labels to give nicknames
blood_factor <- factor(blood_data,
                       levels=c('A','B','AB','O')
                       labels=c('aA','bB','aAbB','oO'))
# ordinal data
tshirt_size <- factor(tshirt, ordered=TRUE,
                      levels=c('S','M','L'))
```

## Module 5 List
```python
# Create name list
song <- list("cool guys", 190, 5, list(title="whatup girls", duration=120))
is.list(song)
names(song) <- c("title","duration(s)","track","similar song")
str(song)

# Subsetting
# single bracket [ select a sublist, double bracket [[ select the elements.
song[c(1,3)]
song[[1]]
song[["similar song"]][[2]] # select the 2nd element in "similar song" of the super-list.
# $ dollar sign is equivalent to [[
song$duration

# extending the list
song$friends <- c('bob','cindy')
song[['friends']] <- list('bob','cindy')
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
