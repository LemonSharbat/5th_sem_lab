package com.student.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBUtil {

    private static final String URL =
            "jdbc:mysql://localhost:3306/student";

    private static final String USERNAME = "root";

    private static final String PASSWORD = "root123";

    // Method to establish a database connection
    public static Connection getConnection() throws SQLException {

        try {
            // Load the MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

        } catch (ClassNotFoundException e) {
            throw new SQLException("MySQL JDBC Driver not found.", e);
        }

        // Return the database connection
        return DriverManager.getConnection(URL, USERNAME, PASSWORD);
    }
}
