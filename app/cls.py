class CLS:

    @staticmethod
    def classify(question_dict, conditional_dict):
        answer = {}
        for target_value, features in conditional_dict.items():
            used = False
            probability = 1
            for feature, feature_values in features.items():
                if feature in question_dict:
                    if question_dict[feature] in feature_values:
                        probability *= feature_values[question_dict[feature]]
                        used = True
                    # else:
                    #     print(f'A value was inserted that does not exist in the model.')
            if used:
                answer[target_value] = probability
        if answer:
            return answer, max(answer, key=lambda k: answer[k])
        else:
            raise ValueError("No usable features in the input record.")