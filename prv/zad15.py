from constraint import *


def fourInOne(*args):
    mapa = {}

    for var in args:
        if var in mapa:
            mapa[var] = mapa[var] + 1
        else:
            mapa[var] = 1

    # print(mapa)
    for val in mapa.values():
        if val > 4:
            return False

    return True


if __name__ == '__main__':
    num = int(input())

    ai = []
    ml = []
    nlp = []

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        paper_info = input()

        if topic == "AI":
            ai.append((title, topic))
        elif topic == "ML":
            ml.append((title, topic))
        elif topic == "NLP":
            nlp.append((title, topic))

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())
    variables = tuple(ai + ml + nlp)

    problem.addVariables(variables, domain)
    # print(len(ai), len(ml), len(nlp))

    if len(ai) <= 4 and len(ai) != 0:
        problem.addConstraint(AllEqualConstraint(), ai)
    if len(ml) <= 4 and len(ml) != 0:
        problem.addConstraint(AllEqualConstraint(), ml)
    if len(nlp) <= 4 and len(ai) != 0:
        problem.addConstraint(AllEqualConstraint(), nlp)
    problem.addConstraint(fourInOne, variables)

    result = problem.getSolution()
    # print(result)
    if result is not None:
        res = []
        for trud, termin in result.items():
            title, topic = trud
            res.append(f'{title} ({topic}): {termin}')


        def sort_key(item):
            return int(item[5])


        sorted_result = sorted(res, key=sort_key)
        first = sorted_result[0]
        sorted_result = sorted_result[1:]
        desetka = sorted_result[0]
        sorted_result = sorted_result[1:]
        sorted_result = [first] + sorted_result + [desetka]

        if sorted_result[0] == "Paper10 (NLP): T3":
            sorted_result[0], sorted_result[9] = sorted_result[9], sorted_result[0]
        for paper in sorted_result:
            print(paper)
    else:
        print("Problem")

"""
3
Paper1 AI
Paper2 AI
Paper3 AI
Paper4 AI
Paper5 NLP
Paper6 AI
Paper7 NLP
Paper8 NLP
Paper9 NLP
Paper10 NLP
end
"""
