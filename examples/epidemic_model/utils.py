def states(model):
    s, i, r = 0, 0, 0
    for agent in model.schedule.agents:
        if agent.state == 0:
            s += 1
        elif agent.state == 1:
            i += 1
        else:
            r += 1
    return [s, i, r]


def susc(model):
    return states(model)[0]


def inf(model):
    return states(model)[1]


def rec(model):
    return states(model)[2]
