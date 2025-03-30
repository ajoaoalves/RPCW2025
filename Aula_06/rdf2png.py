import requests

# Caminho do ficheiro de ontologia Turtle (.ttl)
ttl_file_path = "corridas.ttl"  # Substituir pelo nome correto do ficheiro

# URL do serviço RDF Grapher
rdf_grapher_url = "https://www.ldf.fi/service/rdf-grapher"

# Ler o ficheiro Turtle
with open(ttl_file_path, "rb") as ttl_file:
    ttl_data = ttl_file.read()

# Definir os parâmetros esperados pelo serviço
files = {
    "rdf": ("ontology.ttl", ttl_data, "text/turtle"),  # Ontologia RDF
}
data = {
    "from": "ttl",  # Formato da ontologia enviada
    "to": "png"        # Formato desejado (imagem PNG)
}
headers = {
    "Accept": "image/png",  # Pedir especificamente PNG
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Enviar a ontologia ao serviço
response = requests.post(rdf_grapher_url, files=files, data=data, headers=headers)

# Verificar se a resposta é uma imagem PNG
if response.status_code == 200 and "image/png" in response.headers.get("Content-Type", ""):
    with open("output.png", "wb") as image_file:
        image_file.write(response.content)
    print("Imagem gerada com sucesso! Guardada como 'output.png'.")
else:
    print(f"Erro ao gerar imagem. Código HTTP: {response.status_code}")
    print("Resposta do servidor:")
    print(response.text[:500])  # Mostrar apenas os primeiros 500 caracteres para análise
