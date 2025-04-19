#!/usr/bin/python3
import cgi
import sys
from utils import check_exists, render_template, create_user, USERNAME, EMAIL


# Process form data
form = cgi.FieldStorage()

print("Content-Type: text/html\n\n")

if "username" not in form or "password" not in form or "email" not in form:
    # Render missing-data error page
    html = render_template("error.html", {"message": "Missing form data",
                           "link_url": "signup.html", "link_text": "Go back"})
    print(html)
    sys.exit()

username = form["username"].value
password = form["password"].value
email = form["email"].value

# Check if username or email already exists
if check_exists(username, USERNAME):
    # Render username-taken error page
    html = render_template("error.html", {"message": "Username already exists",
                           "link_url": "signup.html", "link_text": "Go back"})
    print(html)
elif check_exists(email, EMAIL):
    # Render email-taken error page
    html = render_template("error.html", {"message": "Email already exists",
                           "link_url": "signup.html", "link_text": "Go back"})
    print(html)

else:
    # Save new user and render success page
    create_user(username, password, email)

    # Render success page
    html = render_template("success.html", {"message": "Registration successful",
                           "link_url": "login.html", "link_text": "Login"})
    print(html)
