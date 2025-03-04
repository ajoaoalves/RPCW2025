# Jogo sobre a História de Portugal

## Descrição
Este projeto consiste num jogo interativo sobre a História de Portugal, implementado em Python utilizando o framework Flask. O jogo apresenta perguntas sobre reis, presidentes e conquistas históricas, obtendo informações a partir de uma base de dados semântica (GraphDB).

## Tecnologias Utilizadas
- **Flask**: Framework web para Python
- **Flask-CORS**: Para permitir requisições de diferentes origens
- **GraphDB**: Base de dados para armazenar informações históricas em RDF
- **SPARQL**: Linguagem de consulta para obter informações da GraphDB

## Estrutura do Código

### Importação de Bibliotecas
O código importa bibliotecas necessárias para a aplicação web, manipulação de requisições e sessões:
```python
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_cors import CORS
import random
import requests
```

### Configuração da Aplicação Flask
A aplicação Flask é inicializada com uma chave secreta para a gestão de sessões e suporte a CORS:
```python
app = Flask(__name__)
app.secret_key = 'História de Portugal'
CORS(app)
```

### Função para Consulta à GraphDB
A função `query_graphdb()` faz requisições a um endpoint SPARQL da GraphDB para obter informações históricas:
```python
def query_graphdb(endpoint_url, sparql_query):
    headers = {'Accept': 'application/json'}
    response = requests.get(endpoint_url, params={'query': sparql_query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro {response.status_code}: {response.text}")
```

### Consultas SPARQL
O código contém três consultas principais:
1. **Reis de Portugal**: Obtém o nome, data de nascimento e cognomes dos reis.
2. **Presidentes da República**: Obtém o nome, data de nascimento, partido político e número de mandatos.
3. **Conquistas históricas**: Obtém o nome da conquista, data e monarca associado.

Exemplo de consulta SPARQL para reis:
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT distinct ?n ?o ?c
    WHERE {
        ?s a :Rei.
        ?s :nome ?n .
        ?s :nascimento ?o.
        ?s :cognomes ?c .
}
```

### Rotas da Aplicação

#### **Página Inicial**
Redireciona o utilizador para o quiz:
```python
@app.route('/')
def home():
    session['score'] = 0
    return redirect(url_for('quiz'))
```

#### **Geração de Perguntas**
A rota `/quiz` gera uma pergunta aleatória sobre reis, presidentes ou conquistas:
```python
@app.route('/quiz', methods=['GET'])
def generate_question():
    reis = random.choices(infoReis, k=4)
    presidenteSel = random.choice(infoPresidentes)
    conquistaSel = random.choice(infoConquistas)

    question1 = {
        "question": f"Quando nasceu o rei {reis[0]['nome']}?",
        "options": [r['dataNasc'] for r in reis],
        "answer": reis[0]['dataNasc']
    }

    selected_question = random.choice([question1])
    return render_template('quiz.html', question=selected_question)
```

#### **Envio de Respostas**
As respostas dos utilizadores são processadas e o sistema verifica se estão corretas:
```python
@app.route('/quiz', methods=['POST'])
def quiz():
    user_answer = request.form.get('answer')
    answer_correct = request.form.get('answerCorrect')
    correct = answer_correct == user_answer
    session['score'] = session.get('score', 0) + (1 if correct else 0)
    return render_template('result.html', correct=correct, correct_answer=answer_correct, score=session['score'])
```

#### **Modo Matching**
Os utilizadores podem associar corretamente reis e cognomes:
```python
@app.route('/quiz_matching', methods=['GET'])
def generate_matching():
    reis = random.choices(infoReis, k=4)
    matching_pairs = {r['nome']: r['cognomes'].split(',')[0] for r in reis}
    answer_options = list(matching_pairs.values())
    random.shuffle(answer_options)

    question = {
        "question": "Associe corretamente cada rei ao seu cognome.",
        "question_corresp": list(matching_pairs.keys()),
        "options": answer_options,
        "answer": list(matching_pairs.values())
    }
    
    return render_template('quiz_matching.html', question=question)
```

#### **Pontuação**
O utilizador pode verificar a sua pontuação atual:
```python
@app.route('/score')
def score():
    return render_template('score.html', score=session.get('score', 0))
```

## Para compilar
Ter a base de dados up com "docker restart gdb" e acedendo ao localhost pela porta 7200. Para compilar o programa "python3 app_historia.py" e acedendo ao localhost pela porta 5000.
