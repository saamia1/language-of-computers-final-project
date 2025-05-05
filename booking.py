#!/usr/bin/python3

import cgi
import os
import sys
from utils import save_booking_form, get_current_username

# Session guard: redirect to login if not authenticated
user = get_current_username()
if not user:
    print("Status: 302 Found")
    print("Location: login.html")
    print()
    sys.exit()

# Define available destinations
DESTINATIONS = {
    'dubai': {'title': 'Dubai', 'img': 'images/pic05.webp', 'desc': 'Experience vibrant city lights, explore iconic landmarks, and discover a creative city where tradition meets innovation.'},
    'tokyo': {'title': 'Tokyo', 'img': 'images/pic04.avif', 'desc': 'Discover ancient temples, neon-lit districts, and the vibrant culture of Japan.'},
    'paris': {'title': 'Paris', 'img': 'images/pic01.jpg', 'desc': 'Iconic landmarks, world-class art, and scenic river strolls await in the heart of France.'},
    'seoul': {'title': 'Seoul', 'img': 'images/seoul.webp', 'desc': 'A dynamic blend of ancient traditions and cutting-edge technology in South Korea\'s vibrant capital.'},
    'zurich': {'title': 'Zurich', 'img': 'images/zurich.jpg', 'desc': 'Switzerland\'s largest city offers stunning lakeside views, alpine vistas, and world-class cultural attractions.'},
    'rome': {'title': 'Rome', 'img': 'images/rome.webp', 'desc': 'Explore the eternal city\'s ancient ruins, Renaissance masterpieces, and delectable cuisine in Italy\'s historic capital.'}
}

print("Content-Type: text/html\n")
form = cgi.FieldStorage()
method = os.environ.get('REQUEST_METHOD', 'GET')

# HTML header
print("""<!DOCTYPE HTML>
<html>
<head>
    <title>Booking - TravelHub</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
    <link rel="icon" href="images/favicon.png" />
</head>
<body class="is-preload">
    <div id="wrapper">  
        <header id="header" class="alt style2">  
            <a href="index.html" class="logo"><strong>TravelHub</strong></a>
            <nav><a href="#menu">Menu</a></nav>
        </header>
		<nav id="menu">
			<ul class="links">
				<li><a href="index.html">Home</a></li>
			</ul>
			<ul class="actions stacked">
				<li><a href="tours.html" class="button fit">Tours</a></li>
				<li><a href="booking.py" class="button primary fit">Booking Form</a></li>
				<li><a href="login.html" class="button fit">Log In</a></li>
				<li><a href="signup.html" class="button fit">Sign Up</a></li>
				<li><a href="contact.html" class="button fit">Contact Us</a></li>
			</ul>
		</nav>
      """)

# Handle GET requests
if method == 'GET':
    location = form.getfirst('location', '')
    if location in DESTINATIONS:
        dest = DESTINATIONS[location]
        # show destination banner and booking form
        print(f"""
<section id="banner" class="style2">
    <div class="inner">
        <span class="image"><img src="{dest['img']}" alt="{dest['title']}" /></span>
        <header class="major"><h1>{dest['title']}</h1></header>
        <div class="content"><p>{dest['desc']}</p></div>
    </div>
</section>
<section id="main" class="wrapper">
    <div class="inner">
        <header class="major"><h2>Book Your Tour</h2></header>
        <form method="post" action="booking.py">
            <input type="hidden" name="location" value="{location}" />
            <div class="fields">
                <div class="field half">
                    <label for="date">Date</label>
                    <input type="date" name="date" id="date" required />
                </div>
                <div class="field half">
                    <label for="quantity">Quantity</label>
                    <input type="number" name="quantity" id="quantity" min="1" value="1" required />
                </div>
                <div class="field">
                    <label for="notes">Notes</label>
                    <textarea name="notes" id="notes" rows="4" placeholder="Special requests..."></textarea>
                </div>
            </div>
            <ul class="actions">
                <li><input type="submit" value="Confirm Booking" class="primary" /></li>
            </ul>
        </form>
    </div>
</section>
""")
    else:
        # show dropdown to select location
        print(f"""
<section id="banner" class="style2">
    <div class="inner">
        <span class="image"><img src="images/pic04.avif" alt="Book Tour" /></span>
        <header class="major"><h1>Our Locations</h1></header>
        <div class="content"><p>Select a destination to begin booking your tour.</p></div>
    </div>
</section>
<section id="main" class="wrapper">
    <div class="inner">
        <header class="major"><h2>Choose Your Destination</h2></header>
        <form method="get" action="booking.py">
            <div class="field half">
                <label for="location">Location</label>
                <select name="location" id="location" required>
                    <option value="">-- Select Location --</option>
                    {''.join([f'<option value="{key}">{value["title"]}</option>' for key, value in DESTINATIONS.items()])}
                </select>
            </div>
            <ul class="actions">
                <li><input type="submit" value="Continue" class="primary" /></li>
            </ul>
        </form>
    </div>
</section>
""")

# Handle POST requests
elif method == 'POST':
    date = form.getfirst('date', '')
    quantity = form.getfirst('quantity', '')
    location = form.getfirst('location', '')
    notes = form.getfirst('notes', '')

    save_booking_form(user, date, quantity, location, notes)

    # show confirmation
    print(
        f"""
        <section id="main" class="wrapper"><div class="inner">
        <h4>Thank you for booking {DESTINATIONS.get(location, {}).get('title', location).capitalize()} on {date} for {quantity} guest(s). We will contact you with further details soon!</h4>
        <ul class="actions">
            <li><a href="tours.html" class="button next">Browse More Tours</a></li>
        </ul>
        </div></section>
        """
    )

# HTML footer
print("""
        <footer id="footer">
            <div class="inner">
                <ul class="icons">
                    <li><a href="#" class="icon brands alt fa-twitter"><span class="label">Twitter</span></a></li>
                    <li><a href="#" class="icon brands alt fa-facebook-f"><span class="label">Facebook</span></a></li>
                    <li><a href="#" class="icon brands alt fa-instagram"><span class="label">Instagram</span></a></li>
                    <li><a href="#" class="icon brands alt fa-github"><span class="label">GitHub</span></a></li>
                    <li><a href="#" class="icon brands alt fa-linkedin-in"><span class="label">LinkedIn</span></a></li>
                </ul>
                <ul class="copyright">
                    <li>&copy; TravelHub | Language of Computers Final Project</li>
                    <li>Design: <a href="https://html5up.net">HTML5 UP</a></li>
                </ul>
            </div>
        </footer>
    </div>

    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/jquery.scrolly.min.js"></script>
    <script src="assets/js/jquery.scrollex.min.js"></script>
    <script src="assets/js/browser.min.js"></script>
    <script src="assets/js/breakpoints.min.js"></script>
    <script src="assets/js/util.js"></script>
    <script src="assets/js/main.js"></script>
</body>
</html>
""")
