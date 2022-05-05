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
    if len(mensalidades) == 2:
        return [0, 1] if sum(mensalidades) == target else [None, None]

    potential_values = sorted(mensalidades)
    index_cut = bisect_right(potential_values, target)
    potential_values = potential_values[:index_cut] if index_cut < len(potential_values) else potential_values

    result = []
    index = 0
    for value in potential_values:
        amount_due = target - value
        if amount_due >= value:
            result.append(index)
            index += 1
            for index2, value2 in enumerate(potential_values[index:], start=index):
                if amount_due - value2 == 0:
                    result.append(index2)
                    return result
            result = []

    return result
