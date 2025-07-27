from app.cls import CLS

class VLD:

    @staticmethod
    def _gen_row_to_dict(table):
        for row in table.iterrows():
            yield row[1].to_dict()

    @staticmethod
    def _is_success(cf, target_value):
        if cf == target_value:
            return True

    @staticmethod
    def _get_accuracy_percentage(success_counter, len_of_table):
        return (success_counter / len_of_table) * 100

    @staticmethod
    def _remove_key(dictionary, key):
        return {k: v for k, v in dictionary.items() if k != key}

    @staticmethod
    def testing(test_table, target_column, conditional_dict):
        success_counter = 0
        for row_to_dict in VLD._gen_row_to_dict(test_table):
            row_without_target = VLD._remove_key(row_to_dict, target_column)
            cf = CLS.classify(row_without_target, conditional_dict)
            if VLD._is_success(cf, row_to_dict[target_column]):
                success_counter += 1
        return VLD._get_accuracy_percentage(success_counter, len(test_table))