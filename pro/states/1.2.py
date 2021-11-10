# 1.2 wrapping the states capitals logic in function
def get_united_states_capitals():
    us_capitals_by_state = { "Alabamas": "Montgomery", "Alaska": "Juneau" }
    # add values

    us_capitals = sorted(us_capitals_by_state.values())
    # capitals = us_capitals_by_state.values()
    #  rt capitals
    return sorted(us_capitals)
print(sorted(us_capitals))
