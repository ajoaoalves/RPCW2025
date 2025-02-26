Arquitetura REST

GET - retrieve
POST - Inserir/Enviar
PUT - Alterar
DELETE - Apagar

sempre que há um pedido há um codigo:
200 é um codigo de sucesso a um get

Comandos para executar o graphdb/demo.py:
pip3 install requests

Se eu quiser ir buscar os triplos de um fucheiro json que resulta desta query

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

SELECT ?s ?p ?o
    WHERE {
        ?s ?p ?o
    }
LIMIT 100

for r in result['results']['bindings']
    t = (r['s']['value'],r['p']['value'])

para o import do tabulate no demo.py: pip3 install tabulate

no quizz_dbPedia
(isto para usarmos json: app_api.py)
pip3 install flask
pip3 install flask_cors
python3 app_api.py
no browser: http://localhost:5000/api/quiz

(para usarmos paginas web: app_jinja.py)

python3 app_jinja.py
no browser: http://localhost:5000/quiz