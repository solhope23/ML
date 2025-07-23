from sklearn.model_selection import train_test_split

class CLN:

    @staticmethod
    def is_target_column_in_table(table, target_column):
        if target_column not in table.columns:
            raise ValueError(f"Target column '{target_column}' not found in table.")


    @staticmethod
    def df_cleaner(table):
        columns_to_remove = CLN._find_unique_value_columns(table)
        return table[[col for col in table.columns if col not in columns_to_remove]]


    @staticmethod
    def _find_unique_value_columns(df):
        return [column for column in df.columns if df[column].nunique() == len(df)]


    @staticmethod
    def split_train_test(df):
        train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)
        return train_df, test_df


    @staticmethod
    def get_table_schema(table):
        table_schema = {}
        for column in table.columns:
            table_schema[column] = table[column].unique().tolist()
        return table_schema