import pandas as pd  # Certifique-se de importar o Pandas

def search_in_dataframe(dataframe, query):
    """
    Realiza uma busca textual em um DataFrame.

    Args:
        dataframe (pd.DataFrame): O DataFrame onde a busca será realizada.
        query (str): O termo de busca.

    Returns:
        list: Lista de dicionários contendo os registros que correspondem à busca.
    """
    if not query:
        raise ValueError("O termo de busca não pode estar vazio.")

    # Filtrar os registros que contêm o termo de busca em qualquer coluna
    filtered_data = dataframe[
        dataframe.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)
    ]

    # Converter todas as colunas para strings
    filtered_data = filtered_data.astype(str)

    # Substituir valores "nan" (resultantes da conversão) por None
    filtered_data = filtered_data.replace("nan", None)

    # Retornar os resultados como uma lista de dicionários
    return filtered_data.to_dict(orient='records')