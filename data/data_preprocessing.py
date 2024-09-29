import os
import pandas as pd


class DataProcessor:
    """Class for processing raw data files and saving processed data."""
    def __init__(self, raw_data_folder, processed_data_folder):
        """
        Initializes the DataProcessor with raw and processed data folders.

        :param raw_data_folder: Path to the folder containing raw data files.
        :param processed_data_folder:
            Path to the folder where processed data will be saved.
        """
        self.raw_data_folder = raw_data_folder
        self.processed_data_folder = processed_data_folder

    def from_file(self, filename, delimiter):
        """
        Load a CSV file and return a DataFrame.

        :param filename: Name of the file to load.
        :param delimiter: Column separator.
        :return: Loaded DataFrame.
        """
        return pd.read_csv(filename, delimiter=delimiter)

    def process_files(self):
        """
        Process CSV files in the raw data folder and save them
            in the processed data folder.
        """
        # Load files from the raw data folder
        df1 = self.from_file(
            os.path.join(self.raw_data_folder, 'donantes.csv'), ',')
        df2 = self.from_file(
            os.path.join(self.raw_data_folder, 'proveedores.csv'), ',')
        df3 = self.from_file(
            os.path.join(self.raw_data_folder, 'detalle_Ing_Egre.csv'), ',')

        # Convert column names to lowercase
        df1.columns = df1.columns.str.lower()
        df2.columns = df2.columns.str.lower()
        df3.columns = df3.columns.str.lower()

        # Drop unwanted columns
        columns_to_drop_df1 = ['nombre.1', 'razon social', 'cargo']
        df1 = df1.drop(columns=columns_to_drop_df1, errors='ignore')

        columns_to_drop_df2 = ['nombre proveedor.1', 'razón social']
        df2 = df2.drop(columns=columns_to_drop_df2, errors='ignore')

        # Replace '-' with empty string in all data
        df1 = df1.replace('-', '', regex=True)

        # Rename columns
        df1, df2, df3 = self.rename_columns(df1, df2, df3)

        # Convert dates to datetime
        df1, df2 = self.convert_dates_and_clean(df1, df2)

        # Store the processed DataFrames
        self.save_processed_data(df1, df2, df3)

    def rename_columns(self, df1, df2, df3):
        """
        Rename columns in the DataFrames.

        :param df1: DataFrame of donors.
        :param df2: DataFrame of suppliers.
        :param df3: DataFrame of income/expenditure.
        :return: DataFrames with renamed columns.
        """
        df1 = df1.rename(columns={
            'número': 'numero',
            'correo electrónico': 'correo',
            'tipo de contribuyente': 'tipo_contribuyente',
            'nro de cuenta': 'nro_cuenta',
            'fecha de la donacion': 'fecha_donacion',
            'teléfono': 'telefono'
        })

        df2 = df2.rename(columns={
            'número proveedor': 'nro_proveedor',
            'nombre proveedor': 'nombre_proveedor',
            'categor/a proveedor': 'categoria_proveedor',
            'tipo de contribuyente': 'tipo_contribuyente',
            'correo electrónico': 'correo',
            'teléfono': 'telefono'
        })

        df3 = df3.rename(columns={
            'nro de cuenta': 'nro_cuenta',
            'nombre de cuenta': 'nombre_cuenta',
            'tipo de cuenta': 'tipo_cuenta',
            'tipo de contribuyente': 'tipo_contribuyente',
            'descripción': 'descripcion'
        })

        return df1, df2, df3

    def convert_dates_and_clean(self, df1, df2):
        """
        Convert date columns to datetime type, clean the 'importe'
        columns, and return the processed DataFrames.

        :param df1: DataFrame of donors.
        :param df2: DataFrame of suppliers.
        :return: Processed DataFrames (df1 and df2).
        """
        # Convert date columns to datetime
        date_columns_df1 = ['alta', 'baja', 'fecha_donacion']
        date_columns_df2 = ['fecha']

        df1[date_columns_df1] = df1[date_columns_df1].apply(
            pd.to_datetime, errors='coerce', dayfirst=True)
        df2[date_columns_df2] = df2[date_columns_df2].apply(
            pd.to_datetime, errors='coerce', dayfirst=True)

        # Standardize and clean 'importe' column in both DataFrames
        for df in [df1, df2]:
            if 'importe' in df.columns:
                df['importe'] = df['importe'].str.replace(
                    r'[\$,]', '', regex=True).str.strip()
                df['importe'] = pd.to_numeric(df['importe'], errors='coerce')

        # Correct specific text replacements in df2
        df2['categoria_proveedor'] = df2['categoria_proveedor'].replace(
            'AGENTE /MPOSITIVO', 'AGENTE /IMPOSITIVO')

        return df1, df2

    def save_processed_data(self, df1, df2, df3):
        """
        Save the processed DataFrames to CSV files.

        :param df1: DataFrame of donors.
        :param df2: DataFrame of suppliers.
        :param df3: DataFrame of income/expenditure.
        """
        os.makedirs(self.processed_data_folder, exist_ok=True)

        df1.to_csv(
            os.path.join(self.processed_data_folder,
                         'donantes.csv'), index=False)
        df2.to_csv(
            os.path.join(self.processed_data_folder,
                         'proveedores.csv'), index=False)
        df3.to_csv(
            os.path.join(self.processed_data_folder,
                         'ingreso_egreso.csv'), index=False)


# Usage of the class
raw_data_folder = 'raw_data'
processed_data_folder = 'processed_data'
processor = DataProcessor(raw_data_folder, processed_data_folder)
processor.process_files()
