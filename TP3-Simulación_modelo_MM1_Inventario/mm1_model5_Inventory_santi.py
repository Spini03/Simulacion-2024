import numpy as np
import matplotlib.pyplot as plt

class InventorySimulator:
    def __init__(self, initial_inventory, order_point, order_quantity, demand_mean, 
                 lead_time_mean, order_cost, holding_cost, shortage_cost, max_time):
        self.inventory = initial_inventory
        self.order_point = order_point
        self.order_quantity = order_quantity
        self.demand_mean = demand_mean
        self.lead_time_mean = lead_time_mean
        self.order_cost = order_cost
        self.holding_cost = holding_cost
        self.shortage_cost = shortage_cost
        self.max_time = max_time
        
        self.time = 0
        self.last_event_time = 0
        self.next_event_time = 0
        self.order_arrival_time = float('inf')
        
        self.total_order_cost = 0
        self.total_holding_cost = 0
        self.total_shortage_cost = 0
        
        self.inventory_history = [(0, initial_inventory)]
        self.events = []
    
    def run(self):
        self.schedule_event(self.process_demand, np.random.exponential(1/self.demand_mean))
        
        while self.time < self.max_time:
            event, event_time = min(self.events, key=lambda x: x[1])
            self.time = event_time
            event()
            
            if self.time < self.max_time:
                self.update_costs()
    
    def schedule_event(self, event, time):
        self.events.append((event, self.time + time))
    
    def process_demand(self):
        demand = np.random.poisson(self.demand_mean)
        
        if demand <= self.inventory:
            self.inventory -= demand
        else:
            shortage = demand - self.inventory
            self.total_shortage_cost += self.shortage_cost * shortage
            self.inventory = 0
        
        if self.inventory <= self.order_point and self.order_arrival_time == float('inf'):
            self.place_order()
        
        self.inventory_history.append((self.time, self.inventory))
        self.schedule_event(self.process_demand, np.random.exponential(1/self.demand_mean))
    
    def place_order(self):
        self.total_order_cost += self.order_cost
        self.order_arrival_time = self.time + np.random.exponential(self.lead_time_mean)
        self.schedule_event(self.process_order_arrival, self.order_arrival_time - self.time)
    
    def process_order_arrival(self):
        self.inventory += self.order_quantity
        self.order_arrival_time = float('inf')
        self.inventory_history.append((self.time, self.inventory))
    
    def update_costs(self):
        time_diff = self.time - self.last_event_time
        self.total_holding_cost += self.holding_cost * max(self.inventory, 0) * time_diff
        if self.inventory < 0:
            self.total_shortage_cost += self.shortage_cost * (-self.inventory) * time_diff
        self.last_event_time = self.time
    
    def get_total_cost(self):
        return self.total_order_cost + self.total_holding_cost + self.total_shortage_cost

def run_inventory_experiments(initial_inventory, order_point, order_quantity, demand_mean, 
                              lead_time_mean, order_cost, holding_cost, shortage_cost, 
                              max_time, num_runs):
    results = {
        "avg_order_cost": 0,
        "avg_holding_cost": 0,
        "avg_shortage_cost": 0,
        "avg_total_cost": 0
    }
    
    for _ in range(num_runs):
        simulator = InventorySimulator(initial_inventory, order_point, order_quantity, 
                                       demand_mean, lead_time_mean, order_cost, 
                                       holding_cost, shortage_cost, max_time)
        simulator.run()
        
        results["avg_order_cost"] += simulator.total_order_cost
        results["avg_holding_cost"] += simulator.total_holding_cost
        results["avg_shortage_cost"] += simulator.total_shortage_cost
        results["avg_total_cost"] += simulator.get_total_cost()
    
    for key in results:
        results[key] /= num_runs
    
    return results, simulator

# Parámetros de simulación
initial_inventory = 100
order_point = 20
order_quantity = 50
demand_mean = 5
lead_time_mean = 2
order_cost = 100
holding_cost = 1
shortage_cost = 10
max_time = 0.001
num_runs = 10

# Ejecutar experimentos
results, last_simulator = run_inventory_experiments(initial_inventory, order_point, order_quantity, 
                                                    demand_mean, lead_time_mean, order_cost, 
                                                    holding_cost, shortage_cost, max_time, num_runs)

# Imprimir resultados
for key, value in results.items():
    print(f"{key}: {value:.2f}")

# Generar gráfico del último experimento
times, levels = zip(*last_simulator.inventory_history)
plt.figure(figsize=(10, 6))
plt.step(times, levels, where='post')
plt.xlabel('Time')
plt.ylabel('Inventory Level')
plt.title('Inventory Level over Time (Last Run)')
plt.grid(True)
plt.show()