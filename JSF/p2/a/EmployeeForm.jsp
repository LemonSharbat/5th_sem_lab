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
        Department: <input type="text" name="department" required><br><br>
        Email: <input type="email" name="email" required><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
