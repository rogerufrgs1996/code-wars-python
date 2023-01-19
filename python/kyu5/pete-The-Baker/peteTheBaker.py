def cakes(recipe, available):
    receita = set(recipe)
    disponivel = set(available)
    qt = []
    if len(receita.intersection(disponivel)) == len(recipe):
        for ingrediente in recipe:
            qt.append(available.get(ingrediente) // recipe.get(ingrediente))
        return min(qt)
    else:
        return 0
