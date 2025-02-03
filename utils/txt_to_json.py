import json
import os
import chardet

def txt_to_json(uploaded_file):
    data = {}
    
    # Define o caminho do diretório onde o JSON será salvo
    output_directory = 'media/json_files'
    
    # Cria o diretório se não existir
    os.makedirs(output_directory, exist_ok=True)
    
    # Extrai o nome do arquivo original e substitui a extensão
    original_filename = uploaded_file.name
    json_filename = os.path.splitext(original_filename)[0] + '.json'
    
    # Define o caminho completo do arquivo JSON
    json_file = os.path.join(output_directory, json_filename)
    
    # Lê o conteúdo do arquivo carregado
    raw_data = uploaded_file.read()
    
    # Detecta a codificação do arquivo
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    
    # Decodifica o conteúdo com a codificação detectada
    lines = raw_data.decode(encoding).splitlines()
    
    # Ignorar as linhas iniciais até encontrar a seção do resumo
    in_summary = False
    
    for line in lines:
        line = line.strip()
        
        # Começar a ler o resumo
        if line.startswith("[Resumo do Sistema]"):
            in_summary = True
            continue
        elif line.startswith("[Recursos de Hardware]"):
            in_summary = False
            continue
        
        # Processar apenas as linhas do resumo
        if in_summary and line:
            # Separar chave e valor
            if '\t' in line:  # Verifica se a linha contém uma tabulação
                key, value = line.split('\t', 1)  # Divide apenas na primeira tabulação
                data[key.strip()] = value.strip()
    
    # Escrever os dados no formato JSON
    with open(json_file, 'w', encoding='utf-8') as json_out:
        json.dump(data, json_out, ensure_ascii=False, indent=4)