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
        self.next_event_time = 0
        self.order_arrival_time = float('inf')
        
        self.total_order_cost = 0
        self.total_holding_cost = 0
        self.total_shortage_cost = 0
        
        self.inventory_history = [(0, initial_inventory)]
    
    def run(self):
        while self.time < self.max_time:
            self.process_next_event()
    
    def process_next_event(self):
        if self.order_arrival_time <= self.next_event_time:
            self.process_order_arrival()
        else:
            self.process_demand()
    
    def process_demand(self):
        self.time = self.next_event_time
        demand = np.random.poisson(self.demand_mean)
        
        if demand <= self.inventory:
            self.inventory -= demand
            self.total_holding_cost += self.holding_cost * self.inventory * (self.next_event_time - self.time)
        else:
            shortage = demand - self.inventory
            self.total_shortage_cost += self.shortage_cost * shortage
            self.inventory = 0
        
        if self.inventory <= self.order_point and self.order_arrival_time == float('inf'):
            self.place_order()
        
        self.next_event_time += np.random.exponential(1/self.demand_mean)
        self.inventory_history.append((self.time, self.inventory))
    
    def process_order_arrival(self):
        self.time = self.order_arrival_time
        self.inventory += self.order_quantity
        self.order_arrival_time = float('inf')
        self.inventory_history.append((self.time, self.inventory))
    
    def place_order(self):
        self.total_order_cost += self.order_cost
        self.order_arrival_time = self.time + np.random.exponential(self.lead_time_mean)
    
    def get_total_cost(self):
        return self.total_order_cost + self.total_holding_cost + self.total_shortage_cost
    
    def plot_inventory_level(self):
        times, levels = zip(*self.inventory_history)
        plt.figure(figsize=(10, 6))
        plt.step(times, levels, where='post')
        plt.xlabel('Time')
        plt.ylabel('Inventory Level')
        plt.title('Inventory Level over Time')
        plt.grid(True)
        plt.show()

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
    
    return results

# Parámetros de simulación
initial_inventory = 100  # Inventario inicial
order_point = 20  # Punto de reorden
order_quantity = 50  # Cantidad de orden
demand_mean = 5  # Demanda media diaria
lead_time_mean = 2  # Tiempo medio de entrega (en días)
order_cost = 100  # Costo por orden
holding_cost = 1  # Costo de mantener una unidad por día
shortage_cost = 10  # Costo de escasez por unidad por día
max_time = 365  # Tiempo total de simulación (un año)
num_runs = 10  # Número de corridas por experimento

# Justificación:
# - initial_inventory = 100: Comenzamos con un inventario que puede cubrir aproximadamente 20 días de demanda media.
# - order_point = 20: Reordenamos cuando el inventario puede cubrir 4 días de demanda media, considerando el tiempo de entrega.
# - order_quantity = 50: Pedimos para cubrir aproximadamente 10 días de demanda media.
# - demand_mean = 5: Asumimos una demanda diaria promedio de 5 unidades.
# - lead_time_mean = 2: Asumimos un tiempo de entrega promedio de 2 días.
# - order_cost = 100: Costo fijo por realizar un pedido.
# - holding_cost = 1: Costo diario por mantener una unidad en inventario.
# - shortage_cost = 10: Penalización por unidad faltante por día, 10 veces más que el costo de mantenimiento.
# - max_time = 365: Simulamos un año completo para capturar variaciones estacionales.
# - num_runs = 10: Cumple con el requisito mínimo de corridas y proporciona un buen balance entre precisión y tiempo de cálculo.

# Ejecutar experimentos
results = run_inventory_experiments(initial_inventory, order_point, order_quantity, 
                                    demand_mean, lead_time_mean, order_cost, 
                                    holding_cost, shortage_cost, max_time, num_runs)

# Imprimir resultados
for key, value in results.items():
    print(f"{key}: {value:.2f}")

# Ejemplo de gráfico para una simulación específica
simulator = InventorySimulator(initial_inventory, order_point, order_quantity, 
                               demand_mean, lead_time_mean, order_cost, 
                               holding_cost, shortage_cost, max_time)
simulator.run()
simulator.plot_inventory_level()