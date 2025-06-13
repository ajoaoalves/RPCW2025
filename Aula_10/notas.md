


PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/genoa/>
insert {
	?s :temAvoF ?a .
    
}
where {
	?s :temProgenitor/:temPai ?a .
}

PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/genoa/>
insert {
	?s :temAvoM ?a .
    
}
where {
	?s :temProgenitor/:temPai ?a .
}

## Vamos criar o :temIrmao
PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/genoa/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>


construct { 
    ?s :temIrmao ?i .
    :temIrmao rdf:type owl:ObjectProperty .
}
where {
    ?s :temProgenitor/:eProgenitorDe ?i .
    filter (?s != ?i)   ## irreflexibilidade 
}

depois de um construct temos de fazer insert 

insert { 
    ?s :temIrmao ?i .
    :temIrmao rdf:type owl:ObjectProperty .
}
where {
    ?s :temProgenitor/:eProgenitorDe ?i .
    filter (?s != ?i)   ## irreflexibilidade 
}


o construct ve as ligações possiveis, o insert insere na ontologia
##tem primo

PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/genoa/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

construct { 
    ?s :temPrimo ?i .
    :temPrimo rdf:type owl:ObjectProperty .
}
where {
    ?s :temTio/:eProgenitorDe ?i .
}