class BLD:

    @staticmethod
    def train(table, target_column, model_schema):
        model_dict = {}
        BLD._count_feature_values(model_dict, table, target_column)
        BLD._apply_laplace_smoothing(model_dict, model_schema, target_column)
        BLD._calculate_conditional_probabilities(model_dict)
        return model_dict


    @staticmethod
    def _count_feature_values(model_dict, table, target_column):
        target_values = table[target_column].unique()
        columns = [col for col in table.columns if target_column != col]
        for target_value in target_values:
            new_table = table[table[target_column] == target_value]
            model_dict[target_value] = {}
            for column in columns:
                model_dict[target_value][column] = new_table[column].value_counts().to_dict()


    @staticmethod
    def _apply_laplace_smoothing(model_dict, model_schema, target_column):
        for target_value, features in model_dict.items():
            for feature, feature_values in model_schema.items():
                if feature != target_column:
                    for feature_value in feature_values:
                        if feature_value in model_dict[target_value][feature]:
                            model_dict[target_value][feature][feature_value] += 1
                        else:
                            model_dict[target_value][feature][feature_value] = 1


    @staticmethod
    def _calculate_conditional_probabilities(model_dict):
        for target_value, features in model_dict.items():
            for feature, feature_values in features.items():
                count_feature_values = sum(model_dict[target_value][feature].values())
                for feature_value in feature_values:
                    model_dict[target_value][feature][feature_value] /= count_feature_values