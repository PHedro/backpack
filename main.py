from bisect import bisect_right


def recupera_indice_faturas(mensalidades, target):
    indice_atual = 0
    for mensalidade in mensalidades:
        indice_2 = 0
        for mensalidade2 in mensalidades:
            if (
                indice_2 != indice_atual
                and target == mensalidade2 + mensalidade
            ):
                return indice_atual, indice_2
            indice_2 += 1
        indice_atual += 1


def recupera_indice_faturas_amortizado(mensalidades, target):
    mensalidades_dict = {}
    if len(mensalidades) == 2:
        return [0, 1] if sum(mensalidades) == target else [None, None]

    for index, mensalidade in enumerate(mensalidades, start=0):
        indexes = mensalidades_dict.get(mensalidade, [])
        indexes.append(index)
        mensalidades_dict.update({mensalidade: indexes})

    potential_values = sorted(list(mensalidades_dict.keys()))
    index_cut = bisect_right(potential_values, target)
    potential_values = potential_values[:index_cut] if index_cut < len(potential_values) else potential_values

    result = []
    for index, value in enumerate(potential_values, start=0):
        indexes_in = mensalidades_dict.get(value)
        amount_due = target - value
        if amount_due == value and len(indexes_in) > 1:
            result = indexes_in[:2]
        elif amount_due > value:
            result.append(indexes_in[0])
            for index2, value2 in enumerate(potential_values[index:], start=0):
                if amount_due - value2 == 0:
                    result.append(mensalidades_dict.get(value2)[0])
                    return result
            result = []

    return result
