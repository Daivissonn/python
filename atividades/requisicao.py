from urllib import request

cabeçalhos = {"User-Agent": "Mozilla/5.0",
              "cookie": "example_cookie=12345"}

req = request.Request("https://www.example.com", headers=cabeçalhos)
request = request.urlopen(req)
html = request.read()
print(html)

#esse codigo é fantastico, primeiro importamos uma biblioteca especifica de request chamada urllib, que nos permite fazer requisições http. criei uma variavel chamada cabeçalhos que contem um dicionario onde eu passo o hearders, que no caso seria os cookies e o user-agent, que é uma informação que identifica o navegador que está fazendo a requisição, o Cookie é fundamental pois se o site for subido pelo claudflare, ele vai bloquear a requisição se nao tiver o cookie correto, entao é importante passar o cookie correto para que a requisiçao seja aceita. criei a variavel req que recebe a request.Request, que é a função que cria a requisição, passando a url e os cabeçalhos. depois criei a variavel request que recebe a função request.urlopen(req), que é a função que envia a requisição para o servidor e recebe a resposta. depois criei a variavel html que recebe o conteúdo da resposta, usando o método read(). por fim, imprimi o conteúdo da resposta no console.