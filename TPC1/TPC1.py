import json

def ObjectProperties () :
    ttl_data = f"""
#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#Pratica
:Pratica rdf:type owl:ObjectProperty ;
     rdfs:domain :Pessoa .


###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#Realiza
:Realiza rdf:type owl:ObjectProperty ;
     rdfs:domain :Pessoa .

"""
    return ttl_data
        
def Dataproperties():

    ttl_data = f"""
#################################################################
#    Data properties
#################################################################

###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#temNome 
:temNome rdf:type owl:DatatypeProperty ;
    rdfs:domain [ rdf:type owl:Class ;
                  owl:unionOf ( :Modalidade
                                :Pessoa
                              )
                ] ;
    rdfs:range xsd:string .

    
###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#temResultado 
:temResultado rdf:type owl:DatatypeProperty ;
    rdfs:domain [ rdf:type owl:Class ;
                  owl:unionOf ( :Exame
                                :Pessoa
                              )
                ] ;
    rdfs:range xsd:string .

"""
    return ttl_data

        
def Classes() : 
    ttl_data = f"""
#################################################################
#    Classes
#################################################################

###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#Pessoa
:Pessoa rdf:type owl:Class .


###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#Modalidade
:Modalidade rdf:type owl:Class .


###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#Exame
:Exame rdf:type owl:Class .

"""
    return ttl_data

def Individuals():
    ttl_data = f"""
#################################################################
#    Individuals
#################################################################

"""
    return ttl_data

def Individuals_pessoas(entry) : 

    nome_completo = f"{entry['nome']['primeiro'].replace(' ', '')}{entry['nome']['último'].replace(' ', '')}"
    modalidade = entry['modalidade'].replace(" ", "_")
    resultado = "Saudavel" if entry['resultado'] else "NaoSaudavel"

    ttl_data = f"""
###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#{nome_completo}
:{nome_completo} rdf:type owl:NamedIndividual ,
               :Pessoa ;
      :Pratica :{modalidade} ;
      :temNome "{nome_completo}" ;
      :temResultado "{resultado}".

"""
    
    return ttl_data

def Individuals_modalidade(modalidades_set):
    ttl_data = ""
    for e in modalidades_set:
        ttl_data += f"""
###  http://www.semanticweb.org/ajr/ontologies/2025/desporto#{e}
:{e} rdf:type owl:NamedIndividual ,
                 :Modalidade ;
        :temNome "{e}" .
"""
    return ttl_data
    

def json_to_ttl(json_file, ttl_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    with open(ttl_file, 'w', encoding='utf-8') as f:
        f.write("@prefix : <http://www.semanticweb.org/ajr/ontologies/2025/desporto/> .\n")
        f.write("@prefix owl: <http://www.w3.org/2002/07/owl#> .\n")
        f.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
        f.write("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n")
        f.write("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n")
        f.write("@base <http://www.semanticweb.org/ajr/ontologies/2025/desporto/> .\n")
        f.write("<http://www.semanticweb.org/ajr/ontologies/2025/desporto> rdf:type owl:Ontology .\n")

        modalidades_set = set()
        

        f.write(ObjectProperties())
        f.write(Dataproperties())
        f.write(Classes())
        f.write(Individuals())

        for entry in data:
            modalidades_set.add(entry.get("modalidade"))
            f.write(Individuals_pessoas(entry))
        
        f.write(Individuals_modalidade(modalidades_set))
    print(f"Arquivo TTL '{ttl_file}' gerado com sucesso!")

# Exemplo de uso da função
json_to_ttl('emd.json', 'ontologia.ttl')