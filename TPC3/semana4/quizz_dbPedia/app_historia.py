# Um jogo sobre a história de Portugal
# 2025-02-24 jcr
#
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_cors import CORS
import random
import requests

app = Flask(__name__)
app.secret_key = 'História de Portugal'
CORS(app)

# Retrieve info from GraphDB
def query_graphdb(endpoint_url, sparql_query):
    headers = {
        'Accept': 'application/json', 
    }
    response = requests.get(endpoint_url, params={'query': sparql_query}, headers=headers)
    if response.status_code == 200:
        return response.json() 
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

endpoint = "http://localhost:7200/repositories/HistoriaPT"
sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT distinct ?n ?o ?c
    WHERE {
        ?s a :Rei.
    	?s :nome ?n .
    	?s :nascimento ?o.
    	?s :cognomes ?c .
}
"""

sparql_query_presidentes = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
select distinct ?s ?n ?d ?p (count (?m) as ?contamandatos)  where {
    ?s a :Presidente .
    ?s :nome ?n.
    ?s :nascimento ?d.
    ?s :mandato ?m. 
    ?s :partido/:nome ?p
} 
group by ?s ?n ?d ?p
order by desc(?contamandatos)
"""

sparql_query_conquistas = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
select distinct ?s ?n ?d ?r where {
    ?s a :Conquista .
    ?s :nome ?n.
    ?s :data ?d.
    ?s :temReinado/:temMonarca/:nome ?r
    
}
"""

result = query_graphdb(endpoint, sparql_query)
infoReis = []
for r in result['results']['bindings']:
    t = {
            'nome': r['n']['value'].split('#')[-1], 
            'dataNasc': r['o']['value'].split('#')[-1],
            'cognomes': r['c']['value'].split('#')[-1]
    }
    infoReis.append(t)

presidents =  query_graphdb(endpoint, sparql_query_presidentes)
infoPresidentes = []
infoPartidos = []
for r in presidents['results']['bindings']:
    p = {
            'nome': r['n']['value'].split('#')[-1], 
            'mandatos': r['contamandatos']['value'].split('#')[-1],
            'partido' : r['p']['value'].split('#')[-1]
    }
    infoPresidentes.append(p)
    infoPartidos.append(p['partido'])  

conquistas =  query_graphdb(endpoint, sparql_query_conquistas)
infoConquistas = []
for r in conquistas['results']['bindings']:
    c = {
            'nome': r['n']['value'].split('#')[-1], 
            'dataConq': r['d']['value'].split('#')[-1],
            'rei':  r['r']['value'].split('#')[-1]
    }
    infoConquistas.append(c)



@app.route('/')
def home():
    session['score'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET'])
def generate_question():
            reis = random.choices(infoReis, k=4)
            presidentes = random.choices(infoPresidentes, k=4)
            conquistas = random.choices(infoConquistas, k=4)

            reiSel = reis[random.randrange(0,4)]
            presidenteSel = presidentes[random.randrange(0,4)]
            conquistaSel = conquistas[random.randrange(0,4)]

            question1 = {
                "question": f"Quando nasceu o rei {reiSel['nome']}?",
                "options": [reis[0]['dataNasc'], reis[1]['dataNasc'], reis[2]['dataNasc'], reis[3]['dataNasc']],
                "answer": reiSel['dataNasc']
            }

            question2 = {
                "question": f"Que rei era conhecido pelo cognome {reiSel['cognomes'].split(',')[-1]}?",
                "options": [reis[0]['nome'], reis[1]['nome'], reis[2]['nome'], reis[3]['nome']],
                "answer": reiSel['nome']

            }

            question3 = {
                "question": f"António Óscar de Fragoso Carmona foi Presidente da República por 4 mandatos, sendo o Presidente da República com mais mandatos. ",
                "options": ["Verdadeiro", "Falso"],
                "answer": "Verdadeiro"

            }

            mandatoNum = random.choice([p['mandatos'] for p in presidentes])

            question4 = {
                "question": f" {presidenteSel['nome']} foi Presidente da República por {mandatoNum} mandato(s) ",
                "options": ["Verdadeiro", "Falso"],
                "answer": "Verdadeiro" if presidenteSel['mandatos'] == mandatoNum else "Falso"

            }

            conqData = random.choice([c['dataConq'] for c in conquistas])
            conqRei = random.choice([c['rei'] for c in conquistas])


            question5 = {
                "question": f" O feito histórico conhecido por {conquistaSel['nome']} aconteceu no ano de {conqData}, no reinado de {conqRei}",
                "options": ["Verdadeiro", "Falso"],
                "answer": "Verdadeiro" if (conquistaSel['dataConq'] == conqData and conquistaSel['rei'] == conqRei) else "Falso"

            }
            print(infoPartidos)
            infoPartidos.remove(presidenteSel['partido'])
            set_partidos = set(infoPartidos)
            partidos = random.sample(list(set_partidos), k=3)
            partidos.append(presidenteSel['partido'])


            question6 = {
                "question": f"A que partido pertenceu o presidente {presidenteSel['nome']} ?",
                "options": partidos,
                "answer": presidenteSel['partido']
            }

            selected_question = random.choice([question1, question2, question3, question4, question5, question6])
            return render_template('quiz.html', question=selected_question)

@app.route('/quiz_matching', methods=['GET'])
def generate_matching(): 
        reis = random.choices(infoReis, k=4)
        matching_pairs = {f'{reis[i]['nome']}': reis[i]['cognomes'].split(',')[0] for i in range(len(reis))}
        print(matching_pairs)
        reis = list(matching_pairs.keys())
        print(reis)
        answer_options = list(matching_pairs.values())
        random.shuffle(answer_options)

        question = {
        "question": f"Associe corretamente cada rei ao seu cognome. ",
        "question_corresp": reis,
        "options": answer_options,  
        "answer": list(matching_pairs.values())
    }
        
        return render_template('quiz_matching.html', question=question)

@app.route('/quiz', methods=['POST'])
def quiz():
    user_answer = request.form.get('answer')
    print(user_answer)
    answer_correct = request.form.get('answerCorrect')
    correct = answer_correct == user_answer
    session['score'] = session.get('score', 0) + (1 if correct else 0)
    return render_template('result.html', correct=correct, correct_answer=answer_correct, score=session['score'])

@app.route('/quiz_matching', methods=['POST'])
def quiz_matching():
    user_answers = {key: request.form.get(key) for key in request.form if key != "question"}  
    correct_answers = session.get('answerCorrect', {})  
    
    correct_count = sum(1 for key in correct_answers if correct_answers[key] == user_answers.get(key))
    total = len(correct_answers)

    session['score'] = session.get('score', 0) + correct_count  

    return render_template('result.html', correct_count=correct_count, total=total, 
                           correct_answer=correct_answers, score=session['score'])

@app.route('/score')
def score():
    return render_template('score.html', score=session.get('score', 0))

if __name__ == '__main__':
    app.run(debug=True)
