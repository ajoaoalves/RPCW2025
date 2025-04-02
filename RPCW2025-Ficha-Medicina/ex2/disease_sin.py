import csv
import re
import json

def Individuals(datasets):
    id = 2
    dic_disease_info = {}  # Informações das doenças
    set_symptoms = set()   # Conjunto de sintomas
    set_treatments = set()  # Conjunto de tratamentos
    dic_doente = {}  # Informações dos pacientes
    ttl_data = ""
    max_patients = 100
    for data in datasets:  
        for row in data:
            # Processando a doença
            disease = row.get("Disease", "").strip()
            disease = re.sub(r"[()\"]", "", disease)
            disease = disease.replace(" ", "_").capitalize()

            if len(dic_doente) >= max_patients:
                print(f"Limite de {max_patients} pacientes alcançado. Não adicionando mais pacientes.")
                break  #

            # Verificando o nome do paciente
            doente = row.get("nome", None)
            if doente is None:
                continue 

            # Se a doença ainda não estiver no dicionário, adiciona
            if disease not in dic_disease_info:
                dic_disease_info[disease] = {
                    "Nome": disease,
                    "Sintomas": set(),
                    "Descrição": "",
                    "Tratamentos": set()
                }
            
            # Se o paciente ainda não estiver no dicionário de pacientes, adiciona
            if doente not in dic_doente:
                id += 1
                dic_doente[doente] = {
                    "Id": id,
                    "Nome": doente,
                    "Sintomas": row.get("sintomas", [])
                }

            # Adiciona a descrição da doença se existir
            if "Description" in row:
                description = row["Description"].strip()
                description = re.sub(r"[(\")]", "", description)   
                if description:
                    dic_disease_info[disease]["Descrição"] = description

            # Adicionando tratamentos
            for i in range(1, 5):  
                treatment_key = f"Precaution_{i}"
                if treatment_key in row:
                    treatment = row[treatment_key].strip()
                    if treatment:
                        treatment = re.sub(r"[()]", "", treatment)  
                        treatment = treatment.replace(" ", "_").capitalize()
                        dic_disease_info[disease]["Tratamentos"].add(treatment)
                        set_treatments.add(treatment)

            # Adicionando sintomas
            for i in range(1, 18):  
                symptom_key = f"Symptom_{i}"
                if symptom_key in row:
                    symptom = row[symptom_key].strip()
                    if symptom:
                        symptom = re.sub(r"[()]", "", symptom)  
                        symptom = symptom.replace(" ", "_").capitalize()
                        dic_disease_info[disease]["Sintomas"].add(symptom)
                        set_symptoms.add(symptom)

    for disease, data in dic_disease_info.items():
        symptoms = data["Sintomas"]
        description = data["Descrição"]
        treatments = data["Tratamentos"]
        ttl_data += f""":{disease} a :Disease . \n"""

        ttl_data += f""":{disease} a :Disease ;
             :hasSymptom {', '.join(f':{symptom}' for symptom in symptoms)} ;
             :hasDescription "{description}" ;
             :hasTreatment {', '.join(f':{treatment}' for treatment in treatments)} .\n"""
        
    for pessoa, data in dic_doente.items():
        idPessoa = data["Id"]
        nome = data["Nome"]
        sintomas = data["Sintomas"]

        ttl_data += f""":Patient{idPessoa} a :Patient ;
                  :name \"{nome}\" ; \n"""
        for i, sintoma in enumerate(sintomas):
            if i == len(sintomas) - 1: 
                ttl_data += f"""                  :exhibitsSymptom :{sintoma} . \n""" 
            else:
                ttl_data += f"""                  :exhibitsSymptom :{sintoma} ; \n""" 


        
    
    for symptom in set_symptoms:
        ttl_data += f":{symptom} a :Symptom .\n"
    
    for treatment in set_treatments:
        ttl_data += f":{treatment} a :Treatment .\n"
    

    return ttl_data  

def read_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)  
        return list(reader)

def read_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def csv_and_json_to_ttl(files, ttl_file):
    datasets = []
    
    for file in files:
        if file.endswith('.csv'):
            datasets.append(read_csv(file))
        elif file.endswith('.json'):
            datasets.append(read_json(file))
        else:
            print(f"Arquivo {file} não é um arquivo CSV ou JSON.")

    with open(ttl_file, 'a', encoding='utf-8') as f:  
        f.write(Individuals(datasets))  
    
    print(f"Dados dos arquivos {files} adicionados a '{ttl_file}' com sucesso!")

csv_and_json_to_ttl(["Disease_Syntoms.csv", "Disease_Treatment.csv","Disease_Description.csv","doentes.json"], "disease.ttl")

def merge_ttl_files(input_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in input_files:
            with open(file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + '\n')

    print(f"Arquivos {input_files} foram mesclados em '{output_file}' com sucesso!")

merge_ttl_files(["med_tratamentos.ttl","disease.ttl"], "med_doentes.ttl")