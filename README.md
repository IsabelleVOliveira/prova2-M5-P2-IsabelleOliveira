# EC - Prova 2 - Parte 2- 2024-1A
Desenvolvido por Isabelle Beatriz Vasquez Oliveira

## Como executar a aplicação

&emsp;Para executar a aplicação, você deve instalar todos os requisitos do arquivo "requirements.txt" por meio do terminal com o comando "pip install -r requirements".

&emsp;Depois de garantir que todas as instalações foram realizadas, o usuário deve executar o arquivo app.py. Por meio da url "https://localhost:800/ping", a rota ping é acessada e retorna o json {"resposta": 'pong'} além de salvar as informações de horário, método e endereço da requirisição. Essas informações tambem ficam salvas quando a rota /echo é acessada por meio do metodo POST e retorna um jsonify({'dados': texto}). 

&emsp;A rota /dash apenas retorna o arquivo index.html para visualização dos logs inseridos por meio da rota /info. A rota /info pega um componente htmx do arquivo logs.html e retorna em uma tag <ul> no arquivo index.html todas as informações do "banco" a cada 3 segundos.

&emsp;Essa aplicação foi desenvolvida utilizando as seguintes ferramentas: JSON, Flask, HTML e HTMX. 
