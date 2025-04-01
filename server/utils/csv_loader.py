import pandas as pd

def load_csv(file_path):
    """
    Carrega um arquivo CSV e retorna um DataFrame do pandas.
    
    Args:
        file_path (str): Caminho para o arquivo CSV.
    
    Returns:
        pd.DataFrame: DataFrame contendo os dados do CSV.
    """
    try:
        # Especificar o delimitador como ponto e vírgula
        return pd.read_csv(file_path, sep=';', on_bad_lines='skip', encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo CSV não encontrado: {file_path}")
    except Exception as e:
        raise Exception(f"Erro ao carregar o arquivo CSV: {e}")