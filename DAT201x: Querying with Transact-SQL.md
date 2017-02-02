## Section 1

### 01 | Introduction to Transact-SQL

#### SELECT one-in-all:
SELECT OrderDateKey, SUM(SalesAmount) AS TotalSales  
FROM FactInternetSales  
WHERE Status = 'shipped'
GROUP BY OrderDateKey  
HAVING OrderDateKey > 20010000  
ORDER BY OrderDateKey DESC;  

#### Data Type conversion:
CAST/TRY_CAST<br>
CONVERT/TRY_CONVERT<br>
PARSE/TRY_PARSE<br>
STR<br>

#### Nulls
ISNULL(col/var, value) //return value is col or var is null<br>
NULLIF(col/var, value) //return null if col or var is value<br>
COALESCE(col1/var1, col2/var2 ...) //return the 1st non-null col/var in the list<br>




### 02 | Querying Tables with SELECT
## Section 2
### 03 | Querying Multiple Tables with Joins

### 04 | Using Set Operators

### 05 | Using Functions and Aggregating Data
## Section 3
### 06 | Using Subqueries and APPLY
### 07 | Using Table Expressions
### 08 | Grouping Sets and Pivoting Data
## Section 4
### 09 | Modifying Data
### 10 | Programming with Transact-SQL
### 11 | Error Handling and Transactions
