
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<!DOCTYPE html>
<html>
<head>
    <title>Employee Result</title>
</head>
<body>
    <h2>Employee Information Result</h2>

    <%
        String employeeId = request.getParameter("employeeId");
        String name = request.getParameter("name");
        String ageStr = request.getParameter("age");
        String department = request.getParameter("department");
        String email = request.getParameter("email");

        String employeeIdError = "";
        String nameError = "";
        String ageError = "";
        String departmentError = "";
        String emailError = "";

        boolean isValid = true;
        int age = 0;

        // Validate Employee ID
        if (employeeId == null || employeeId.trim().isEmpty()) {
            employeeIdError = "Employee ID is required.";
            isValid = false;
        }

        // Validate Name
        if (name == null || !name.matches("[a-zA-Z ]+")) {
            nameError = "Name must contain only letters and spaces.";
            isValid = false;
        }

        // Validate Age
        try {
            age = Integer.parseInt(ageStr);

            if (age < 18 || age > 65) {
                ageError = "Age must be between 18 and 65.";
                isValid = false;
            }
        } catch (NumberFormatException e) {
            ageError = "Age must be a valid number.";
            isValid = false;
        }

        // Validate Department
        if (department == null ||
            !department.matches("HR|Finance|IT|Sales")) {
            departmentError = "Please select a valid department.";
            isValid = false;
        }

        // Validate Email
        if (email == null ||
            !email.matches("[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}")) {
            emailError = "Enter a valid email, e.g. name@example.com.";
            isValid = false;
        }
    %>

    <% if (isValid) {
        int currentYear = java.util.Calendar.getInstance()
                            .get(java.util.Calendar.YEAR);

        int birthYear = currentYear - age;
        String nameAndDepartment = name + " (" + department + ")";
        String formattedEmail = email.toLowerCase();
    %>

        <table border="1">
            <tr>
                <th>Employee ID</th>
                <td><%= employeeId %></td>
            </tr>
            <tr>
                <th>Name and Department</th>
                <td><%= nameAndDepartment %></td>
            </tr>
            <tr>
                <th>Birth Year</th>
                <td><%= birthYear %></td>
            </tr>
            <tr>
                <th>Formatted Email</th>
                <td><%= formattedEmail %></td>
            </tr>
        </table>

    <% } else { %>

        <h3>Validation Errors</h3>

        <ul>
            <% if (!employeeIdError.isEmpty()) { %>
                <li><b>Employee ID:</b> <%= employeeIdError %></li>
            <% } %>

            <% if (!nameError.isEmpty()) { %>
                <li><b>Name:</b> <%= nameError %></li>
            <% } %>

            <% if (!ageError.isEmpty()) { %>
                <li><b>Age:</b> <%= ageError %></li>
            <% } %>

            <% if (!departmentError.isEmpty()) { %>
                <li><b>Department:</b> <%= departmentError %></li>
            <% } %>

            <% if (!emailError.isEmpty()) { %>
                <li><b>Email:</b> <%= emailError %></li>
            <% } %>
        </ul>

        <a href="EmployeeForm.jsp">Go back to the form</a>

    <% } %>

</body>
</html>
