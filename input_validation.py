def input_validation(hours, hourly_rate, discount=0):
    if hours < 0:
        raise ValueError("Hours cannot be negative.")
    if hourly_rate < 0:
        raise ValueError("Hour_rate cannot be negative. ")
    if discount < 0:
        raise ValueError("Discount cannot be negative.")
    total = hours * hourly_rate
    if discount > total:
        raise ValueError("Discount cannot be greater than the total")
    
    final_cost = total - discount
    return final_cost


result1  = input_validation(4, 2000, 1000)
result2 = input_validation(-2, 2000, 0)
print(result1)
print(result2)
