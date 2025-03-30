import json
import re

def Object_Prop():
    ttl_data = f"""
###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#temGénero
:temGénero rdf:type owl:ObjectProperty ;
           rdfs:domain :Filme ;
           rdfs:range :Género .


###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#temLingua
:temLingua rdf:type owl:ObjectProperty ;
           rdfs:domain :Filme ;
           rdfs:range :Lingua .


###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#temPaisOrigem
:temPaisOrigem rdf:type owl:ObjectProperty ;
               rdfs:domain :Filme ;
               rdfs:range :País .
    """
    return ttl_data

def Class():
    ttl_data = f"""
###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#País
:País rdf:type owl:Class .

###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#Filme
:Filme rdf:type owl:Class .

###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#Género
:Género rdf:type owl:Class .

###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#Lingua
:Lingua rdf:type owl:Class .

###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#Pessoa
:Pessoa rdf:type owl:Class .
    """
    return ttl_data

def Data_Properties():
    ttl_data = f"""
#################################################################
#    Data properties
#################################################################

###  http://www.semanticweb.org/ajr/ontologies/2025/untitled-ontology-9#Data
:Data rdf:type owl:DatatypeProperty ;
      rdfs:domain :Filme ;
      rdfs:range xsd:string .


###  http://www.semanticweb.org/ajr/ontologies/2025/untitled-ontology-9#Duracao
:Duracao rdf:type owl:DatatypeProperty ;
         rdfs:domain :Filme ;
         rdfs:range xsd:int .

###  http://www.semanticweb.org/ajr/ontologies/2025/untitled-ontology-9#titulo
:titulo rdf:type owl:DatatypeProperty ;
        rdfs:domain :Filme ;
        rdfs:range xsd:string .
    
"""
    return ttl_data

def Individuals(data):
    ttl_data = f"""
#################################################################
#    Individuals
#################################################################

"""
    for filme in data["movies"]:
        titulo = filme['tituloOriginal']
        titulo = re.sub(r'[^a-zA-Z0-9]', '_', titulo)
        dataLanc = filme['ano']
        duracao = filme['duração']
        generos = filme['género'] 
        pais = filme['PaisOrigem'] 
        lingua = filme['linguaOriginal']
        generos_com_prefixo = [":" + genero for genero in generos] 
        generos_formatados = ", ".join(generos_com_prefixo)

        ttl_data += f"""
    ###  <http://www.semanticweb.org/ajr/ontologies/2025/cinema#{titulo}>
    :{titulo} rdf:type owl:NamedIndividual ,
                       :Filme ;
                 :temGénero {generos_formatados} ;
                 :temPaisOrigem :{pais} ;
                 :Data "{dataLanc}" ;"""
        if lingua is not None:
            ttl_data += f"""
                 :temLingua :{lingua} ;"""

        ttl_data += f"""
                 :Duracao {duracao} ;
                 :titulo "{titulo}" ."""

        
    ttl_data = ttl_data.strip().rstrip(";") + " .\n"

    for genero in data["allgénero"]:
        
        ttl_data += f"""
###  <http://www.semanticweb.org/ajr/ontologies/2025/cinema#{genero}>
:{genero} rdf:type owl:NamedIndividual ,
               :Género .
        """
        
    for lingua in data["allLanguages"]:
        
        ttl_data += f"""
###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#{lingua}
:{lingua} rdf:type owl:NamedIndividual ,
               :Lingua .
        """
    
    for pais in data["allCountries"]:
        
        ttl_data += f"""
###  http://www.semanticweb.org/ajr/ontologies/2025/cinema#{pais}
:{pais} rdf:type owl:NamedIndividual ,
               :País . 
        """
    for pessoa in data["allPeople"].values():
        pessoa = pessoa.replace(" ", "_")
        pessoa = re.sub(r'[^a-zA-Z0-9]', '_', titulo)
        
        ttl_data += f"""
###  <http://www.semanticweb.org/ajr/ontologies/2025/cinema#{pessoa}>
:{pessoa} rdf:type owl:NamedIndividual ,
               :Pessoa .
        """
        
    return ttl_data

def json_to_ttl(json_file, ttl_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    with open(ttl_file, 'w', encoding='utf-8') as f:
        f.write("@prefix : <http://www.semanticweb.org/ajr/ontologies/2025/cinema/> .\n")
        f.write("@prefix owl: <http://www.w3.org/2002/07/owl#> .\n")
        f.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
        f.write("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n")
        f.write("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n")
        f.write("@base <http://www.semanticweb.org/ajr/ontologies/2025/cinema/> .\n")
        f.write("<http://www.semanticweb.org/ajr/ontologies/2025/cinema> rdf:type owl:Ontology .\n")
        

        f.write(Individuals(data))


        
    print(f"Arquivo TTL '{ttl_file}' gerado com sucesso!")

json_to_ttl('movies.json', 'cinema.ttl')