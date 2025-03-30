
https://www.iro.umontreal.ca/~lapalme/ift6281/sparql-1_1-cheat-sheet.pdf

rdf: http://xmlns.com/foaf/0.1/
    conceito de dominio
    conceito de range
    condeito de subclasse
rdfs: http://www.w3.org/2000/01/rdf-schema#
owl: http://www.w3.org/2002/07/owl#
    conceito de dominio
    conceito de range
    conceito de subclasse
    conceito de logica
        primiera ordem
        segunda ordem
xsd: http://www.w3.org/2001/XMLSchema#

dc: http://purl.org/dc/elements/1.1/
    conjunto de metadados mais utilizado no digital, como bibliotecas
foaf: http://xmlns.com/foaf/0.1/ (friend of a friend)
    conceito de nome, etc e relações entre este


SELECT * WHERE {
    ?s a :Rei
    ?s :temFilho ?filho
    ?filho :temNome ?nome
}

Vai selecionar os filhos que têm nome de um rei. Se não tiver nome, nao obtemos esse triplo

OPTIONAL {
    ?filho :temNome ?nome
}

para incluir os que não tem nome

OPTIONAL {
    ?filho :temNome ?nome
    FILTER (lang(?nome) = "en")
}

Assim verifica os nomes apenas em ingles

# Exercicio 

## Lista os nomes dos desportos contemplados na DBpedia: lista a sua designação e a sua descrição em inglês;

```
select distinct ?nome ?abs where {
?desporto a dbo:Sport.
?desporto dbo:abstract ?abs .
filter (lang (?abs) = "en").
?desporto rdfs:label ?nome.
filter (lang (?nome) = "en").
} LIMIT 100
```

## Lista os nomes e respectiva informação (nome, data nascimento, local de nascimento) dos jogadores de Polo Aquático que estão classificados como "Person" na Ontologia "schema.org";

select distinct  ?atleta where {
?atleta a schema:Person .
?atleta dbp:sport <http://dbpedia.org/resource/Water_polo>.
} 


## Refina a query anterior para is buscar valores em lugar de IRIs: birthPlace...

select distinct  ?atleta ?desporto ?nome ?origem where {
?atleta a schema:Person .
?atleta dbp:sport ?desporto .
?atleta dbp:name ?nome.
?atleta dbp:nationality? ?origem.
} 
LIMIT 1000


## Da lista de desportos obtida, seleciona cerca de 50;

select distinct ?desporto where {
?desporto a dbo:Sport.
?desporto dbo:abstract ?abs .
filter (lang (?abs) = "en").
?desporto rdfs:label ?nome.
filter (lang (?nome) = "en").
} LIMIT 200


## Para os 50 desportos selecionados constrói um serviço em Python que vai buscar os atletas de cada um dos desportos e constrói um dataset em JSON com duas coleções: desportos e atletas.



TPC

fazer um haverster sobre o DBPedia sob o tema "cinema"

Filmes { id,
        titulo, 
        pais(pais de produçao)
        data(data de lançamento),
        realizador,
        elenco [ator],
        genero [genero],
        sinopese/abs
        }