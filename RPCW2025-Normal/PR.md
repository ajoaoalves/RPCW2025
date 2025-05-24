Numa fase inicial procedi à realização do documento em ttl que é uma ontologia OWL escrita em Turtle (.ttl), usada para descrever conceitos e relações num domínio de conhecimento, provavelmente relacionado à educação, história ou filosofia. Eis o que contém:

Prefixos e Metadados
Define prefixos comuns (rdf, owl, xsd, etc.) e o URI base da ontologia.

# Propriedades de Objeto (Object Properties)

:aprende — liga um Aprendiz a uma Disciplina.
:ensina — liga um Mestre a uma Disciplina.
:estáRelacionadoCom — relaciona dois Conceitos.
:explica — liga uma Obra a um Conceito.
:foiEscritoPor — liga uma Obra a um Mestre.
:pertenceA — liga uma Disciplina a um TipoDeConhecimento.
:surgeEm — liga um Conceito a um PeríodoHistorico.
:temAplicaçãoEm — liga um Conceito a uma Aplicação.
:éEstudadoEm — liga um Conceito a uma Disciplina.

# Propriedades de Dados (Data Properties)

:nome — nome de várias entidades (Aplicação, Aprendiz, Autor, Conceito, Disciplina, Mestre, TipoDeConhecimento).
:periodo — período de um PeríodoHistorico.
:titulo — título de uma Obra.

# Classes

Define as seguintes classes:

:Aplicação
:Aprendiz
:Autor
:Conceito
:Disciplina
:Mestre
:Obra
:PeríodoHistorico
:TipoDeConhecimento

# Povoa 

Resumo do que faz o ficheiro povoa.py
O ficheiro povoa.py é um script Python que:

Lê vários ficheiros JSON com dados de aprendizes, mestres, disciplinas, obras e conceitos.
Usa a função clean_id para garantir que os identificadores são válidos para Turtle/Protégé.
Gera triplas Turtle para cada entidade e relação, de acordo com a ontologia definida.
Junta estas instâncias ao ficheiro base da ontologia (sapientia_base.ttl) e guarda tudo em sapientia_ind.ttl.
Ou seja, o script povoa automaticamente a ontologia com instâncias concretas a partir dos dados JSON, ficando pronta para ser consultada com SPARQL.


## Função clean_id

Garante que todos os identificadores usados nas URIs (nomes de pessoas, disciplinas, etc.) só têm letras, números e underscores, tornando-os válidos para Turtle/Protégé.

## Função Povoa

Lê os dados dos ficheiros JSON (mestres.json, conceitos.json, disciplinas.json, obras.json, pg57505.json).
Para cada tipo de entidade (Aprendiz, Mestre, Conceito, Disciplina, Obra), gera triplas Turtle com as propriedades e relações corretas, de acordo com a ontologia.
Por exemplo, para cada aprendiz, cria uma instância com nome, idade e as disciplinas que aprende.
Para cada mestre, cria uma instância com nome, período histórico e disciplinas que ensina.
Faz o mesmo para conceitos, disciplinas e obras, incluindo as relações entre eles.
Função save_to_ttl_with_base
Junta o conteúdo gerado (ttl_data) ao ficheiro base da ontologia (sapientia_base.ttl) e guarda tudo num novo ficheiro (sapientia_ind.ttl).

## Execução

No final do ficheiro, lê todos os ficheiros JSON, chama a função Povoa e guarda o resultado.

Como correr o povoa.py
Coloque todos os ficheiros JSON e o sapientia_base.ttl na mesma pasta do script.
No terminal, navege até à pasta do projeto.

Executa: python3 povoa.py


# Queries 

O ficheiro sparql.txt contém várias queries SPARQL para consultar a ontologia gerada. Estas queries permitem:

Procurar conceitos ensinados por um mestre específico.
Listar obras que explicam um conceito.
Ver disciplinas de um tipo de conhecimento.
Consultar aplicações práticas de conceitos.
Ver mestres de um certo período histórico.
Listar aprendizes por disciplina, por escalão etário, etc.
Criar relações novas como :estudaCom (aluno-mestre) e :daBasesPara (disciplina-aplicação) usando queries CONSTRUCT e INSERT.
Ou seja, o ficheiro serve para explorar e enriquecer a ontologia com perguntas e inferências automáticas.

