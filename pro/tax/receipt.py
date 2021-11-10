from sales_tax import (
     add_sales_tax,
     add_state_tax,
     add_city_tax,
     add_local_millage_tax, ...
)

def print_receipt():
    total = 2.06
    state = 3.06
    print(f"total: {total}")
    print(f"after  tax:  {add_sales_tax(total, state)}")
