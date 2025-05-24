import re
import json

def clean_id(s):
    # Permite letras (incluindo acentuadas), números e _
    return re.sub(r'[^\w]', '_', s, flags=re.UNICODE)

def Povoa(dic_jsonConceitos, dic_jsonDisciplinas, dic_jsonMestres, dic_jsonObras, dic_jsonAprendiz ):
    ttl_data = ""
    for aprendiz in dic_jsonAprendiz:
        nome = aprendiz['nome'].strip()
        nome_clean = clean_id(nome)
        idade = int(aprendiz['idade'])
        disciplinas = aprendiz['disciplinas']
        ttl_data += (
            f":{nome_clean} a :Aprendiz ;\n"
            f'    :nome "{nome}" ;\n'
            f'    :idade {idade} ;\n'
            f'    :aprende {", ".join(f":{clean_id(d)}" for d in disciplinas)} . \n\n'
        )

    for mestre in dic_jsonMestres["mestres"]:
        nome = mestre['nome'].strip()
        nome_clean = clean_id(nome)
        periodo = mestre['períodoHistórico'].replace(" ", "_")
        disciplinas = mestre['disciplinas']
        ttl_data += (
            f":{nome_clean} a :Mestre ;\n"
            f'    :nome "{nome}" ;\n'
            f'    :periodo "{periodo}" ;\n'
            f'    :ensina {", ".join(f":{clean_id(d)}" for d in disciplinas)} . \n\n'
        )

    for conceito in dic_jsonConceitos["conceitos"]:
        nome = conceito['nome'].strip()
        nome_clean = clean_id(nome)
        aplicacoes = conceito.get('aplicações', [])
        periodo = conceito.get('períodoHistórico', '').replace(" ", "_")
        conceitos_rel = conceito.get('conceitosRelacionados', [])
        ttl_data += (
            f":{nome_clean} a :Conceito ;\n"
            f'    :nome "{nome}" ;\n'
            f'    :periodo "{periodo}" ;\n'
            f'    :temAplicaçãoEm {", ".join(f":{clean_id(a)}" for a in aplicacoes)} ;\n'
            f'    :estáRelacionadoCom {", ".join(f":{clean_id(c)}" for c in conceitos_rel)} .\n\n'
        )

    for disciplina in dic_jsonDisciplinas["disciplinas"]:
        nome = disciplina['nome'].strip()
        nome_clean = clean_id(nome)
        tipos = disciplina['tiposDeConhecimento']
        ttl_data += (
            f":{nome_clean} a :Disciplina ;\n"
            f'    :nome "{nome}" ;\n'
            f'    :pertenceA {", ".join(f":{clean_id(d)}" for d in tipos)}  .\n\n'
        )

    for obra in dic_jsonObras["obras"]:
        titulo = obra['titulo'].strip()
        titulo_clean = clean_id(titulo)
        autor = clean_id(obra['autor'].strip())
        conceitos = obra.get('conceitos', [])
        ttl_data += (
            f":{titulo_clean} a :Obra ;\n"
            f'    :titulo "{titulo}" ;\n'
            f'    :foiEscritoPor :{autor} ;\n'
            f'    :explica {", ".join(f":{clean_id(c)}" for c in conceitos)} .\n\n'
        )

    return ttl_data

def read_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_to_ttl_with_base(base_file, ttl_data, output_file):
    with open(base_file, 'r', encoding='utf-8') as f:
        base_content = f.read()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(base_content)
        f.write('\n\n')
        f.write(ttl_data)

mestres = read_json("mestres.json")
conceitos_json = read_json("conceitos.json")
disciplinas = read_json("disciplinas.json")
obras = read_json("obras.json")
aprendizes = read_json("pg57505.json")

ttl_content = Povoa(conceitos_json, disciplinas, mestres, obras, aprendizes)
save_to_ttl_with_base("sapientia_base.ttl", ttl_content, "sapientia_ind.ttl")