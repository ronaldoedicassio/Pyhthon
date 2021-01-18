import urllib.request

try:
    site: urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Site não esta disponivel')
else:
    print('Site disponivel')