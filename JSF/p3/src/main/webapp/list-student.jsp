<%@ page language="java"
         contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>

<%@ page import="com.student.dao.StudentDAO" %>
<%@ page import="com.student.model.Student" %>
<%@ page import="java.util.List" %>
<%@ page import="java.sql.SQLException" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>List Students</title>
</head>
<body>

    <h2>Student List</h2>

    <table border="1" cellpadding="8">

        <tr>
            <th>Roll No</th>
            <th>Name</th>
            <th>Email</th>
            <th>Age</th>
            <th>Actions</th>
        </tr>

        <%
            try {
                StudentDAO dao = new StudentDAO();

                List<Student> students = dao.getAllStudents();

                if (students.isEmpty()) {
        %>

                    <tr>
                        <td colspan="5">No students found.</td>
                    </tr>

        <%
                } else {

                    for (Student student : students) {
        %>

                        <tr>
                            <td><%= student.getRollNo() %></td>
                            <td><%= student.getName() %></td>
                            <td><%= student.getEmail() %></td>
                            <td><%= student.getAge() %></td>

                            <td>
                                <a href="update-student.jsp?rollNo=<%= student.getRollNo() %>">
                                    Update
                                </a>

                                |

                                <a href="delete-student.jsp?rollNo=<%= student.getRollNo() %>">
                                    Delete
                                </a>
                            </td>
                        </tr>

        <%
                    }
                }

            } catch (SQLException e) {

                application.log("Error retrieving students", e);
        %>

                <tr>
                    <td colspan="5">
                        Unable to retrieve student records.
                        Check the database connection.
                    </td>
                </tr>

        <%
            }
        %>

    </table>

    <br>

    <a href="add-student.jsp">Add New Student</a>
    <br><br>

    <a href="index.jsp">Back to Home</a>

</body>
</html>
