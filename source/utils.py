import random
from typing import Dict, Any


def dict_sample(options: Dict[Any, float]) -> Any:
    value_sum = 0
    for key in options.keys():
        value_sum += options[key]
    for key in options.keys():
        options[key] = options[key] / value_sum if value_sum > 0 else 1

    rand = random.uniform(0, 1)
    prob_accumulated = 0
    option_chosen_key = None
    for key in options.keys():
        prob_accumulated += options[key]
        if prob_accumulated >= rand:
            option_chosen_key = key
            break
    return option_chosen_key