**JDBC – Java Database Connectivity**

---

### What is JDBC?

**JDBC** is an API in Java that defines how a Java program can talk to a database.
It gives you methods to:

* connect to a database,
* run SQL queries,
* update data,
* read results.

---

### Why is JDBC needed?

We need JDBC because:

* Java apps often need to store and read data from databases (MySQL, PostgreSQL, etc.).
* Different databases have different low-level protocols.
* JDBC gives **one standard interface** so you can write mostly database-independent code.

---

### Types of JDBC Drivers

1. **JDBC-ODBC Bridge Driver** (Type 1)
2. **Native-API Driver** (Type 2)
3. **Network Protocol Driver** (Type 3)
4. **Thin Driver** / Pure Java Driver (Type 4)

Type 4 (Thin Driver) is what you realistically use with MySQL today.

---

### JDBC Workflow / Steps

1. **Import the package**
   `import java.sql.*;`

2. **Load/Register the driver**
   a. Load the driver class
   `Class.forName("com.mysql.jdbc.Driver");`
   b. (Alternative) Manually register the driver
   `DriverManager.registerDriver(new com.mysql.jdbc.Driver());`

3. **Establish the connection**
   `Connection con = DriverManager.getConnection(url, username, password);`

4. **Create the statement**
   There are 3 main types:

   * `Statement`
   * `PreparedStatement`
   * `CallableStatement`

5. **Execute the query** (SELECT / INSERT / UPDATE / DELETE)

6. **Process the results** (read rows from ResultSet)

7. **Close all resources** (ResultSet, Statement, Connection)

---

### Basic Example

```java
import java.sql.*; // step 1

public static void main(String[] args) throws Exception {

    // Step 2: Load/Register Driver
    Class.forName("com.mysql.jdbc.Driver"); // step 2
    DriverManager.registerDriver(new com.mysql.jdbc.Driver()); // step 2 alternative

    // Step 3: Connection (3 parameters - url, username, password)
    Connection con = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/dbname",
        "username",
        "password"
    );

    // Step 4: Create Statement
    Statement stmt = con.createStatement();

    // Step 5: Execute Query
    ResultSet rs = stmt.executeQuery("select * from tablename");

    // Step 6: Process Results
    while (rs.next()) {
        System.out.println(rs.getInt(1) + " " + rs.getString(2));
    }

    // Step 7: Close Resources
    rs.close();
    stmt.close();
    con.close();
}
```

---

### Full Example (Reading from DB)

Scenario:

* Database: `school`
* Table: `students(id, name)`
* We first create the DB/table and insert some data in MySQL Workbench.
* Then Java code connects and prints all rows.

```java
import java.sql.*;

public class JdbcExample {
    public static void main(String[] args) {
        try {
            // Step 2: Load and register the JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Step 3: Establish the connection
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/school",
                "root",
                "password"
            );

            // Step 4: Create the statement
            Statement stmt = con.createStatement();

            // Step 5: Execute the query
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");

            // Step 6: Process results
            while (rs.next()) {
                System.out.println(
                    "ID: " + rs.getInt("id") +
                    ", Name: " + rs.getString("name")
                );
            }

            // Step 7: Close the connection
            rs.close();
            stmt.close();
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### Insert Data Example

```java
import java.sql.*;

public class JdbcInsertExample {
    public static void main(String[] args) {
        try {
            // Step 2: Load and register the JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Step 3: Establish the connection
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/school",
                "root",
                "password"
            );

            // Step 4: Create the statement
            Statement stmt = con.createStatement();

            // Step 5: Execute the insert query
            String sql = "INSERT INTO students (id, name) VALUES (1, 'John Doe')";
            stmt.executeUpdate(sql);
            System.out.println("Record inserted successfully");

            // Step 7: Close the connection
            stmt.close();
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### When to Use Which Statement Type?

1. **Statement**

   * Use for static SQL with **no parameters**.
   * Example: `"SELECT * FROM students"`

2. **PreparedStatement**

   * Use when the SQL needs **parameters (?)**.
   * Helps prevent SQL injection.
   * Better performance for repeated queries.

3. **CallableStatement**

   * Use to call **stored procedures** in the database.

---

### PreparedStatement Example

```java
import java.sql.*;

public class JdbcPreparedStatementExample {
    public static void main(String[] args) {
        try {
            // Step 2: Load and register the JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Step 3: Establish the connection
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/school",
                "root",
                "password"
            );

            // Step 4: Create the PreparedStatement
            String sql = "INSERT INTO students (id, name) VALUES (?, ?)";
            PreparedStatement pstmt = con.prepareStatement(sql);

            // Set parameters
            pstmt.setInt(1, 2);
            pstmt.setString(2, "Jane Smith");

            // Step 5: Execute the insert query
            pstmt.executeUpdate();
            System.out.println("Record inserted successfully");

            // Step 7: Close the connection
            pstmt.close();
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

## Understanding `Class.forName()`

Before JDBC, understand normal class loading in Java.

### Example:

```java
public class DemoClass {
    public static void main(String[] args) {
        Pqr obj = new Pqr();
    }
}

class Pqr {
    static {
        System.out.println("in Static block");
    }
    // instance block
    {
        System.out.println("in instance block");
    }
}
```

**Output when running DemoClass:**

```
in Static block
in instance block
```

Why?

* When you create `new Pqr()`, first:

  * The class `Pqr` is loaded → its `static` block runs once.
  * Then the object is created → its instance block runs.

Now: what if you **don’t** create an object, but you still want to trigger only the static block?

You can do this:

```java
public class DemoClass {
    public static void main(String[] args) throws ClassNotFoundException {
        Class.forName("Pqr");
    }
}
```

* `Class.forName("Pqr")` tells the JVM: load class `Pqr`.
* When the class loads, its static block runs.
* No object is created, so the instance block doesn't run.

If you write:

```java
Class.forName("Pqr").newInstance();
```

* First: class loads → static block runs.
* Then: `newInstance()` creates an object → instance block runs too.

So:

* `Class.forName("SomeClass")` → triggers static block.
* `Class.forName("SomeClass").newInstance()` → triggers static + instance.

---

## Back to JDBC Driver Loading

These two lines:

```java
Class.forName("com.mysql.jdbc.Driver");        // option 1
DriverManager.registerDriver(new com.mysql.jdbc.Driver()); // option 2
```

How are they related?

* `Class.forName("com.mysql.jdbc.Driver")`

  * Loads the MySQL JDBC driver class into memory.
  * Inside that driver class, there is usually a `static` block.
  * That static block auto-registers the driver with `DriverManager`.

* `DriverManager.registerDriver(new com.mysql.jdbc.Driver())`

  * You manually create the driver object and register it with DriverManager.

In other words:

* Calling `Class.forName(...)` indirectly causes registration because of the driver's static block.
* Calling `DriverManager.registerDriver(...)` does the registration explicitly.

Effect: after either of these, `DriverManager.getConnection(...)` knows which driver to use to connect to the database.
