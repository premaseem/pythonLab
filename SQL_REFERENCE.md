# MYSQL QUIRES AND CONCEPTS 

SQL is a standard language for storing, manipulating and retrieving data in databases.

## SQL Aliases
SQL aliases are used to give a table, or a column in a table, a temporary name.
Aliases are often used to make column names more readable.
An alias only exists for the duration of the query.

## SQL JOIN
A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

### Different Types of SQL JOINs
Here are the different types of the JOINs in SQL:

    (INNER) JOIN: Returns records that have matching values in both tables
    LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
    RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
    FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table


## INNER JOIN (Intersection)
Returns records that have matching values in both tables
Print order table, just fetch values from join table to populate the values in the projection from the customer table. 
Since it is intersection, order ie left of right does not matter

    SELECT ot.orderid, ot.customerid as ocid, ct.customerid as ccid, ct.customername, ot.orderdate FROM Orders AS ot INNER JOIN customers as ct ON ot.customerid=ct.customerid;

## LEFT JOIN 
Returns all records from the left table, and the matched records from the right table. 

## What is a Stored Procedure?
A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.
So if you have an SQL query that you write over and over again, save it as a stored procedure, and then just call it to execute it.
You can also pass parameters to a stored procedure, so that the stored procedure can act based on the parameter value(s) that is passed.

Create

    CREATE PROCEDURE procedure_name
    AS
    sql_statement
    GO;

    CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
    AS
    SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode
    GO;

Invoke 

    EXEC procedure_name;

    EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';






## Query for exact word
SELECT * FROM Customers where city = "Berlin";

## Query for like or wild cards
SELECT * FROM Customers where city LIKE "%erli%";

Wildcard characters are used with the SQL LIKE operator. The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

```
LIKE Operator	                Description
WHERE CustomerName LIKE 'a%'	Finds any values that starts with "a"
WHERE CustomerName LIKE '%a'	Finds any values that ends with "a"
WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position
WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position
WHERE CustomerName LIKE 'a_%_%'	Finds any values that starts with "a" and are at least 3 characters in length
WHERE ContactName LIKE 'a%o'	Finds any values that starts with "a" and ends with "o"
```

## Query challenges
### second highest salary
    Sorting solution
    select (SELECT DISTINCT salary FROM employee ORDERBY salary DESC LIMIT 1 OFFSET 1) as SecondHighestSalary;

    Nested query 
    SELECT max(salary) FROM employee WHERE salary not in (SELECT max(salary) FROM employee)

