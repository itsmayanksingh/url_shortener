
import pyshorteners

link = input("enter the link: ")

shortener = pyshorteners.Shortener()

shortened_link = shortener.tinyurl.short(link)
print(shortened_link)
