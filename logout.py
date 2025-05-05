#!/usr/bin/python3
import sys
# Clear the session cookie and redirect to home
print("Status: 302 Found")
print("Set-Cookie: username=; Max-Age=0; Path=/")
print("Location: index.html")
print()
sys.exit()
