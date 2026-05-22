def generate_age_numproducts_score(row):
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
    if row["IsActiveMember"] == 1:
        multiplier = 1.2
    if row["IsActiveMember"] == 0:
        multiplier = 1

    balance = row["Balance"]

    return balance * multiplier


def generate_AgeAndSalary_score(row):
    score = row["EstimatedSalary"] / row["Age"]

    return score