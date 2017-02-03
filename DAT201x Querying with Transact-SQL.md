## Section 1

### 01 | Introduction to Transact-SQL

#### SELECT one-in-all:
SELECT OrderDateKey, SUM(SalesAmount) AS TotalSales  
FROM FactInternetSales  
WHERE Status = 'shipped'
GROUP BY OrderDateKey  
HAVING OrderDateKey > 20010000  
ORDER BY OrderDateKey DESC;  

### 02 | Querying Tables with SELECT

#### Data Type conversion:
CAST/TRY_CAST<br>
CONVERT/TRY_CONVERT<br>
PARSE/TRY_PARSE<br>
STR<br>

#### Nulls
ISNULL(col/var, value) //return value is col or var is null<br>
NULLIF(col/var, value) //return null if col or var is value<br>
COALESCE(col1/var1, col2/var2 ...) //return the 1st non-null col/var in the list<br>

#### Distinct, Top and Offset

<em>Examples:</em>

- SELECT IsNull(try_cast(Size As Integer),0) As NumericSize FROM SalesLT.Product

- SELECT ProductNumber, NULLIF(Color,'Multi') + ',' + IsNull(Size, '') As ProductDetails FROM SalesLT.Product

- SELECT Name, <br>
	Case<br>
	   When SellEndDate IS NULL THEN 'on sale'<br>
		 ELSE 'Discontinued'<br>
		 END AS SalesStatus<br>
  FROM SalesLT.Product<br>
      
- SELECT DISTINCT ISNULL(Color, 'NONE') AS COLOR, ISNULL(Size, '-') AS SIZE<br>
  FROM SalesLT.Product<br>
  ORDER BY COLOR DESC<br>
  
- SELECT TOP 10 Name, ListPrice FROM SalesLT.Product<br>
  ORDER BY ListPrice DESC<br>

- SELECT Name, ListPrice FROM SalesLT.Product<br>
  ORDER BY ListPrice DESC<br>
  OFFSET 5 ROWS<br>
  FETCH FIRST 10 ROW ONLY<br>

- SELECT TOP 10 PERCENT Name, Color, Size FROM SalesLT.Product WHERE ProductID > 100

#### Filtering and Removing Duplicate

##### wildcard: %:any length, _: one digit
##### Specify predicates in WHERE CLAUSE: "= < >", IN, BETWEEN, LIKE, AND, OR, NOT

- SELECT Name FROM SalesLT.Product WHERE ProductNumber LIKE '%FR%'
- SELECT Name FROM SalesLT.Product WHERE ProductNumber LIKE 'FR-_[0-9][0-9]_-[0-9][0-9]'
- SELECT Name FROM SalesLT.Product WHERE SellEndDate IS NOT NULL
- SELECT Name FROM SalesLT.Product WHERE SellEndDate BETWEEN '2006/1/1' AND '2006/12/31'
- SELECT ProductCategoryID, SellEndDate, Name, ListPrice FROM SalesLT.Product WHERE ProductCategoryID IN (5,6,7,8) AND SellEndDate BETWEEN '2006/1/1' AND '2006/12/31'



## Section 2
### 03 | Querying Multiple Tables with Joins

#### Inner Join
- SELECT SalesLT.Product.Name AS ProductName, SalesLT.ProductCategory.Name As Category<br>
  FROM SalesLT.Product JOIN SalesLT.ProductCategory<br>
  ON SalesLT.Product.ProductCategoryID = SalesLT.ProductCategory.ProductCategoryID<br>
  
#### Outer Join
* Left Outer
* Right Outer
* Full Outer

- SELECT c.FirstName, c.LastName, oh.SalesOrderNumber<br>
  FROM SalesLT.Customer As c<br>
  LEFT JOIN SalesLT.SalesOrderHeader As oh<br>
  ON c.CustomerID = oh.CustomerID<br>
  ORDER BY c.CustomerID

#### Cross Join
A cross join returns a Cartesian product that includes every combination of the selected columns from both tables.

- SELECT p.Name, c.FirstName, c.LastName, c.Phone<br>
  FROM SalesLT.Product As p<br>
  CROSS JOIN SalesLT.Customer as c<br>

#### Self Join
SELF JOIN is using LEFT JOIN but must with alias


### 04 | Using Set Operators

#### Union
Use UNION to combine the rowsets returned by mulitple queries.

- SELECT FirstName, LastName, 'Employee' As Type<br>
  FROM SalesLT.Employees<br>
  UNION ALL<br>
  SELECT FirstName, LastName, 'Customer' --it's changing the column name customer to Type also<br>
  FROM SalesLT.Customers<br>
  ORDER BY LastName<br>

#### Intersect
#### Except

### 05 | Using Functions and Aggregating Data

Lecture Notes:
![ALT TEXT](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/Using%20Functions%20and%20Aggregating%20Data.jpg)

Sample SQLs: Build In Functions<br>

--Scalar<br>
--YEAR, DATENAME(mm/dw, XX), DAY, DATEDIFF, GETDATE()<br>
--UPPER, CONCAT, LEFT, SUBSTRING, CHARINDEX, REVERSE<br>

--Logical<br>
SELECT Name, Size AS NumericSize FROM SalesLT.Product<br>
WHERE ISNUMERIC(Size)=1<br>

SELECT Name, IIF(ProductCategoryID IN (5,6,7), 'Bike', 'Others') AS ProductType<br>
FROM SalesLT.Product<br>

SELECT prd.Name AS ProductName, cat.Name AS categoty,<br>
	CHOOSE (cat.ParentProductCategoryID, 'Bike','Component','Clothing','Accessories') AS ProductType<br>
FROM SalesLT.Product AS prd<br>
JOIN SalesLT.ProductCategory AS cat<br>
ON prd.ProductCategoryID = cat.ProductCategoryID<br>

--WINDOW<br>
SELECT TOP(100) ProductID, Name, ListPrice,<br>
	RANK() OVER (ORDER BY ListPrice DESC) AS RankByPrice<br>
FROM SalesLT.Product <br>
ORDER BY RankByPrice<br>

SELECT c.Name AS Category, p.Name AS Product, ListPrice,<br>
	RANK() OVER (PARTITION BY c.Name ORDER BY ListPrice DESC) AS RankByPrice<br>
FROM SalesLT.Product AS p<br>
JOIN SalesLT.ProductCategory AS c<br>
ON p.ProductCategoryID = c.ProductCategoryID<br>
ORDER BY Category, RankByPrice<br>
<br>
--Aggregate<br>
SELECT COUNT(*) AS Products, COUNT(DISTINCT ProductCategoryID) AS Categories, AVG(ListPrice) AS AveragePrice<br>
FROM SalesLT.Product<br>
<br>
SELECT COUNT(P.ProductID) AS BikeModels, MIN(p.ListPrice) AS MinPrice<br>
FROM SalesLT.Product as p<br>
JOIN SalesLT.ProductCategory AS c<br>
ON p.ProductCategoryID = c.ProductCategoryID<br>
WHERE c.Name LIKE '%Bikes'<br>

--Grouping<br>
SELECT c.SalesPerson, CONCAT(c.FirstName+ ' ', C.LastName) AS Customer, ISNULL(SUM(oh.SubTotal), 0.00) AS SalesRevenue<br>
FROM SalesLT.Customer As c<br><br>
LEFT JOIN SalesLT.SalesOrderHeader AS oh<br>
ON c.CustomerID = oh.CustomerID<br>
GROUP BY c.SalesPerson, CONCAT(c.FirstName+ ' ', C.LastName) --group by cannot use alias<br>
ORDER BY SalesRevenue DESC, Customer -- order by you can<br>

SELECT ProductID, SUM(sod.OrderQty) AS Quantity<br>
FROM SalesLT.SalesOrderDetail AS sod<br>
JOIN SalesLT.SalesOrderHeader AS soh<br>
ON sod.SalesOrderID = soh.SalesOrderID<br>
WHERE YEAR(soh.OrderDate) = 2008<br>
GROUP BY ProductID<br>
HAVING SUM(sod.OrderQty) > 50<br>


## Section 3
### 06 | Using Subqueries and APPLY

![ALT TEXT](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/Subqueries%20and%20APPLY.jpg)

Example:<br>

--Subqueries<br>
SELECT * FROM SalesLT.Product<br>
WHERE ListPrice > <br>
	(SELECT MAX(UnitPrice) FROM SalesLT.SalesOrderDetail)<br>


SELECT CustomerID , SalesOrderID, OrderDate<br>
FROM SalesLT.SalesOrderHeader As SO1<br>
WHERE orderDate = <br>
	(SELECT MAX(orderDate)<br>
	FROM SalesLT.SalesOrderHeader AS SO2<br>
	WHERE SO1.CustomerID = SO2.CustomerID)<br>
	ORDER BY CustomerID<br>

--Apply<br>


### 07 | Using Table Expressions
![ALT TEXT](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/VIEW%2C%20and%20table%20Expressions.jpg)

--Table Expression<br>

--Query VIEWS<br>
CREATE VIEW SalesLT.vCustomerAddress<br>
AS<br>
SELECT C.CustomerID, FirstName, LastName, AddressLine1, City, stateProvice<br>
FROM <br>
SalesLT.Customer C JOIN SalesLT.Customer.Address CA<br>
ON C.CustomerID = CA.CustomerID<br>
JOIN<br>
SalesLT.Address A<br>
ON CA.AddressID = A.AddressID<br>

--Temporary Tables<br>
CREATE TABLE #Colors<br>
(Color varchar(15))<br>

INSERT INTO #Colors<br>
SELECT DISTINCT Color FROM SalesLT.Product<br>

SELECT * FROM #Colors<br>

--Table variable<br>
DECLARE @Colors As TABLE (Color varchar(15))<br>
<br>
INSERT INTO @Colors<br>
SELECT DISTINCT Color FROM SalesLT.Product<br>
SELECT * FROM @Colors<br>
<br>
--TABLE_VALUED FUNCTIONS (TVF)<br>
CREATE FUNCTION SalesLT.udfCustomersByCity<br>
(@City AS varchar(20))<br>
RETURN TABLE<br>
AS<br>
RETURN<br>
(SELECT C.CustomerID, FirstName, LastName, AddressLine1, City, StateProvice<br>
FROM <br>
SalesLT.Customer AS C JOIN SalesLT.Customer.Address AS CA<br>
ON C.CustomerID = CA.CustomerID<br>
JOIN SalesLT.Address A ON CA.AddressID = A.AddressID<br>
WHERE City = @CITY)<br>

SELECT * FROM SalesLT.udfCustomersByCity('Bellevue')<br>


--Derived Tables<br>
SELECT Category, COUNT(ProductID) AS Products<br>
FROM<br>
	(SELECT p.ProductID, p.Name AS Product, c.Name AS Category<br>
	FROM SalesLT.Product AS p<br>
	JOIN SalesLT.ProductCategory AS c<br>
	ON p.ProductCategoryID = c.ProductCategoryID) AS ProdCats<br>
GROUP BY Category<br>
ORDER BY Category<br>

--Common Table Expressions (CTEs)<br>
WITH ProductByCategory (ProductID, ProductName, Category)<br>
AS<br>
(<br>
	SELECT p.ProductID, p.Name, c.Name AS Category<br>
	FROM SalesLT.Product AS p<br>
	JOIN SalesLT.ProductCategory As c<br>
	ON p.ProductCategoryID = c.ProductCategoryID<br>
)<br>
SELECT Category, COUNT(ProductID) AS Products<br>
FROM ProductByCategory<br>
GROUP BY Category<br>
ORDER BY Category<br>


### 08 | Grouping Sets and Pivoting Data



## Section 4
### 09 | Modifying Data
### 10 | Programming with Transact-SQL
### 11 | Error Handling and Transactions
