$ docker images   -> Exibe uma lista das imagens Docker armazenadas localmente no seu sistema.

$ docker run -d -p 7200:7200 --name graphdb <id imagem>   executar o container 

$ docker stop graphdb ---> para o container
$ docker rm graphdb ---> apago o container

$ docker stop graphdb ---> parar o container
$ docker restart graphdb  -> reiniciar o container


docker volume create graphdb_data

docker images

docker run -d -p 7200:7200 -v graphdb_data:/opt/graphdb/home --name gdb 1919d5a74509

docker ps

se for ao localhost:7200 na web tenho la informação

set->repositorios->create->graphdb repository


# QUERIES EM SPARQL

PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/banco/>
select ?s ?n ?a where {
    ?s :Nome ?n.
    ?s :Animal ?a.
} 



PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/banco/>
select ?s ?n ?a ?c ?p where {
    ?s :Nome "Alfredo".
    ?s :Animal ?a.
    ?s :Cor ?c.
    ?s :Profissão ?p.
} 


PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/banco/>
select ?s ?n ?a ?c ?p where {
    ?s :Nome ?n.
    ?s :Animal ?a.
    ?s :Cor ?c.
    ?s :Profissão ?p.
} 
order by ?n




PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/banco/>
select ?s ?n ?a ?c ?p where {
    ?s :Nome ?n.
    ?s :Animal ?a.
    ?s :Cor ?c.
    ?s :Profissão ?p.
} 
order by desc(?n)


PREFIX : <http://www.semanticweb.org/ajr/ontologies/2025/banco/>
select ?s ?n ?a ?c ?p where {
    ?s :Nome ?n.
    ?s :Animal ?a.
    ?s :Cor ?c.
    ?s :Profissão ?p.
} 
order by ?n
limit 3


site para saber prefixo: https://prefix.cc/