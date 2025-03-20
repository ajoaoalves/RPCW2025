# Explicação do Código Python para Extração de Dados de Filmes da DBpedia

## Introdução
Este programa em **Python** recolhe informação sobre filmes a partir da **DBpedia**, uma base de conhecimento extraída da Wikipedia. O código consulta a DBpedia usando a linguagem **SPARQL**, recolhe dados sobre filmes e guarda-os num ficheiro `dataset.json`.

---

## Bibliotecas Utilizadas
- `json`: Para ler e escrever ficheiros JSON.
- `requests`: Para fazer pedidos HTTP.
- `query_graphdb`: Função personalizada que executa consultas SPARQL na DBpedia.

---

###  **Carregamento da Lista de Filmes**
```python
with open("filmes.json") as f:
    filmes = json.load(f)
```
Lê o ficheiro `filmes.json`, que contém uma lista de URIs (endereços) de filmes na DBpedia.

###  **Definição do Endpoint da DBpedia**
```python
endpoint = "https://dbpedia.org/sparql"
```
Define o URL do endpoint **SPARQL** da DBpedia, onde serão feitas as consultas.

### **Inicialização da Lista de Dados**
```python
dataset = []
```
Cria uma lista vazia onde serão armazenados os dados dos filmes.

---

## **Execução das Consultas SPARQL**

O código percorre cada filme na lista e faz **duas consultas SPARQL**:
1. **Recolhe informação básica do filme**: Nome, sinopse, data de lançamento, país de origem e realizador.
2. **Recolhe os atores que participaram no filme.**

### **Consulta SPARQL para Informações do Filme**
```python
sparql_query = f"""
    SELECT DISTINCT ?nome ?abs ?dataLan ?pais ?realizador WHERE {{
    <{d}> dbo:abstract ?abs .
    <{d}> rdfs:label ?nome.
    <{d}> dbo:releaseDate ?dataLan.
    <{d}> dbp:country ?pais .
    <{d}> dbp:director ?realizador .
    FILTER (LANG(?abs) = "en").
    FILTER (LANG(?nome) = "en").
    }}
"""
result = query_graphdb(endpoint, sparql_query)
```
- Usa a URI do filme (`<{d}>`) para obter:
  - `?nome` → Nome do filme
  - `?abs` → Sinopse
  - `?dataLan` → Data de lançamento
  - `?pais` → País de origem
  - `?realizador` → Diretor
- Os filtros `LANG(?abs) = "en"` e `LANG(?nome) = "en"` garantem que os textos estejam em inglês.

### 5️ **Consulta SPARQL para Obter os Atores**
```python
sparql_query2 = f"""
    SELECT DISTINCT ?ator ?nome WHERE {{
        <{d}> dbo:starring ?ator .
        ?ator a dbo:Person .       
        ?ator foaf:name ?nome .    
    }}
"""
result2 = query_graphdb(endpoint, sparql_query2)
```
- Obtém a lista de atores (`?ator`) e os seus nomes (`?nome`).

###  **Armazenamento dos Atores**
```python
atores = []
for a in result2['results']['bindings']:
    atores.append({
        "id": a['ator']['value'],
        "nome": a['nome']['value']
    })
```
Percorre os resultados da consulta e guarda os atores numa lista.

---

## **Tratamento dos Dados e Construção do Dataset**

### **Criação do Dicionário de Cada Filme**
```python
dataset.append(
    {
        "id": d,
        "titulo": result['results']['bindings'][0]['nome']['value'],
        "sinopese": result['results']['bindings'][0]['abs']['value'],
        "dataLançamento": result['results']['bindings'][0]['dataLan']['value'],
        "pais_origem": result['results']['bindings'][0]['pais']['value'],
        "realizador": result['results']['bindings'][0]['realizador']['value'],
        "atores": atores
    }
)
```
- Guarda as informações do filme num dicionário e adiciona ao `dataset`.


## **Escrita dos Dados no Ficheiro JSON**
```python
with open("dataset.json", "w") as fout:
    json.dump(dataset, fout)
```
- Guarda os dados extraídos no ficheiro `dataset.json`.

---

## **Conclusão**
Este script recolhe informações sobre filmes da DBpedia e grava-as num ficheiro JSON. As consultas SPARQL obtêm os dados e o programa garante que os resultados sejam processados corretamente antes de os armazenar.
