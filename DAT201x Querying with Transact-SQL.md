## Section 1

### 01 | Introduction to Transact-SQL

#### SELECT one-in-all:
```sql
SELECT OrderDateKey, SUM(SalesAmount) AS TotalSales  
FROM FactInternetSales  
WHERE Status = 'shipped'
GROUP BY OrderDateKey  
HAVING OrderDateKey > 20010000  
ORDER BY OrderDateKey DESC;  
```

### 02 | Querying Tables with SELECT

#### Data Type conversion:
```sql
CAST/TRY_CAST
CONVERT/TRY_CONVERT
PARSE/TRY_PARSE
STR
```

#### Nulls

```sql
ISNULL(col/var, value) //return value is col or var is null
NULLIF(col/var, value) //return null if col or var is value
COALESCE(col1/var1, col2/var2 ...) //return the 1st non-null col/var in the list
```

#### Distinct, Top and Offset

<em>Examples:</em>

```sql
SELECT IsNull(try_cast(Size As Integer),0) As NumericSize FROM SalesLT.Product

SELECT ProductNumber, NULLIF(Color,'Multi') + ',' + IsNull(Size, '') As ProductDetails FROM SalesLT.Product

SELECT Name, 
  Case
    When SellEndDate IS NULL THEN 'on sale'
    ELSE 'Discontinued'
    END AS SalesStatus
FROM SalesLT.Product
      
SELECT DISTINCT ISNULL(Color, 'NONE') AS COLOR, ISNULL(Size, '-') AS SIZE<br>
FROM SalesLT.Product<br>
ORDER BY COLOR DESC<br>
  
SELECT TOP 10 Name, ListPrice FROM SalesLT.Product<br>
ORDER BY ListPrice DESC<br>

SELECT Name, ListPrice FROM SalesLT.Product<br>
ORDER BY ListPrice DESC<br>
OFFSET 5 ROWS<br>
FETCH FIRST 10 ROW ONLY<br>

SELECT TOP 10 PERCENT Name, Color, Size FROM SalesLT.Product WHERE ProductID > 100
```

#### Filtering and Removing Duplicate

##### wildcard: %:any length, _: one digit
##### Specify predicates in WHERE CLAUSE: "= < >", IN, BETWEEN, LIKE, AND, OR, NOT

```sql
- SELECT Name FROM SalesLT.Product WHERE ProductNumber LIKE '%FR%'
- SELECT Name FROM SalesLT.Product WHERE ProductNumber LIKE 'FR-_[0-9][0-9]_-[0-9][0-9]'
- SELECT Name FROM SalesLT.Product WHERE SellEndDate IS NOT NULL
- SELECT Name FROM SalesLT.Product WHERE SellEndDate BETWEEN '2006/1/1' AND '2006/12/31'
- SELECT ProductCategoryID, SellEndDate, Name, ListPrice FROM SalesLT.Product WHERE ProductCategoryID IN (5,6,7,8) AND SellEndDate BETWEEN '2006/1/1' AND '2006/12/31'
```



## Section 2
### 03 | Querying Multiple Tables with Joins

#### Inner Join
```sql
SELECT SalesLT.Product.Name AS ProductName, SalesLT.ProductCategory.Name As Category
FROM SalesLT.Product JOIN SalesLT.ProductCategory
ON SalesLT.Product.ProductCategoryID = SalesLT.ProductCategory.ProductCategoryID
```
  
#### Outer Join
* Left Outer
* Right Outer
* Full Outer

```sql
SELECT c.FirstName, c.LastName, oh.SalesOrderNumber
FROM SalesLT.Customer As c
LEFT JOIN SalesLT.SalesOrderHeader As oh
ON c.CustomerID = oh.CustomerID
ORDER BY c.CustomerID
 ```

#### Cross Join
A cross join returns a Cartesian product that includes every combination of the selected columns from both tables.

```sql
SELECT p.Name, c.FirstName, c.LastName, c.Phone
FROM SalesLT.Product As p
CROSS JOIN SalesLT.Customer as c
```

#### Self Join
SELF JOIN is using LEFT JOIN but must with alias


### 04 | Using Set Operators

#### Union
Use UNION to combine the rowsets returned by mulitple queries.

```sql
SELECT FirstName, LastName, 'Employee' As Type
FROM SalesLT.Employees
UNION ALL
SELECT FirstName, LastName, 'Customer' --it's changing the column name customer to Type also
FROM SalesLT.Customers
ORDER BY LastName
```

#### Intersect
#### Except

### 05 | Using Functions and Aggregating Data

Lecture Notes:
![Using Functions and Aggregation Data](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT201x%20Querying%20with%20Transact-SQL%20screenshots/Using%20Functions%20and%20Aggregating%20Data.jpg)

Sample SQLs: Build In Functions<br>

```sql
--Scalar
--YEAR, DATENAME(mm/dw, XX), DAY, DATEDIFF, GETDATE()
--UPPER, CONCAT, LEFT, SUBSTRING, CHARINDEX, REVERSE

--Logical
SELECT Name, Size AS NumericSize FROM SalesLT.Product
WHERE ISNUMERIC(Size)=1

SELECT Name, IIF(ProductCategoryID IN (5,6,7), 'Bike', 'Others') AS ProductType
FROM SalesLT.Product

SELECT prd.Name AS ProductName, cat.Name AS categoty,
	CHOOSE (cat.ParentProductCategoryID, 'Bike','Component','Clothing','Accessories') AS ProductType
FROM SalesLT.Product AS prd
JOIN SalesLT.ProductCategory AS cat
ON prd.ProductCategoryID = cat.ProductCategoryID

--WINDOW
SELECT TOP(100) ProductID, Name, ListPrice,
	RANK() OVER (ORDER BY ListPrice DESC) AS RankByPrice
FROM SalesLT.Product 
ORDER BY RankByPrice

SELECT c.Name AS Category, p.Name AS Product, ListPrice,
	RANK() OVER (PARTITION BY c.Name ORDER BY ListPrice DESC) AS RankByPrice
FROM SalesLT.Product AS p
JOIN SalesLT.ProductCategory AS c
ON p.ProductCategoryID = c.ProductCategoryID
ORDER BY Category, RankByPrice

--Aggregate<br>
SELECT COUNT(*) AS Products, COUNT(DISTINCT ProductCategoryID) AS Categories, AVG(ListPrice) AS AveragePrice
FROM SalesLT.Product

SELECT COUNT(P.ProductID) AS BikeModels, MIN(p.ListPrice) AS MinPrice
FROM SalesLT.Product as p
JOIN SalesLT.ProductCategory AS c
ON p.ProductCategoryID = c.ProductCategoryID
WHERE c.Name LIKE '%Bikes'

--Grouping
SELECT c.SalesPerson, CONCAT(c.FirstName+ ' ', C.LastName) AS Customer, ISNULL(SUM(oh.SubTotal), 0.00) AS SalesRevenue
FROM SalesLT.Customer As c
LEFT JOIN SalesLT.SalesOrderHeader AS oh
ON c.CustomerID = oh.CustomerID
GROUP BY c.SalesPerson, CONCAT(c.FirstName+ ' ', C.LastName) --group by cannot use alias
ORDER BY SalesRevenue DESC, Customer -- order by you can

SELECT ProductID, SUM(sod.OrderQty) AS Quantity
FROM SalesLT.SalesOrderDetail AS sod
JOIN SalesLT.SalesOrderHeader AS soh
ON sod.SalesOrderID = soh.SalesOrderID
WHERE YEAR(soh.OrderDate) = 2008
GROUP BY ProductID
HAVING SUM(sod.OrderQty) > 50
```


## Section 3
### 06 | Using Subqueries and APPLY

![Using Subqueries and APPLY](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT201x%20Querying%20with%20Transact-SQL%20screenshots/Subqueries%20and%20APPLY.jpg)

Example:<br>

```sql
--Subqueries
SELECT * FROM SalesLT.Product
WHERE ListPrice > 
	(SELECT MAX(UnitPrice) FROM SalesLT.SalesOrderDetail)


SELECT CustomerID , SalesOrderID, OrderDate
FROM SalesLT.SalesOrderHeader As SO1
WHERE orderDate = 
	(SELECT MAX(orderDate)
	FROM SalesLT.SalesOrderHeader AS SO2
	WHERE SO1.CustomerID = SO2.CustomerID)
	ORDER BY CustomerID

--Apply
```

### 07 | Using Table Expressions
![Using Table Expressions](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT201x%20Querying%20with%20Transact-SQL%20screenshots/VIEW%2C%20and%20table%20Expressions.jpg)

```sql
--Table Expression

--Query VIEWS
CREATE VIEW SalesLT.vCustomerAddress
AS
SELECT C.CustomerID, FirstName, LastName, AddressLine1, City, stateProvice
FROM 
SalesLT.Customer C JOIN SalesLT.Customer.Address CA
ON C.CustomerID = CA.CustomerID
JOIN
SalesLT.Address A
ON CA.AddressID = A.AddressID

--Temporary Tables
CREATE TABLE #Colors
(Color varchar(15))

INSERT INTO #Colors
SELECT DISTINCT Color FROM SalesLT.Product

SELECT * FROM #Colors

--Table variable
DECLARE @Colors As TABLE (Color varchar(15))

INSERT INTO @Colors
SELECT DISTINCT Color FROM SalesLT.Product
SELECT * FROM @Colors

--TABLE_VALUED FUNCTIONS (TVF)
CREATE FUNCTION SalesLT.udfCustomersByCity
(@City AS varchar(20))
RETURN TABLE
AS
RETURN
(SELECT C.CustomerID, FirstName, LastName, AddressLine1, City, StateProvice
FROM 
SalesLT.Customer AS C JOIN SalesLT.Customer.Address AS CA
ON C.CustomerID = CA.CustomerID
JOIN SalesLT.Address A ON CA.AddressID = A.AddressID
WHERE City = @CITY)

SELECT * FROM SalesLT.udfCustomersByCity('Bellevue')


--Derived Tables
SELECT Category, COUNT(ProductID) AS Products
FROM
	(SELECT p.ProductID, p.Name AS Product, c.Name AS Category
	FROM SalesLT.Product AS p
	JOIN SalesLT.ProductCategory AS c
	ON p.ProductCategoryID = c.ProductCategoryID) AS ProdCats
GROUP BY Category
ORDER BY Category

--Common Table Expressions (CTEs)
WITH ProductByCategory (ProductID, ProductName, Category)
AS
(
	SELECT p.ProductID, p.Name, c.Name AS Category
	FROM SalesLT.Product AS p
	JOIN SalesLT.ProductCategory As c
	ON p.ProductCategoryID = c.ProductCategoryID
)
SELECT Category, COUNT(ProductID) AS Products
FROM ProductByCategory
GROUP BY Category
ORDER BY Category
```

### 08 | Grouping Sets and Pivoting Data

![Grouping Sets and Pivoting Data](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT201x%20Querying%20with%20Transact-SQL%20screenshots/Grouping%20and%20Pivoting.jpg)

Example:<br>

```sql
--Grouping Set
SELECT cat.ParentProductCategoryName, cat.ProductcategoryName, count(prd.productID) AS Products
FROM SalesLT.vGetAllCategories AS cat
LEFT JOIN SalesLT.Product AS prd
ON prd.ProductCategoryID = cat.ProductCategoryID
GROUP BY cat.ParentProductCategoryName, cat.ProductCategoryName
--Group BY GROUPING SETS(cat.ParentProductCategoryName, cat.ProductCategoryName,())
--Group BY ROLLUP(cat.ParentProductCategoryName, cat.ProductCategoryName)
--Group BY CUBE(cat.ParentProductCategoryName, cat.ProductCategoryName)
ORDER BY cat.ParentProductCategoryName, cat.ProductCategoryName

--Pivoting Data
SELECT * FROM 
(SELECT P.ProductID, PC.Name, ISNULL(P.Color, 'Uncolored') AS Color
FROM SalesLT.ProductCategory AS PC
JOIN SalesLT.Product AS P
ON PC.ProductCategoryID = P.ProductCategoryID
) AS PPC
PIVOT(Count(ProductID) FOR Color IN([Red],[Blue],[Black],[Silver],[Yellow],[Grey],[Multi],[Uncolored])) AS pvt
ORDER BY Name
```


## Section 4

### 09 | Modifying Data

![Modifying Data](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT201x%20Querying%20with%20Transact-SQL%20screenshots/Modifying%20data.jpg)

```sql
--Insert data
CREATE TABLE SalesLT.CallLog
(
	CallID int IDENTITY PRIMARY KEY NOT NULL,
	CallTime datetime NOT NULL Default GETDATE(),
	SalesPerson nvarchar(256) NOT NULL,
	CustomerID int NOT NULL REFERENCES SalesLT.Customer(CustomerID),
	PhoneNumber nvarchar(25) NOT NULL,
	Notes nvarchar(max) NULL
);
GO

INSERT INTO SalesLT.CallLog
VALUES
('2016-01-01T12:30:00','adventure-works\pamela0',1,'245-555-0173','returning call to me')

SELECT * FROM SalesLT.CallLog

INSERT INTO SalesLT.CallLog
VALUES
(DEFAULT, 'adventure\davd8',2,'170-555-0217',NULL)

INSERT INTO SalesLT.CallLog (SalesPerson, CustomerID, PhoneNumber)
VALUES
('adventure-works\jilian0',3,'279-555-0130')

INSERT INTO SalesLT.CallLog (SalesPerson, CustomerID, PhoneNumber, Notes)
SELECT SalesPerson, CustomerID, Phone, 'Sales promotion call'
FROM SalesLT.Customer
WHERE companyName = 'Big-Time Bike Store'

INSERT INTO SalesLT.CallLog (SalesPerson, CustomerID, PhoneNumber)
VALUES
('adventure-works\jose1',10,'150-555-0127')

SELECT SCOPE_IDENTITY()

SELECT * FROM SalesLT.CallLog

--Overriding Identity
SET IDENTITY_INSERT SalesLT.CallLog ON
INSERT INTO SalesLT.CallLog (CallID, SalesPerson, CustomerID, PhoneNumber)
VALUES
(10,'adventure-works\jose1',10,'926-555-0159')
SET IDENTITY_INSERT SalesLT.CallLog OFF


--Updating Data
UPDATE SalesLT.CallLog
SET Notes = 'No Notes'
WHERE Notes IS NULL

SELECT * FROM SalesLT.CallLog

UPDATE SalesLT.CallLog
SET SalesPerson = c.SalesPerson, PhoneNumber = c.Phone
FROM SalesLT.Customer AS c
WHERE c.CustomerID = SalesLT.CallLog.CustomerID

DELETE FROM SalesLT.CallLog

DELETE FROM SalesLT.CallLog
WHERE CallTime < DateAdd(dd, -7, GETDATE())

TRUNCATE TABLE SalesLT.CallLog
```

### 10 | Programming with Transact-SQL

![Programming with Transact-SQL](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT201x%20Querying%20with%20Transact-SQL%20screenshots/Programming%20with%20T-SQL.jpg)

--PROGRAMMING IN SQL<br>

```sql
/*
	Batches: GO
	Comments: /* */
	Variables: 
		-work only with one batch
		DECLARE @City VARCHAR(20) = 'Toronto'
		SET @City = 'Chengdu'
		-can use with SELECT
		SELECT @MAX_DATE = MAX(Date) FROM SalesLT.SalesOrderHeader
		PRINT @MAX_DATE
	Conditional Branching:
		-IF...ELSE:
			UPDATE SalesLT.Product
			SET DiscontunedDate=GETDATE()
			WHERE ProductID = 680

			IF @@ROWCOUNT &lt; 1
			BEGIN
				PRINT 'Product not Found'
			END
			ELSE
			BEGIN
				PRINT 'Product Updated'
			END
	
	Looping:
		DECLARE @counter int = 1
		WHILE @counter &lt;= 5

		BEGIN
			INSERT SalesLT.DemoTable(Description)
			VALUES('ROW' + CONVERT(varchar(5), @counter)
			SET @counter = @counter+1
		END
		SELECT Description FROM SalesLT.DemoTable
	
	Stored Procedure:
		CREATE PROCEDURE SalesLT.GetProductByCategory (@CategoryID INT =NULL)
		AS
			IF @CategoryID IS NULL
				SELECT ProductID, Name, Color, Size, ListPrice
				FROM SalesLT.Product
			ELSE 
				SELECT ProductID, Name, Color, Size, ListPrice
				FROM SalesLT.Product
				WHERE ProductCategoryID = @CategoryID

		EXEC SalesLT.GetProductByCategory
		EXEC SalesLT.GetProductByCategory 5
*
```

### 11 | Error Handling and Transactions

![Error Handling and Transactions](https://github.com/yang0339/Microsoft-Professional-Program-Learning-Materials/blob/master/DAT201x%20Querying%20with%20Transact-SQL%20screenshots/Error%20Handling%20and%20Transactions.jpg)
