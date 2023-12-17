import httpx

urls = [
        'https://www.free-proxy-list.net/',
        'https://www.sslproxies.org/',
        'https://free-proxy-list.net/anonymous-proxy.html',
        'https://free-proxy-list.net/',
        'https://www.freeproxy.world/?type=http&anonymity=&country=&speed=&port=&page=1',
]

with open("proxies.txt", 'w') as file:
    for url in urls:
        response = httpx.get(url)
        file.write(response.text + "\n")