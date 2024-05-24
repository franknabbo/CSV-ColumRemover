import pandas as pd

# Funzione per rimuovere una colonna da un file CSV
def rimuovi_colonna(file_input, file_output, colonna_da_rimuovere):
    # Leggi il file CSV
    df = pd.read_csv(file_input)
    
    # Verifica se la colonna esiste
    if colonna_da_rimuovere in df.columns:
        # Rimuovi la colonna
        df.drop(columns=[colonna_da_rimuovere], inplace=True)
        # Salva il risultato in un nuovo file CSV
        df.to_csv(file_output, index=False)
        print(f"Colonna '{colonna_da_rimuovere}' rimossa con successo.")
    else:
        print(f"La colonna '{colonna_da_rimuovere}' non esiste nel file CSV.")

# Esempio di utilizzo
file_input = 'file.csv'
file_output = 'nuovo_file.csv'
colonna_da_rimuovere = ''  # Sostituisci con il nome della colonna da rimuovere

rimuovi_colonna(file_input, file_output, colonna_da_rimuovere)
