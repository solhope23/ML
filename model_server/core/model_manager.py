from .dat import DAT
from .cln import CLN
from .bld import BLD
from .vld import VLD
from .model import Model

class ModelManager:

    @staticmethod
    def builder():
        table = DAT.load_csv()
        table = CLN.df_cleaner(table)
        target_column = table.columns[-1]
        model_schema = CLN.get_table_schema(table)
        table_70, table_30 = CLN.split_train_test(table)
        conditional_dict = BLD.train(table_70, target_column, model_schema)
        model_accuracy = VLD.testing(table_30, target_column, conditional_dict)
        return Model(conditional_dict, target_column, model_schema, model_accuracy)