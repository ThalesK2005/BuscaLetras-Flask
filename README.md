# BuscaLetras-Flask 

Aplicação web desenvolvida em Python (Flask) que consome a API pública `lyrics.ovh` para buscar e exibir letras de músicas. 

##  Entendendo o Código (Como funciona)

O fluxo do sistema é direto e acontece em 4 etapas principais:

### 1. A Interação (Front-end)
O arquivo `index.html` possui um formulário (`<form>`) configurado com `method="GET"`. Quando o usuário digita a banda e a música e clica em pesquisar, os dados viajam pela própria URL (ex: `/?Banda=Linkin+Park&Musica=Numb`).

### 2. A Captura de Dados (Flask)
No back-end, a rota `@app.route("/")` "escuta" essa requisição. Através do objeto `request.args.get()` do Flask, o sistema captura exatamente os valores que foram passados nos inputs do HTML.

### 3. O Consumo da API (Requests)
Um teste lógico (`if`) verifica se os campos não estão vazios. Se estiver tudo certo, a função `buscar_letras()` entra em ação. Ela utiliza a biblioteca `requests` para montar a URL dinâmica e fazer um GET na API externa:
`https://api.lyrics.ovh/v1/{banda}/{musica}`
O retorno é um pacote JSON, do qual o Python extrai e guarda apenas o conteúdo da chave `["lyrics"]`.

### 4. A Entrega (Jinja2)
Com a letra salva na memória, o Flask usa o `render_template` para devolver a página ao usuário, enviando a letra junto. No HTML, o Jinja2 (`{{ letra }}`) injeta o texto dentro de uma tag `<pre>`, garantindo que todas as quebras de linha originais da música sejam mantidas na tela.

##  Stack Tecnológica
- **Python + Flask:** Construção do back-end e rotas.
- **Requests:** Requisições HTTP para a API.
- **Jinja2:** Renderização dinâmica de variáveis no front-end.
- **HTML:** Estruturação da interface.
