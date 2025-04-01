import pandas as pd
import unicodedata

def remove_accents(text):
    """
    Remove acentos de um texto.
    """
    if not isinstance(text, str):
        return text
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def search_in_dataframe(dataframe, query):
    """
    Realiza uma busca textual no DataFrame e retorna os registros mais relevantes.
    """
    query = remove_accents(query.lower())  # Normalizar o texto e remover acentos
    
    relevant_columns = ['Razao_Social', 'Nome_Fantasia', 'Cidade', 'UF', 'Modalidade', 'Telefone', 'Endereco_eletronico']  # Campos relevantes

    # Transformar todos os valores dos campos relevantes em strings, lidar com valores nulos e remover acentos
    dataframe[relevant_columns] = dataframe[relevant_columns].fillna('').astype(str).applymap(remove_accents)

    # Filtrar os registros onde a query está contida em algum valor dos campos relevantes
    filtered_df = dataframe[dataframe[relevant_columns].apply(
        lambda row: any(query in value.lower() for value in row), axis=1
    )]

    # Garantir que todos os valores no DataFrame sejam serializáveis em JSON
    filtered_df = filtered_df.fillna('').replace({pd.NA: '', None: ''})

    return filtered_df.to_dict(orient='records')  # Retornar os resultados como uma lista de dicionários