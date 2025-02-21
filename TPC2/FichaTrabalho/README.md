# Queries em SPARQL

## Executando SPARQL no GraphDB via Docker

## 1.Executar o GraphDB via Docker

```

### **Rodar o contêiner**
```bash
docker run -d -p 7200:7200 -v graphdb_data:/opt/graphdb/home --name gdb (ID IMAGEM)```

- `-d` → Roda em segundo plano.
- `--name graphdb` → Nome do contêiner.
- `-p 7200:7200` → Mapeia a porta 7200 do contêiner para o host.

Como já tinha o docker a correr bastou fazer docker restart gdb

---

## 2. Aceder a Interface Web

Após iniciar o GraphDB, acedemos à interface web para gerenciar repositórios e dados:

- **URL**: [http://localhost:7200](http://localhost:7200)

---

## 3. Criar um Repositório no GraphDB

1. Vamos a **"Setup" > "Repositories"**.
2. Clicamos em **"Create new repository"**.

---

## 4. Carregar um Arquivo RDF (TTL, OWL, N3, etc.)

1. **"Import" > "Server files"** ou **"Upload RDF files"**.
2. Escolhemos um arquivo RDF (neste caso Histria_de_Portucal.rdf).
3. Fazemos o upload.

---

## 5. Executar Consultas SPARQL

1. **"Explore" > "SPARQL"**.
2. Escrevemos a query que queremos consultar
```

3. Clicamos em **"Run Query"** para vermos os resultados.


# ficha.md


Este documento contém um conjunto de consultas SPARQL aplicadas a uma ontologia de história, focada principalmente em reis, presidentes e partidos políticos. As consultas visam extrair diversas informações, como classes definidas, propriedades, número de indivíduos e relações entre diferentes entidades históricas.
