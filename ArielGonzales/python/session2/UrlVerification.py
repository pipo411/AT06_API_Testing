import re


def url_verification(url):
    if (re.search("^http://", url) and re.search(" $", url)):
        return url
    else:
        return "Is not a valid URL"


print(url_verification("http://www.google.com "))
print(url_verification("http://www.google.com"))
print(url_verification("http://www.youtube.com "))
print(url_verification("https://www.facebook.com "))
print(url_verification("HTTP://www.facebook.com "))
