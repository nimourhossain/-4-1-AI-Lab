import itertools

foods = ["chicken", "Rice", "Beans", "Brocoli", "Milk"]
costs = [2.0, 0.5, 1.0, 1.5, 1.2]
nutrients = [
    [250,200,150,50,100],
    [30,4,10,4,8],
    [5,1,1,0,4]
]
required_min = [2000, 50, 20]
required_max = [2500, 200, 70]

def objective_function(amounts):
    total_cost = sum(a*c for a,c in zip(amounts, costs))
    nutrient_totals = [sum(amounts[j]*nutrients[i][j] for j in range(len(foods))) for i in range(len(nutrients))]
    penalty = 0
    for i in range(len(nutrients)):
        if nutrient_totals[i] < required_min[i]:
            penalty += (required_min[i] - nutrient_totals[i]) ** 2 * 100
        if nutrient_totals[i] > required_max[i]:
            penalty += (nutrient_totals[i] - required_max[i]) ** 2 * 100     
    negative_penalty = sum(abs(min(0,a)) for a in amounts) * 100
    return -(total_cost + penalty + negative_penalty)

def generate_neighbors(state, step=0.1):
    neighbors = []
    for i in range(len(state)):
        for delta in [-step, step]:  # প্রতিটি item সামান্য বাড়ানো বা কমানো
            neighbor = state[:]
            neighbor[i] += delta
            neighbors.append(neighbor)
    return neighbors

def steepest_ascent_hill_climbing(max_iteration=1000):
    state = [2.5]*len(foods)  # শুরুতে মধ্যমান দিয়ে শুরু করা (deterministic)
    best_score = objective_function(state)
    
    for _ in range(max_iteration):
        neighbors = generate_neighbors(state)
        neighbor_scores = [(n, objective_function(n)) for n in neighbors]
        best_neighbor, best_neighbor_score = max(neighbor_scores, key=lambda x: x[1])
        
        if best_neighbor_score > best_score:
            state, best_score = best_neighbor, best_neighbor_score
        else:
            break  # কোন neighbor current state-এর চেয়ে ভালো না হলে থামো
    
    return state, best_score

state, score = steepest_ascent_hill_climbing()
print("Food amounts:", [round(w,3) for w in state])
print("Score:", round(score,4))
