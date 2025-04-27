#!/usr/bin/python3

import cgi
from utils import save_contact_form

print("Content-Type: text/html \n\n")


data = cgi.FieldStorage()


def headHTML():
    print("""

        <!DOCTYPE HTML>
        <head>
        <title> Contact Us </title>
        <link rel="stylesheet" href="assets/css/main.css" />
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
                                        <li><a href="tours.html" class="button primary fit">Tours</a></li>
                                        <li><a href="login.html" class="button fit">Log In</a></li>
                                        <li><a href="signup.html" class="button fit">Sign Up</a></li>
                                </ul>
                        </nav>

                <hr>

                        <section id="main" class="wrapper">
                                <div class="inner">
                                        <header class="major"><h2>Contact Us</h2></header>



                """)


def endHTML():
    print("""
                                <ul class="actions">
                                        <li><a href="tours.html" class="button next">Browse Tours</a></li>
                                </ul>
                                </div>
                        </section>
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
                </div>

                <!-- Scripts -->
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


def contact():

    name = data['name'].value

    email = data['email'].value
    message = data['message'].value

    save_contact_form(name, email, message)

    print("<h4> Thank you for reaching out,", name, ". We will get back to you shortly! </h4>")
    # print("<a href='index.html' class='logo'><strong>TravelHub</strong></a> ")
    print("<hr>")


headHTML()
contact()
endHTML()
