def filter_by_state(list_dict: list, state_key: str) -> list:
    new_list_dict = []
    for dict_ in list_dict:
        if dict_["state"] == 'EXECUTED':
            new_list_dict.append(dict_)

    return new_list_dict
