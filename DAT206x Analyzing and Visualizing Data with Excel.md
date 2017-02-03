# DAT206x Analyzing and Visualizing Data with Excel

## Module 1
* Perform data analysis in Excel using classic tools, such as pivot tables, pivot charts, and slicers, on data that is already in a worksheet / grid data.

### Data Model

- Data -> Manage Data Model<br>
- Power Pivot -> Manage<br>

- Check Tables' relationship: Diagram View<br>
- Using Data Model in Pivot Table: Pivot Table -> use this workbook's Data Model<br>
- Create a slicer<br>

## Module 2 
* Explore an Excel data model. Create your first DAX expressions for calculated columns and measures.

what is DAX - Data Analysis Expressions (DAX) is a collection of functions, operators, and constants that can be used in a formula, or expression, to calculate and return one or more values. Stated more simply, DAX helps you create new information from data already in your model.

Where to use DAX: as [**calculated columns/rows**](http://www.excel-easy.com/examples/images/structured-references/formula-copied.png) and as [**measures**](https://support.content.office.net/en-us/media/fa025fa9-1921-427d-b273-6c9395743135.png).

Create a DAX 
- an example: Revenue:=[OrderQuantity]***[ListPrice] // *calculated column* <br>
- second example: TotalRevenue:=sum(InternalSales[Revenue]) // *measure* as revenue (also a DAX created previously) in InternalSales table<br>
and they can be used in PivotTable.

## Module 3
* Learn about queries (Power Query add-in in Excel 2013 and Excel 2010), and build an Excel data model from a single flat table.

Acess csv file: Data -> New Query -> From Files -> From csv<br>
Pre=processing functionality: Split Column / (right click) Replace Values <br>
Save and Load (To)<br>

## Module 4
* Learn how to import multiple tables from a SQL database, and create an Excel data model from the imported data.
* Create a mash-up between data from text-files and data from a SQL database.

- More on **Pre-processing**:<br>
- Add Column -> Merge Column<br>
- Filters (↓ menu) -> Equal/Between/Larger...<br>
- Create a *Date Table*: Design -> Date Table<br>
- Home -> Append Query<br>


## Module 5
* Get the details on how to create measures to calculate for each cell, filter context for calculation, and explore several advanced DAX functions.

- SUMX/COUNTX/AVERAGEX(Table, Expression)<br>
- Pivot Table Right Panel (right click) -> Add Measure -> "=CALCULATE(Expression, Filter1, Filter2...)<br>
  Example: =CALCULATE([Revenue], ALL([CountryName]) -> this is for given a grand total which could be used for percentage calculation in subsequent step.

More on DAX:

DAX includes many functions that return a table rather than a value. The table is not displayed, but is used to provide input to other functions. For example, you can retrieve a table and then count the distinct values in it, or calculate dynamic sums across filtered tables or columns.
DAX includes a variety of time intelligence functions. These functions let you define or select date ranges, and perform dynamic calculations based on them. For example, you can compare sums across parallel periods.
 
## Module 6
* Find out how to use advanced text query to import data from a formatted Excel report. Perform querie beyond the standard user interface.

- Home -> Use 1st row as headers
- Transform -> Fill -> Fill up/down
- Transform -> Pivot/Unpivot

## Module 7
* Explore ways to create stunning visualizations in Excel. Use the cube functions to perform year-over-year comparisons.

Slicer connect to multiple charts:<br>
Options -> Report Connections<br>
Pivot Table Tools -> Analyze -> OLAP Tools -> Convert to Formulas<br>

## Module 8
* Create timelines, hierarchies, and slicers to enhance your visualizations. Learn how Excel can work together with Power BI.
* Upload an Excel workbook to the Power BI service. Explore the use of Excel on the mobile platform. 


