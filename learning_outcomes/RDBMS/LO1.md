# Identify and use the processes and terminology used in designing a RDBMS

## 30th Sept 2025

### Abstract

----------------------------------------------

Database normalization is the process of structuring relational databases in a way that reduces data redundancies and increases data integrity by reducing anomalies. It is accomplished by adhering to so-called normal forms that are sets of progressively strict rules constraining the database.

A relational database is an abstract idea of tables wherein columns (fields) and rows (records) are related in some way to columns and rows of other tables. A relational database management system (RDBMS) is software that provides tools necessary for creation and management of such tables, and for interaction with their data. An example here could be the `sqlite3` python library. It provides:

* tools to **create, read, update, and delete** (CRUD) data,

* a query language (SQL),

* enforcement of relational concepts such as **primary keys and foreign keys.**



There are three types of relationships in relational databases. Those are:

1. One-to-many Relationship: In this relationship, one record from table A can be associated with multiple records in table B.

2. Many-to-many Relationship: In this relationship, multiple records from table A can be associated with multiple records in table B.

3. One-to-one Relationship: 



Relational databases define two concepts called Entities and Attributes. An entity is a category of the thing or person you're trying to describe; for example an employee. An attribute is what you can use to describe that object with; for example, every employee has an ID and salary.







### Body Section

----------------------------------------------

### Personal Experience

----------------------------------------------

[link to LO]

### References

----------------------------------------------

[Database Normalization – Normal Forms 1nf 2nf 3nf Table Examples](https://www.freecodecamp.org/news/database-normalization-1nf-2nf-3nf-table-examples/)

[Normal Forms in DBMS - GeeksforGeeks](https://www.geeksforgeeks.org/dbms/normal-forms-in-dbms/)

[Database normalization - Wikipedia](https://en.wikipedia.org/wiki/Database_normalization)

https://cloud.google.com/learn/what-is-a-relational-database

https://medium.com/@ethan.duong1120/8-critical-concepts-in-relational-database-80c74aa15e9c

[Partial Dependency in DBMS - GeeksforGeeks](https://www.geeksforgeeks.org/dbms/partial-dependency-in-dbms/)

[Identifying Entities and Attributes - InterBase](https://docwiki.embarcadero.com/InterBase/2020/en/Identifying_Entities_and_Attributes)

https://www.ibm.com/docs/en/eamfoc/7.6.0?topic=structure-database-relationships
