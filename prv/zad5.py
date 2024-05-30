from constraint import *


def addPredavanja(prob, what, num, all, domain):
    for i in range(num):
        all.append(f'{what}_cas_{i + 1}')
        prob.addVariable(f'{what}_cas_{i + 1}', domain)


def all_constraint(var1, var2):
    den1, cas1 = tuple(var1.split("_"))
    den2, cas2 = tuple(var2.split("_"))

    if den1 == den2 and abs(int(cas1) - int(cas2)) < 2:
        return False

    return True


def ml_constraint(var1, var2):
    den1, cas1 = tuple(var1.split("_"))
    den2, cas2 = tuple(var2.split("_"))

    return cas1 != cas2


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    all = []
    ml = []
    # ---Tuka dodadete gi promenlivite--------------------
    addPredavanja(problem, "AI", casovi_AI, all, AI_predavanja_domain)

    for i in range(casovi_ML):
        all.append(f'ML_cas_{i + 1}')
        ml.append(f'ML_cas_{i + 1}')
        problem.addVariable(f'ML_cas_{i + 1}', ML_predavanja_domain)

    addPredavanja(problem, "R", casovi_R, all, R_predavanja_domain)
    addPredavanja(problem, "BI", casovi_BI, all, BI_predavanja_domain)

    str = ("AI_vezbi", "ML_vezbi", "BI_vezbi")

    [all.append(elem) for elem in str]
    ml.append(str[1])

    problem.addVariable(str[0], AI_vezbi_domain)
    problem.addVariable(str[1], ML_vezbi_domain)
    problem.addVariable(str[2], BI_vezbi_domain)

    for i in range(len(all)):
        for j in range(i + 1, len(all)):
            problem.addConstraint(all_constraint, [all[i], all[j]])

    for i in range(len(ml)):
        for j in range(i + 1, len(ml)):
            problem.addConstraint(ml_constraint, [ml[i], ml[j]])

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
