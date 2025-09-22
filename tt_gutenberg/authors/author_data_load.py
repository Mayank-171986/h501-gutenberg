import pandas as pd

"""
    Load Project Gutenberg data from a CSV file.
"""
def load_gutenberg_data(filepath: str) -> pd.DataFrame:
    
    df = pd.read_csv(filepath)
    return df
