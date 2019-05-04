import copy as cp


def cell_complete(states, days):
    # representation of adjacent vertice List
    # 0 -> adjacent 0
    # 1 -> adjacent 0, 2
    # 2 -> adjacent 1, 2
    # graph = {
    #     0: [states[0]],
    #     1: [states[0], states[2]],
    #     2: [states[1], states[3]],
    #     3: [states[2], states[4]],
    #     4: [states[3], states[5]],
    #     5: [states[4], states[6]],
    #     6: [states[5], states[7]],
    #     7: [states[6]
    # }
    states_copy = cp.copy(states)
    k = days
    while k > 0:
        # corner case and 0 and 8
        states_copy[0] = 0 ^ states[1]
        states_copy[7] = 0 ^ states[6]

        # intermediary cells between 1, 6
        for i in range(1, 7):
            states_copy[i] = states[i - 1] ^ states[i + 1]
        # prepare following iteration
        states = cp.copy(states_copy)
        k -= 1
    print(states_copy)
    return states_copy


t1 = [1, 0, 0, 0, 0, 1, 0, 0]
cell_complete(t1, 1)  # 0 1 0 0 1 0 1 0
t2 = [1, 1, 1, 0, 1, 1, 1, 1]
cell_complete(t2, 2)  # 0 0 0 0 0 1 1 0
