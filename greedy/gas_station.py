# There are n gas stations arranged in a circular route. You are given two arrays:
#
# gas: The amount of gas available at each station.
# cost: The amount of gas required to travel from the current station to the next.
from selectors import SelectSelector


# You start with an empty tank of gas at a station. Your goal is to determine:
#
# The starting gas station index where you can complete the circuit once, or
# Return -1 if it's not possible to complete the circuit.

def can_complete_circuit(gas, cost):
    """
    Approach is simple, we have to skip the indexes where the current tank value becomes zero
    We first have two variables, total and current for fuel(gas).
    Start will start with zero and then it skips many stations to i + 1
    If at any point in time, if the current becomes negative, skip to the i + 1 index
    Return start if total_gas is still non-negative
    :param gas:
    :param cost:
    :return:
    """
    n = len(gas)
    total_gas = 0
    current_gas = 0
    start = 0

    for i in range(n):
        total_gas = total_gas + gas[i] - cost[i]
        current_gas = current_gas + gas[i] - cost[i]

        if current_gas < 0:
            current_gas = 0
            start = i + 1

    return start if total_gas >= 0 else -1

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print(f"The starting gas index where car can complete circuit: {can_complete_circuit(gas, cost)}")