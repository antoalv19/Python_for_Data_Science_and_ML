import pandas as pd
import numpy as np

# Create new Dataframe
df = pd.DataFrame({'A': [1, 2, np.nan],
                   'B': [5, np.nan, np.nan],
                   'C': [1, 2, 3]})

# df.dropna() droppa tutte le righe dove ci sono NaN, per colonna se axis = 1
df.dropna()
df.dropna(axis=1)  # per colonna

# tramite comando thresh specifichi il numero di valori minimi dopo i quali droppare e.g. almeno 2 NaN
df.dropna(thresh=2)

# metodo FILLNA inserisce un valore alternativo al posto dei NaN
df.fillna(value="FILLATO_X")

# i valori NaN possono essere sostituiti tramite FILLNA anche con statistiche
print(df["A"].fillna(value=df["A"].mean()))
