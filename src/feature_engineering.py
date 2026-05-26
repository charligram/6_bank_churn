def generate_age_numproducts_score(row):
    """
    Asigna un valor numérico a cada grupo etario, también para el número de productos. Devolver el producto de la multiplicación
    cada número asignado.

    Args:
        row (pd.Series): Serie que hace alución a 1 registro o fila del DataFrame.

    Returns:
        (int): Score obtenido.
    """
    if row["AgeGroup"] == "Young adult":
        age_score = 4

    if row["AgeGroup"] == "Adult":
        age_score = 3

    if row["AgeGroup"] == "Middle Age":
        age_score = 0.5

    if row["AgeGroup"] == "Senior":
        age_score = 2

    diccionario_numproducts_score = {
        1: 3,
        2: 4,
        3: 2,
        4: 1
    }

    ptj_numproducts = diccionario_numproducts_score.get(row["NumOfProducts"])

    return age_score * ptj_numproducts

def generate_balance_and_active_score(row):
    """
    Generar puntaje generando una tasa de multiplicador del balance, dependiendo de si es un miembro activo o no.

    Args:
        row (pd.Series): Serie que hace alución a 1 registro o fila del DataFrame.

    Returns:
        (int): Producto del multiplicador y balance.
    """
    if row["IsActiveMember"] == 1:
        multiplier = 1.2
    if row["IsActiveMember"] == 0:
        multiplier = 1

    balance = row["Balance"]

    return balance * multiplier


def generate_AgeAndSalary_score(row):
    """
    Generar puntaje que hace alución al potencial o capacidad de compra de un cliente.

    Args:
        row (pd.Series): Serie que hace alución a 1 registro o fila del DataFrame.
        
    Returns
        (int): Resultado de la división de EstimatedSalary entre Age
    """
    score = row["EstimatedSalary"] / row["Age"]

    return score