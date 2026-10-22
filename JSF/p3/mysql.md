

MySQL JDBC Connection URL
```
jdbc:mysql://localhost:3306/database_name
```

### mysql shell 

```sh
mysql -u root -p

# password: root123
```

```sql
SHOW DATABASES;
```

```sql
CREATE DATABASE student;
```

Select the database
```sql
USE student;
```

List all tables in the database
```sql
SHOW TABLES;
```

```sql
CREATE TABLE students (
  roll_no INT PRIMARY KEY,
  name VARCHAR(150),
  email VARCHAR(150),
  age INT
);

```

Table structure
```sql
DESCRIBE table_name;
```

Get the current database
```sql
SELECT DATABASE();
```

To check on which port MySQL is running on
```sql
SELECT @@PORT;
```
