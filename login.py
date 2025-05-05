#!/usr/bin/python3
import cgi
import sys
from utils import validate_credentials, render_template


# Process form data
form = cgi.FieldStorage()

# Output HTTP header
print("Content-Type: text/html")

# Validate form inputs
if "username" not in form or "password" not in form:
    html = render_template(
        "error.html",
        {"message": "Missing form data", "link_url": "login.html", "link_text": "Go back"}
    )
    print()  # blank line before HTML
    print(html)
    sys.exit()

# Extract form values
username = form["username"].value
password = form["password"].value

# Authenticate user
if not validate_credentials(username, password):
    html = render_template(
        "error.html",
        {"message": "Invalid username or password", "link_url": "login.html", "link_text": "Go back"}
    )
    print()  # blank line before HTML
    print(html)
else:
    # Set session cookie for logged-in user
    print(f"Set-Cookie: username={username}; Path=/")
    print()  # blank line before HTML
    html = render_template(
        "success.html",
        {"message": "Login successful", "link_url": "tours.html", "link_text": "View Tours"}
    )
    print(html)
