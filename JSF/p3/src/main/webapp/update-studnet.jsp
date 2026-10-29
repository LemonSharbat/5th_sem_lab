<%@ page language="java"
         contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>

<%@ page import="com.student.dao.StudentDAO" %>
<%@ page import="java.sql.SQLException" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Delete Student</title>
</head>
<body>

    <h2>Delete Student</h2>

    <%
        String rollNoStr = request.getParameter("rollNo");

        if ("POST".equalsIgnoreCase(request.getMethod())) {

            try {
                int rollNo = Integer.parseInt(rollNoStr);

                StudentDAO dao = new StudentDAO();

                dao.deleteStudent(rollNo);

                response.sendRedirect("list-student.jsp");
                return;

            } catch (NumberFormatException e) {

                out.println("<p>Invalid roll number.</p>");

            } catch (SQLException e) {

                application.log("Error deleting student", e);

                out.println("<p>Unable to delete the student.</p>");
            }
        }

        if (rollNoStr != null && !rollNoStr.trim().isEmpty()) {
    %>

            <p>
                Are you sure you want to delete the student
                with Roll No <%= rollNoStr %>?
            </p>

            <form action="delete-student.jsp" method="post">

                <input type="hidden"
                       name="rollNo"
                       value="<%= rollNoStr %>">

                <input type="submit" value="Confirm Delete">

            </form>

    <%
        } else {
    %>

            <p>No roll number was provided.</p>

    <%
        }
    %>

    <br>
    <a href="list-student.jsp">Back to Student List</a>

</body>
</html>
