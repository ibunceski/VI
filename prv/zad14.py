from constraint import *

termini_simona = [13, 14, 16, 19]
termini_marija = [14, 15, 18]
termini_petar = [12, 13, 16, 17, 18, 19]


def marija_petar(m, p):
    return m + p == 1 or m + p == 2


def constr(m, p, s, vr):
    if s == 0:
        return False

    if s == 1 and vr not in termini_simona:
        return False

    if m == 1 and vr not in termini_marija:
        return False

    if p == 1 and vr not in termini_petar:
        return False

    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", (0, 1))
    problem.addVariable("Simona_prisustvo", (0, 1))
    problem.addVariable("Petar_prisustvo", (0, 1))
    problem.addVariable("vreme_sostanok", (range(12, 20)))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(constr, ["Marija_prisustvo", "Petar_prisustvo", "Simona_prisustvo", "vreme_sostanok"])
    problem.addConstraint(marija_petar, ["Marija_prisustvo", "Petar_prisustvo"])
    # ----------------------------------------------------

    keys = ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok")
    for solution in problem.getSolutions():
        ordered = {key: solution[key] for key in keys}
        print(ordered)
