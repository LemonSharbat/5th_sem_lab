<%@ page language="java"
         contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>

<%@ page import="com.student.dao.StudentDAO" %>
<%@ page import="com.student.model.Student" %>
<%@ page import="java.sql.SQLException" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Add Student</title>
</head>
<body>

    <h2>Add Student</h2>

    <form action="add-student.jsp" method="post">

        Roll No:
        <input type="number" name="rollNo" required>
        <br><br>

        Name:
        <input type="text" name="name" maxlength="150" required>
        <br><br>

        Email:
        <input type="email" name="email" maxlength="150" required>
        <br><br>

        Age:
        <input type="number" name="age" min="1" max="150" required>
        <br><br>

        <input type="submit" value="Add Student">

    </form>

    <%
        if ("POST".equalsIgnoreCase(request.getMethod())) {

            try {
                int rollNo = Integer.parseInt(
                    request.getParameter("rollNo"));

                String name = request.getParameter("name");
                String email = request.getParameter("email");

                int age = Integer.parseInt(
                    request.getParameter("age"));

                Student student =
                    new Student(rollNo, name, email, age);

                StudentDAO dao = new StudentDAO();

                dao.addStudent(student);

                out.println(
                    "<p>Student added successfully!</p>");

            } catch (NumberFormatException e) {

                out.println(
                    "<p>Error: Roll number and age must be integers.</p>");

            } catch (SQLException e) {

                application.log("Error adding student", e);

                out.println(
                    "<p>Unable to add student. Check the database connection "
                    + "and ensure the roll number is not already in use.</p>");
            }
        }
    %>

    <br>
    <a href="index.jsp">Back to Home</a>
    <br>
    <a href="list-student.jsp">View Students</a>

</body>
</html>
