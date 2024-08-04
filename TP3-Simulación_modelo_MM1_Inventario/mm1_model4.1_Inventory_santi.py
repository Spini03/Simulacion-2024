import numpy as np
import matplotlib.pyplot as plt

class InventorySimulator:
    def __init__(self, initial_inventory, order_point, max_stock, demand_mean, 
                 lead_time_mean, order_cost, holding_cost, shortage_cost, max_time, alpha, recargoIncremental, order_time=float('inf')):
        self.inventory = initial_inventory
        self.order_point = order_point
        self.max_stock = max_stock 
        self.demand_mean = demand_mean
        self.lead_time_mean = lead_time_mean
        self.order_cost = order_cost
        self.holding_cost = holding_cost
        self.shortage_cost = shortage_cost
        self.max_time = max_time
        self.alpha = alpha
        self.recargoIncremental = recargoIncremental
        self.order_time = order_time

        self.time = 0
        self.last_event_time = 0
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
        # Prioridad a la llegada del pedido
        if self.order_arrival_time <= self.next_event_time:
            self.process_order_arrival() 
        # En caso de que no haya pedido pendiente, la prioridad es la demanda
        elif self.next_event_time < float('inf'):  # Asegurar que haya un próximo evento
            self.process_demand()

    def process_demand(self):
        time_diff = self.next_event_time - self.last_event_time
        self.total_holding_cost += self.holding_cost * max(self.inventory, 0) * time_diff
        self.total_shortage_cost += self.shortage_cost * max(-self.inventory, 0) * time_diff

        self.last_event_time = self.next_event_time
        self.time = self.next_event_time

        # demand = int(np.random.choice([1, 2, 3, 4], p=[0.16, 0.34, 0.34, 0.16]))
        demand = np.random.lognormal(-self.alpha, 1) 
        demand = int(round(demand))  

        if demand <= self.inventory:
            self.inventory -= demand
        else:
            shortage = demand - self.inventory
            self.total_shortage_cost += self.shortage_cost * shortage
            self.inventory = 0

        if self.inventory <= self.order_point and self.order_arrival_time == float('inf'):
            self.place_order()

        # Programando el siguiente evento de demanda
        self.next_event_time += np.random.exponential(1 / self.demand_mean)
        self.inventory_history.append((self.time, self.inventory))

    def process_order_arrival(self):
        time_diff = self.order_arrival_time - self.last_event_time 
        self.total_holding_cost += self.holding_cost * max(self.inventory, 0) * time_diff
        self.total_shortage_cost += self.shortage_cost * max(-self.inventory, 0) * time_diff

        self.last_event_time = self.order_arrival_time
        self.time = self.order_arrival_time
        self.inventory += self.order_quantity

        self.total_order_cost += self.order_cost + (self.recargoIncremental * self.order_quantity)

        self.order_arrival_time = float('inf')
        self.order_time = float('inf')
        self.inventory_history.append((self.time, self.inventory))

    def place_order(self):
        self.order_quantity = self.max_stock - self.inventory
        self.total_order_cost += (self.recargoIncremental * self.order_quantity)
        self.order_arrival_time = self.time + np.random.exponential(self.lead_time_mean)

    def get_total_cost(self):
        return self.total_order_cost + self.total_holding_cost + self.total_shortage_cost

    def plot_inventory_level(self):
        times, levels = zip(*self.inventory_history)
        plt.figure(figsize=(10, 6))
        plt.step(times, levels, where='post', label='Inventory Level')
        plt.axhline(y=0, color='r', linestyle='--', label='Zero Inventory')
        plt.xlabel('Time')
        plt.ylabel('Inventory Level')
        plt.title('Inventory Level over Time')
        plt.legend()
        plt.grid(True)
        plt.show()

def run_inventory_experiments(initial_inventory, order_point, max_stock, demand_mean, 
                              lead_time_mean, order_cost, holding_cost, shortage_cost, 
                              max_time, num_runs, alpha, recargoIncremental):
    results = {
        "avg_order_cost": 0,
        "avg_holding_cost": 0,
        "avg_shortage_cost": 0,
        "avg_total_cost": 0
    }

    for _ in range(num_runs):
        simulator = InventorySimulator(initial_inventory, order_point, max_stock, 
                                       demand_mean, lead_time_mean, order_cost, 
                                       holding_cost, shortage_cost, max_time, alpha, recargoIncremental)
        simulator.run()

        results["avg_order_cost"] += simulator.total_order_cost
        results["avg_holding_cost"] += simulator.total_holding_cost
        results["avg_shortage_cost"] += simulator.total_shortage_cost
        results["avg_total_cost"] += simulator.get_total_cost()

    for key in results:
        results[key] /= num_runs

    return results

# Parámetros de simulación
initial_inventory = 100 # Inventario inicial
order_point = 20 # Punto de reorden
max_stock = 150 # Capacidad máxima del inventario
# order_quantity = 50 # Cantidad de orden
demand_mean = 10 # Demanda media diaria
lead_time_mean = 2 # Tiempo medio de entrega (en días)
order_cost = 100 # Costo por orden (recargoOrden en AnyLogic)
holding_cost = 1 # Costo de mantener una unidad por día (recargoMantenimiento en AnyLogic)
shortage_cost = 10 # Costo de escasez por unidad por día (recargoFaltante en AnyLogic)
max_time = 365 # Tiempo total de simulación (un año)
num_runs = 10 # Número de corridas por experimento
recargoIncremental = 3 # Costo variable por cantidad pedida (recargoIncremental en AnyLogic)
alpha = 0.1 # Parámetro de la distribución de demanda en AnyLogic
max_stock = 150 # Capacidad máxima del inventario

# Ejecutar experimentos
results = run_inventory_experiments(initial_inventory, order_point, max_stock, 
                                    demand_mean, lead_time_mean, order_cost, 
                                    holding_cost, shortage_cost, max_time, num_runs, alpha, recargoIncremental)

# Imprimir resultados
for key, value in results.items():
    print(f"{key}: {value:.2f}")

# Ejemplo de gráfico para una simulación específica
simulator = InventorySimulator(initial_inventory, order_point, max_stock, 
                               demand_mean, lead_time_mean, order_cost, 
                               holding_cost, shortage_cost, max_time, alpha, recargoIncremental)
simulator.run()
simulator.plot_inventory_level()