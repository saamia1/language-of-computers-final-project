import os

USERNAME = "username"
EMAIL = "email"

DATA_FILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DATA_FILE_PATH = os.path.join(DATA_FILE_DIR, "users.txt")
if not os.path.exists(DATA_FILE_DIR):
    os.makedirs(DATA_FILE_DIR)

# Create the data file if it doesn't exist
if not os.path.exists(DATA_FILE_PATH):
    with open(DATA_FILE_PATH, "w") as file:
        pass

# Create the contact file if it doesn't exist
CONTACT_FILE_PATH = os.path.join(DATA_FILE_DIR, "contact.txt")
if not os.path.exists(CONTACT_FILE_PATH):
    with open(CONTACT_FILE_PATH, "w") as file:
        pass

# Create the booking file if it doesn't exist
BOOKING_FILE_PATH = os.path.join(DATA_FILE_DIR, "booking.txt")
if not os.path.exists(BOOKING_FILE_PATH):
    with open(BOOKING_FILE_PATH, "w") as file:
        pass


def check_exists(string, type_):
    """
    Check if a string exists in the specified file.
    :param string: The string to check.
    :param type: The type of data to check (username or email).
    :return: True if the string exists, False otherwise.
    """
    with open(DATA_FILE_PATH, "r") as file:
        for line in file:
            username, password, email = line.strip().split(":")
            if type_ == "username" and username == string:
                return True
            elif type_ == "email" and email == string:
                return True
    return False


def create_user(username, password, email):
    """
    Create a new user and save it to the data file.
    :param username: The username of the new user.
    :param password: The password of the new user.
    :param email: The email of the new user.
    """
    with open(DATA_FILE_PATH, "a") as file:
        file.write(f"{username}:{password}:{email}\n")
    return True


def validate_credentials(input_username, input_password):
    """
    Check if the provided credentials match a stored user record by username or email.
    :param input_username: The username or email to check.
    :param input_password: The password to check.
    :return: True if the credentials are valid, False otherwise.
    """
    with open(DATA_FILE_PATH, "r") as file:
        for line in file:
            username, password, email = line.strip().split(":")
            if (username == input_username or email == input_username) and password == input_password:
                return True
    return False


def render_template(template_filename, context):
    """
    Load an HTML template and replace placeholders in the form {{key}} with context values.
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), template_filename)
    with open(path) as f:
        html = f.read()
    for key, value in context.items():
        html = html.replace("{{" + key + "}}", value)
    return html


def save_contact_form(name, email, message):
    """
    Save the contact form data to a file.
    :param name: The name of the person who filled out the form.
    :param email: The email of the person who filled out the form.
    :param message: The message from the contact form.
    """
    message = message.replace("\n", " ")
    message = message.replace(":", " ")
    with open(CONTACT_FILE_PATH, "a") as file:
        file.write(f"{name}:{email}:{message}\n")
    return True


def save_booking_form(username, date, quantity, location, notes):
    """
    Save the booking form data to a file.
    :param username: The user making the booking.
    :param date: The date of the tour.
    :param quantity: Number of spots booked.
    :param location: The tour location.
    :param notes: Special requests or notes.
    """
    notes = notes.replace("\n", " ")
    notes = notes.replace(":", " ")
    with open(BOOKING_FILE_PATH, "a") as file:
        file.write(f"{username}:{date}:{quantity}:{location}:{notes}\n")
    return True


def get_current_username():
    """
    Parse the HTTP_COOKIE environment variable and return the current username cookie, or None if not set.
    """
    import os
    cookies = os.environ.get('HTTP_COOKIE', '')
    for kv in cookies.split(';'):
        parts = kv.strip().split('=', 1)
        if len(parts) == 2 and parts[0] == USERNAME:
            return parts[1]
    return None
