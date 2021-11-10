# sales 1
def add_sales_tax(total, tax_rate):
    return total * tax_rate

# sales 2
tax_rates_by_state ={
"MI": 1.06,
# ....
}

def add_sales_tax(total, state):
    return total * tax_rates_by_states[state]

# sales 3
tax_rates_by_state = {
"mi": 1.06,
# ...
}

def add_sales_tax(total, state):
    tax_rate = tax_rates_by_state[state]
    return total * tax_rate
