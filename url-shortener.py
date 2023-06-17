
import pyshorteners

user_input_irl = input("Enter a URL to shorten it: ")
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(user_input_irl)

print(short_url)