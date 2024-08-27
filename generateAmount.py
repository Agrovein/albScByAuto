import math
def generateAmount(sold_count_str, budget, item_level_str):
    # Convert sold_count and item_level to integers
    try:
        sold_count = int(sold_count_str)
    except ValueError:
        raise ValueError("Invalid input: sold_count must be a string representing an integer")

    try:
        item_level = int(item_level_str)
    except ValueError:
        raise ValueError("Invalid input: item_level must be a string representing an integer")

    # Calculate base amount as 5% of sold_count
    base_amount = 0.03 * sold_count


    # Modify base amount based on budget
    if budget < 1000000:
        base_amount *= 0.2
    elif 1000000 <= budget < 2000000:
        base_amount *= 0.3
    elif 2000000 <= budget < 3000000:
        base_amount *= 0.4
    elif 3000000 <= budget < 4000000:
        base_amount *= 0.5
    elif 4000000 <= budget < 5000000:
        base_amount *= 0.6
    elif 5000000 <= budget < 6000000:
        base_amount *= 0.7
    elif 6000000 <= budget < 7000000:
        base_amount *= 0.8
    elif 7000000 <= budget < 8000000:
        base_amount *= 0.9
    elif 8000000 <= budget < 9000000:
        base_amount *= 1.0
    elif 9000000 <= budget < 10000000:
        base_amount *= 1.0
    elif 10000000 <= budget < 15000000:
        base_amount *= 1.1
    elif 15000000 <= budget < 20000000:
        base_amount *= 1.2
    elif 20000000 <= budget < 30000000:
        base_amount *= 1.3
    elif 30000000 <= budget < 40000000:
        base_amount *= 1.4
    elif 40000000 <= budget < 50000000:
        base_amount *= 1.5
    elif 50000000 <= budget < 60000000:
        base_amount *= 1.6
    elif 60000000 <= budget < 70000000:
        base_amount *= 1.7
    elif 70000000 <= budget < 80000000:
        base_amount *= 1.8
    elif 80000000 <= budget < 90000000:
        base_amount *= 1.9
    elif 90000000 <= budget < 100000000:
        base_amount *= 2.0
    else:
        base_amount *= 2.2  # Default multiplier for very high budgets

    # Ensure minimum amount is 1
    purchase_amount = round(max(1, math.ceil(base_amount)))
    
    return purchase_amount
