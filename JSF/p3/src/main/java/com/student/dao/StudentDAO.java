package com.student.dao;

import com.student.model.Student;
import com.student.util.DBUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class StudentDAO {

    // CREATE: Insert a new student
    public void addStudent(Student student) throws SQLException {

        String query =
                "INSERT INTO student (roll_no, name, email, age) " +
                "VALUES (?, ?, ?, ?)";

        try (Connection con = DBUtil.getConnection();
             PreparedStatement ps = con.prepareStatement(query)) {

            ps.setInt(1, student.getRollNo());
            ps.setString(2, student.getName());
            ps.setString(3, student.getEmail());
            ps.setInt(4, student.getAge());

            ps.executeUpdate();
        }
    }

    // READ: Retrieve all students
    public List<Student> getAllStudents() throws SQLException {

        List<Student> students = new ArrayList<>();

        String query = "SELECT * FROM student ORDER BY roll_no";

        try (Connection con = DBUtil.getConnection();
             PreparedStatement ps = con.prepareStatement(query);
             ResultSet rs = ps.executeQuery()) {

            while (rs.next()) {

                Student student = new Student();

                student.setRollNo(rs.getInt("roll_no"));
                student.setName(rs.getString("name"));
                student.setEmail(rs.getString("email"));
                student.setAge(rs.getInt("age"));

                students.add(student);
            }
        }

        return students;
    }

    // UPDATE: Modify an existing student
    public void updateStudent(Student student) throws SQLException {

        String query =
                "UPDATE student SET name = ?, email = ?, age = ? " +
                "WHERE roll_no = ?";

        try (Connection con = DBUtil.getConnection();
             PreparedStatement ps = con.prepareStatement(query)) {

            ps.setString(1, student.getName());
            ps.setString(2, student.getEmail());
            ps.setInt(3, student.getAge());
            ps.setInt(4, student.getRollNo());

            ps.executeUpdate();
        }
    }

    // DELETE: Remove a student
    public void deleteStudent(int rollNo) throws SQLException {

        String query = "DELETE FROM student WHERE roll_no = ?";

        try (Connection con = DBUtil.getConnection();
             PreparedStatement ps = con.prepareStatement(query)) {

            ps.setInt(1, rollNo);

            ps.executeUpdate();
        }
    }
}
