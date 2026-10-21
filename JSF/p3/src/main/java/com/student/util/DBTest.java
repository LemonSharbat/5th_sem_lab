package com.student.util;

import java.sql.Connection;

public class DBTest {

	public static void main(String[] args) {

		try {
			Connection conn = DBUtil.getConnection();
			System.out.println(conn);
			conn.close();
		} catch (Exception e) {
			System.out.println("Error!");
		}
	}

}
