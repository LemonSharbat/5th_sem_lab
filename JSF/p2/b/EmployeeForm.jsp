
<!DOCTYPE html>
<html>
<head>
    <title>Employee Form</title>
</head>
<body>
    <h2>Employee Information Form</h2>

    <form action="EmployeeResult.jsp" method="post">
        Employee ID: <input type="text" name="employeeId" required><br><br>

        Name: <input type="text" name="name" required><br><br>

        Age: <input type="number" name="age" required><br><br>

        Department:
        <select name="department" required>
            <option value="">Select</option>
            <option value="HR">HR</option>
            <option value="Finance">Finance</option>
            <option value="IT">IT</option>
            <option value="Sales">Sales</option>
        </select><br><br>

        Email: <input type="email" name="email" required><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
