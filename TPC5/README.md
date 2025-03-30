
# Descrição do Código para Geração de Arquivo TTL a partir de Dados JSON

Este código Python tem como objetivo gerar um arquivo TTL (Turtle), a partir de um arquivo JSON contendo informações sobre filmes, gêneros, idiomas, países e pessoas. O arquivo TTL gerado é utilizado para representar uma ontologia (modelo de conhecimento) sobre filmes no formato RDF.

## Funções do Código

### 1. Função `Object_Prop()`
Esta função cria as propriedades de objetos na ontologia, que são usadas para relacionar diferentes recursos em RDF.

- **Propriedades de objetos** definidas:
  - `temGénero`: Relaciona um filme a um ou mais gêneros.
  - `temLingua`: Relaciona um filme a uma língua.
  - `temPaisOrigem`: Relaciona um filme a um país de origem.

### 2. Função `Class()`
A função cria as classes da ontologia, que representam categorias ou tipos de recursos.

- **Classes definidas**:
  - `Filme`: Representa filmes na ontologia.
  - `País`: Representa países de origem.
  - `Género`: Representa gêneros de filmes.
  - `Lingua`: Representa idiomas de filmes.
  - `Pessoa`: Representa pessoas (como atores, diretores, etc.).

### 3. Função `Data_Properties()`
Esta função cria as propriedades de dados, que associam valores literais (como strings, inteiros) aos recursos.

- **Propriedades de dados definidas**:
  - `Data`: Representa a data de lançamento de um filme.
  - `Duracao`: Representa a duração de um filme em minutos.
  - `titulo`: Representa o título do filme.

### 4. Função `Individuals(data)`
A função cria os indivíduos na ontologia. Indivíduos são instâncias específicas das classes definidas anteriormente (por exemplo, filmes, gêneros, pessoas).

- **Processo**:
  - Para cada filme, é gerado um indivíduo com suas propriedades (título, data de lançamento, duração, etc.).
  - Também são criados indivíduos para gêneros, línguas, países e pessoas.
  - Caracteres especiais no título, gênero, língua e nome das pessoas são substituídos por underscores (`_`) usando expressões regulares.

### 5. Função `json_to_ttl(json_file, ttl_file)`
Esta função lê o arquivo JSON contendo os dados, gera o conteúdo do arquivo TTL e escreve o conteúdo gerado em um arquivo `.ttl`.

- O arquivo gerado começa com a definição de prefixos RDF, que são usados para referenciar classes e propriedades de forma compacta.
- A função chama as funções `Object_Prop()`, `Class()`, `Data_Properties()` e `Individuals()` para gerar as seções do arquivo TTL.

## Fluxo do Código

1. O arquivo JSON é lido e o seu conteúdo é carregado.
2. Para cada filme, as propriedades são extraídas, e os indivíduos (instâncias) são gerados com as respectivas propriedades.
3. O código também cria indivíduos para gêneros, línguas, países e pessoas mencionados no arquivo JSON.
4. O arquivo TTL gerado segue o padrão de representação de ontologias no RDF, usando as classes, propriedades de objetos e de dados definidas.

## Objetivo do Arquivo TTL Gerado

O arquivo TTL gerado pode ser carregado em ferramentas de processamento RDF, como Protégé, para trabalhar com a ontologia dos filmes de forma estruturada. Ele também pode ser utilizado para consultas SPARQL e inferência semântica.


