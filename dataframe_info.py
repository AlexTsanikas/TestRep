import pandas as pd

def dataframe_info(df):
    """
    Gibt eine kompakte Übersicht über ein pandas DataFrame aus.

    Parameter
    ----------
    df : pandas.DataFrame
        Das zu analysierende DataFrame.

    Gibt aus
    ----------
    - Anzahl der Zeilen und Spalten
    - Spaltennamen und Datentypen
    - Anzahl fehlender Werte je Spalte
    - Erste 3 Zeilen als Vorschau
    """
    print("Form:", df.shape)
    print("\nSpalten und Datentypen:\n", df.dtypes)
    print("\nFehlende Werte je Spalte:\n", df.isnull().sum())
    print("\nVorschau:\n", df.head(3))

