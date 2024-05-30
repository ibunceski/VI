from searching_framework import Problem, astar_search


def generate_cords(direction):
    #    actions = ("SvrtiLevo", "ProdolzhiPravo", "SvrtiDesno")

    if direction == "nadolu":
        return ((0, -1), "nadolu"), ((-1, 0), "nalevo"), ((1, 0), "nadesno")
    elif direction == "nagore":
        return ((0, 1), "nagore"), ((1, 0), "nadesno"), ((-1, 0), "nalevo")
    elif direction == "nadesno":
        return ((1, 0), "nadesno"), ((0, -1), "nadolu"), ((0, 1), "nagore")
    elif direction == "nalevo":
        return ((-1, 0), "nalevo"), ((0, 1), "nagore"), ((0, -1), "nadolu")
    else:
        return None


class SnakeGame(Problem):

    def __init__(self, initial):
        super().__init__(initial)

    def goal_test(self, state):
        return len(state[2]) == 0

    def successor(self, state):
        successors = {}

        actions = ("ProdolzhiPravo", "SvrtiDesno", "SvrtiLevo")
        directions = generate_cords(state[1])

        for act, dir in zip(actions, directions):
            rez = self.move(state, dir)
            if rez is not None:
                successors[act] = rez

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def move(self, state, dir):
        d, nasoka = dir
        dx, dy = d

        snake = list(state[0])

        sx, sy = snake.pop()
        snake.append((sx, sy))
        new_sx, new_sy = sx + dx, sy + dy

        new_snake = snake[1:] + [(new_sx, new_sy)]

        zeleni = list(state[2])
        if (new_sx, new_sy) in zeleni:
            new_snake = [snake[0]] + new_snake
            zeleni.remove((new_sx, new_sy))

        new_state = (tuple(new_snake), nasoka, tuple(zeleni))

        if self.is_state_valid(new_state):
            return new_state
        else:
            return None

    def is_state_valid(self, state):
        snake = list(state[0])
        sx, sy = snake.pop()

        if not (0 <= sx < 10 and 0 <= sy < 10):
            return False

        if (sx, sy) in snake:
            return False

        return True

    def h(self, node):
        state = node.state

        snake = list(state[0])
        zeleni = state[2]

        sx, sy = snake.pop()

        distances = [abs(sx - j[0]) + abs(sy - j[1]) for j in zeleni]
        if len(distances) == 0:
            return 0

        return max(distances)
        # avg = 0
        # for dist in distances:
        #     avg+=dist
        #
        # return avg/(len(distances))



if __name__ == "__main__":
    zeleni_num = int(input())

    zeleni = []

    for i in range(zeleni_num):
        zeleni.append(tuple(map(int, input().split(","))))

    problem = SnakeGame((((0, 9), (0, 8), (0, 7)), "nadolu", tuple(zeleni)))

    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("Problem")
