import random
import numpy as np
import matplotlib.pyplot as plt

class InventorySimulation:
    def __init__(self, demand_rate, order_cost, holding_cost, shortage_cost, simulation_time, order_quantity, reorder_point):
        self.demand_rate = demand_rate
        self.order_cost = order_cost
        self.holding_cost = holding_cost
        self.shortage_cost = shortage_cost
        self.simulation_time = simulation_time
        self.order_quantity = order_quantity
        self.reorder_point = reorder_point
        self.reset()

    def reset(self):
        self.time = 0
        self.inventory_level = self.order_quantity  # Start with an initial order
        self.total_order_cost = 0
        self.total_holding_cost = 0
        self.total_shortage_cost = 0
        self.num_orders = 0
        self.total_demand = 0
        self.events = []

    def simulate(self):
        next_demand = random.expovariate(self.demand_rate)
        next_restock = float('inf')

        while self.time < self.simulation_time:
            if next_demand < next_restock:
                self.time = next_demand
                self.handle_demand()
                next_demand = self.time + random.expovariate(self.demand_rate)
                self.events.append((self.time, 'demand'))
            else:
                self.time = next_restock
                self.handle_restock()
                next_restock = float('inf')
                self.events.append((self.time, 'restock'))
            
            if self.inventory_level <= self.reorder_point and next_restock == float('inf'):
                next_restock = self.time + 1  # Assume 1 unit time for restocking

        self.print_results()

    def handle_demand(self):
        self.total_demand += 1
        if self.inventory_level > 0:
            self.inventory_level -= 1
        else:
            self.total_shortage_cost += self.shortage_cost

    def handle_restock(self):
        self.inventory_level += self.order_quantity
        self.total_order_cost += self.order_cost
        self.total_holding_cost += self.holding_cost * self.inventory_level

    def print_results(self):
        total_cost = self.total_order_cost + self.total_holding_cost + self.total_shortage_cost
        print(f"Costo total de órdenes: {self.total_order_cost}")
        print(f"Costo total de mantenimiento: {self.total_holding_cost}")
        print(f"Costo total de faltantes: {self.total_shortage_cost}")
        print(f"Costo total: {total_cost}")

    def get_metrics(self):
        total_cost = self.total_order_cost + self.total_holding_cost + self.total_shortage_cost
        return {
            'total_order_cost': self.total_order_cost,
            'total_holding_cost': self.total_holding_cost,
            'total_shortage_cost': self.total_shortage_cost,
            'total_cost': total_cost
        }

    def plot_results(self):
        times = [event[0] for event in self.events]
        states = [self.inventory_level if event[1] == 'restock' else self.inventory_level-1 for event in self.events]
        plt.plot(times, states)
        plt.xlabel('Time')
        plt.ylabel('Inventory Level')
        plt.title('Inventory Level Over Time')
        plt.show()

# Parámetros iniciales
demand_rate = 0.5  # Tasa de demanda
order_cost = 50  # Costo por orden
holding_cost = 1  # Costo de mantenimiento por unidad de tiempo
shortage_cost = 100  # Costo de faltante por unidad
simulation_time = 100  # Tiempo de simulación
order_quantity = 20  # Cantidad de cada orden
reorder_point = 5  # Punto de reorden

# Ejecutar la simulación
simulation = InventorySimulation(demand_rate, order_cost, holding_cost, shortage_cost, simulation_time, order_quantity, reorder_point)
simulation.simulate()
simulation.plot_results()

# Experimentos
def run_experiments(base_demand_rate, simulation_time, order_quantity, reorder_point):
    demand_rates = [0.5, 1.0, 1.5, 2.0, 2.5]
    results = []

    for rate_factor in demand_rates:
        demand_rate = rate_factor * base_demand_rate
        metrics = []

        for _ in range(10):  
            simulation = InventorySimulation(demand_rate, order_cost, holding_cost, shortage_cost, simulation_time, order_quantity, reorder_point)
            simulation.simulate()
            metrics.append(simulation.get_metrics())

        avg_metrics = {
            'Costo total de órdenes': np.mean([m['total_order_cost'] for m in metrics]),
            'Costo total de mantenimiento': np.mean([m['total_holding_cost'] for m in metrics]),
            'Costo total de faltantes': np.mean([m['total_shortage_cost'] for m in metrics]),
            'Costo total': np.mean([m['total_cost'] for m in metrics])
        }
        results.append((demand_rate, avg_metrics))

    return results

# Ejecutar experimentos
experiment_results = run_experiments(demand_rate, simulation_time, order_quantity, reorder_point)
for demand_rate, metrics in experiment_results:
    print(f"Tasa de demanda: {demand_rate}")
    for metric, value in metrics.items():
        print(f"  {metric}: {value}")
