# Identify and use the processes and terminology used in designing a RDBMS

## 30th Sept 2025

### Abstract

----------------------------------------------

#### Overview

Database normalization is the process of structuring relational databases in a way that reduces data redundancies and increases data integrity by reducing anomalies. It is accomplished by adhering to so-called normal forms that are sets of progressively strict rules constraining the database.

A relational database is an abstract idea of tables (entities) wherein columns (fields/attributes) and rows (records) are related in some way to columns and rows of other tables. There are three degrees of relationships in relational databases. Those are:

1. One-to-many Relationship: Here, one record from table A can be associated with multiple records in table B.

2. Many-to-many Relationship: Here, multiple records from table A can be associated with multiple records in table B.

3. One-to-one Relationship: Here, only one record from table A can be associated with a single record in table B.

A relational database management system (RDBMS) is software that provides tools necessary for creation and management of such tables, and for interaction with their data. An example here could be the `sqlite3` python library. It provides:

- tools to **create, read, update, and delete** (CRUD) data,

- a query language (SQL),

- enforcement of relational concepts such as **primary keys and foreign keys.



### Identifying Entities

The first task in creating every database, completed during entity relationship modeling (ER Modeling), is identifying entities.

At this stage, entity is not yet a table, it is instead an object with attributes, either real life or abstract object that you're trying to express/represent using a table. an example here could be employees, cars, sales ... Pretty much anything.





Those relationships are usually enforced by utilization of a concept called unique identifiers (UIDs).  Those are single fields or collections of fields that 



Those are fields wherein every value is unique, i.e. does not repeat in the same field in the same entity. Every entity should have at least one UID. 

The primary function of a UID is identification of records which is instrumental in precise targetting of the record during CRUD operations.

There are 



**

### Normal forms

#### Unnormalized Form (UNF)

An unnormalized form does not meet any normalization criteria defined by further forms. It is usually the first step in building a database, before normalization. At this point in time you will have identified entities (tables), defined degrees of relationship (1:1/1:M/M:M), and devised main unique identifiers (primary and composite keys).

An example database at this point in time may look like this:

| Employees | Employee ID:PK | Name              | Salary |
| --------- | -------------- | ----------------- | ------ |
|           | 0              | Charles McCrimmon | $1     |

| Wages | Employee ID:FK | Hours Worked | Pay this week |
| ----- | -------------- | ------------ | ------------- |
|       | 0              | 60           | $0.028        |

This database defines the entities (Employees and Wages), degrees of relationship (1:1), and unique identifiers (Employee ID), but doesn't yet comply with 1NF because the **Name** attribute is not atomic.

#### First Normal Form (1NF)

The first normal form enforces atomicity of fields. In this form, every field must be **atomic**, i.e. indivisable.

An atomic field is a field that holds a **single indivisable** value. **Single** means that it cannot be a collection of values such as a list. **Indivisable** means that the value cannot be logically divided any further; it constitutes a single whole value.

For example, the following table is NOT atomic:

<table>
<tr>
<th>Employee ID:PK</th>
<th>Name</th>
</tr>
<tr>
<td>0</td>
<td>Charles McCrimmon</td>
</tr>
</table>

Here, the first name and surname are combined into a single field - **Name**. To enforce atomicity in this table, we need to split them:

| Employee ID:PK | Name    | Surname   |
| -------------- | ------- | --------- |
| 0              | Charles | McCrimmon |

#### Second Normal Form (2NF)

The second normal form eliminates **partial dependencies**. 

A partial dependency occurs when a non-key attribute is dependent on only a part of a composite key instead of the whole key. For example:

<table>
  <tr>
     <th>Order ID:PK</th>
     <th>Product ID:FK</th>
     <th>Product Name</th>
     <th>Quantity</th>
  </tr>
  <tr>
     <td>0</td>
     <td>403</td>
     <td>Fruit</td>
     <td>1</td>
  </tr>
</table>

In here, **Product Name** attribute is only *really* dependent on **Product ID**, but you need both **Order ID** and **Product ID** to access it. This is a **partial dependency.** To now make this table compliant with 2NF, we need to eliminate it:

<table>
<tr>
<th>Order ID:PK</th>
<th>Product ID:FK</th>
<th>Quantity</th>
</tr>
<tr>
<td>0</td>
<td>403</td>
<td>1</td>
</tr>
</table>

<table>
<tr>
    <th>Product ID:PK</th>
    <th>Product Name</th>
    <th>Origin</th>
<tr>
    <td>403</td>
    <td>Fruit</td>
    <td>Eden</td>
</table>

Now **Product Name** is only dependent on **Product ID**, and only that is required to retrieve it.

#### Third Normal Form (3NF)

The third normal form eliminates **transitive dependencies.**

A transitive dependency occurs when a non-key attribute is dependent on another non-key attribute. If B depends on A, and C depends on B, then C commits transitive dependency because it also depends on A. For example, the following table has a transitive dependency:

<table>
<tr>
<th>Entry ID:PK</th>
<th>Date</th>
<th>Day Of Week</th>
</tr>
<tr>
<td>0</td>
<td>3/10/2025</td>
<td>Friday</td>
</tr>
</table>

Here, **Date**, which is a non-key attribute, depends on **Entry ID**, and **Day Of Week**, which is also a non-key attribute, depends on **Date**. Now to resolve this to 3NF:

<table>
<tr>
<th>Entry ID:PK</th>
<th>Date:FK</th>
</tr>
<tr>
<td>0</td>
<td>3/10/2025</td>
</tr>
</table>

<table>
<tr>
<th>Date:PK</th>
<th>Day Of Week</th>
</tr>
<tr>
<td>3/10/2025</td>
<td>Friday</td>
</tr>
</table>

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

[Third Normal Form (3NF) - GeeksforGeeks](https://www.geeksforgeeks.org/dbms/third-normal-form-3nf/)

https://wit-hdip-computer-science.github.io/semester-1-databases/topic04/talk-3/UIDs.pdf

[Data Preparation: Unique Identifiers &ndash; DataRails](https://support.datarails.com/hc/en-us/articles/11047617937181-Data-Preparation-Unique-Identifiers)
