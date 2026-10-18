package com.practice;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/SessionServlet")
public class SessionServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        String url = request.getContextPath() + "/SessionServlet";
        String action = request.getParameter("action");

        // Logout
        if ("logout".equals(action)) {
            HttpSession session = request.getSession(false);

            if (session != null) {
                session.invalidate();
            }

            response.sendRedirect(url);
            return;
        }

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        HttpSession session = request.getSession(false);

        // Display welcome page if logged in
        if (session != null && session.getAttribute("username") != null) {

            String username = (String) session.getAttribute("username");

            out.println("<html><body>");
            out.println("<h2>Welcome, " + username + "!</h2>");
            out.println("<a href='" + url + "?action=logout'>Logout</a>");

            out.println("<h3>Session Information</h3>");
            out.println("<p>Session ID: " + session.getId() + "</p>");
            out.println("<p>Creation Time: "
                    + new Date(session.getCreationTime()) + "</p>");
            out.println("<p>Last Accessed Time: "
                    + new Date(session.getLastAccessedTime()) + "</p>");

            out.println("</body></html>");

        } else {
            // Display login form
            out.println("<html><body>");
            out.println("<h2>Login</h2>");

            out.println("<form method='post' action='" + url + "'>");
            out.println("Username: <input type='text' name='username' required><br><br>");
            out.println("Password: <input type='password' name='password' required><br><br>");
            out.println("<input type='submit' value='Login'>");
            out.println("</form>");

            out.println("</body></html>");
        }
    }

    @Override
    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response)
            throws ServletException, IOException {

        String username = request.getParameter("username");
        String password = request.getParameter("password");

        String url = request.getContextPath() + "/SessionServlet";

        // Validate login credentials
        if ("admin".equals(username) && "password".equals(password)) {

            HttpSession session = request.getSession(true);
            session.setAttribute("username", username);

            response.sendRedirect(url);

        } else {
            response.sendRedirect(url);
        }
    }
}
