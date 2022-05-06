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
        return (0, 1) if sum(mensalidades) == target else (None, None)

    mensalidades_dict = {}
    for index, mensalidade in enumerate(mensalidades, start=0):
        value = mensalidades_dict.get(mensalidade, [])
        value.append(index)
        mensalidades_dict.update({mensalidade: value})

    for value in mensalidades_dict.keys():
        amount_due = target - value
        if amount_due == value:
            if len(mensalidades_dict.get(value)) >= 2:
                index, index2 = mensalidades_dict.get(value)[:2]
                return index, index2
        else:
            index = mensalidades_dict.get(value)[0]
            if mensalidades_dict.get(amount_due):
                index2 = mensalidades_dict.get(amount_due)[0]
                return index, index2
    return None, None
