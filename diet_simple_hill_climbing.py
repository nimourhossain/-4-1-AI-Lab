import random

foods = ["chicken", "Rice", "Beans", "Brocoli", "Milk"]
costs = [2.0, 0.5, 1.0, 1.5, 1.2]
nutrients=[
    [250,200,150,50,100],
    [30,4,10,4,8],
    [5,1,1,0,4]
]
required_min = [2000, 50, 20]
required_max = [2500, 200, 70]

def objective_function(amounts):
    total_cost = sum(a*c for a,c in zip(amounts, costs) )
    nutrient_totals = [0]* len(nutrients)
    for i in range(len(nutrients)):
        nutrient_totals[i] = sum(amounts[j] * nutrients[i][j] for j in range(len(foods)))
    penalty = 0
    for i in range (len(nutrients)):
        if nutrient_totals[i] < required_min[i]:
            penalty += (required_min[i] - nutrient_totals[i]) **2 *100
        if nutrient_totals[i] > required_max[i]:
            penalty += (required_min[i] - nutrient_totals[i]) **2 *100     
            
    negative_penalty = sum(abs(min(0,a)) for a in amounts) *100
    return -(total_cost + penalty + negative_penalty)

def random_neighbor(state, step = 0.1):
    neighbor = state[:]
    idx = random.randint(0, len(state) - 1)
    change = random.uniform(-step, step)
    neighbor[idx] +=change
    return neighbor

def hill_climbing(max_iteration=1000):
    state = [random.uniform(0,5) for _ in foods] 
    best_score = objective_function(state)
    
    for _ in range(max_iteration):
        neighbor = random_neighbor(state)
        score = objective_function(neighbor)
        if score > best_score:
            state, best_score = neighbor, score
            
    return state, best_score

state, score = hill_climbing()

print("food amounts:",  [round(w, 3) for w in state])
print("Score:",  round(score, 4))
        
           