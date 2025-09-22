import pandas as pd
from .author_data_load import load_gutenberg_data

def list_authors(by_languages=True, alias=True) -> list:
    """
    Return a list of author aliases sorted by translation count (descending).
    """

    df_author = load_gutenberg_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    df_language = load_gutenberg_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
    df_metadata = load_gutenberg_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
    df_subjects = load_gutenberg_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')
    
    if by_languages and alias:
        df_author_metadata = pd.merge(df_author, df_metadata, on = 'gutenberg_author_id', how = 'inner')
        df_author_metadata_language = pd.merge(df_author_metadata, df_language, on = 'gutenberg_id', how = 'inner')

        df_translated_book_data = df_author_metadata_language.loc[df_author_metadata_language['total_languages'] > 1]
        author_with_translated_data = df_translated_book_data .groupby('alias')['total_languages'].sum()
        df_sorted = author_with_translated_data.sort_values(ascending=False)
        alias_list = df_sorted.index.tolist()
        return alias_list
    raise NotImplementedError("Only by_languages=True and alias=True is currently supported.")
