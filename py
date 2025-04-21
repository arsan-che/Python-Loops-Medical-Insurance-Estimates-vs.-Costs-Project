# List of names of individuals
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]

# List of estimated insurance costs for each individual
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]

# List of actual insurance costs for each individual
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Initialize total cost to 0
total_cost = 0
# Calculate the total of all actual insurance costs
for cost in actual_insurance_costs:
    total_cost += cost

# Calculate the average insurance cost
average_cost = total_cost / len(actual_insurance_costs)

# Print the average insurance cost
print(f'Average Insurance Cost: {average_cost} dollars.')
# Iterate over each individual to compare their insurance cost to the average
for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
    
    # Check if the insurance cost is above average
    if insurance_cost > average_cost:
        print("The insurance cost for " + name + " is above average.")
    
    # Check if the insurance cost is below average
    elif insurance_cost < average_cost:
        print("The insurance cost for " + name + " is below average.")

# Create a new list of updated estimated costs, increasing each by 10%
updated_estimated_costs = [i * 11 / 10 for i in estimated_insurance_costs]

# Print the updated estimated costs
print(updated_estimated_costs)
    
    # Check if the insurance cost is equal to the average
    else:
        print("The insurance cost for " + name + " is equal to the average.")
