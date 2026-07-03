# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []

for costs in travel_costs:
    min_value = min(costs)
    temp_list = []
    for i in range(len(costs)):
        if costs[i] <= 100:
            temp_list.append("Cheap")
        else:
            temp_list.append(costs[i])
    processed_expenses.append(temp_list)


# Testing
print('Processed Travel Expenses:', processed_expenses)