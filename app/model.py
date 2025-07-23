class Model:

    def __init__(self, conditional_dict : dict[str, dict[str, dict[str, float]]], target_col : str, model_schema : dict[str, list[str]], model_accuracy : float):
        self.conditional_dict = conditional_dict
        self.target_col = target_col
        self.model_schema = model_schema
        self.model_accuracy = model_accuracy




