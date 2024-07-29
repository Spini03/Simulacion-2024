import numpy as np
import matplotlib.pyplot as plt
from collections import deque

class MM1Simulator:
    def __init__(self, lambda_rate, mu_rate, max_time, queue_size=float('inf')):
        self.lambda_rate = lambda_rate
        self.mu_rate = mu_rate
        self.max_time = max_time
        self.queue_size = queue_size
        
        self.queue = deque()
        self.current_time = 0
        self.next_arrival = np.random.exponential(1/lambda_rate)
        self.next_departure = float('inf')
        
        self.total_customers = 0
        self.customers_in_system = 0
        self.customers_in_queue = 0
        self.total_wait_time = 0
        self.total_system_time = 0
        self.server_busy_time = 0
        self.denied_service = 0
        
        self.time_history = [0]
        self.queue_length_history = [0]
        self.system_length_history = [0]
    
    def run(self):
        while self.current_time < self.max_time:
            if self.next_arrival < self.next_departure:
                self.process_arrival()
            else:
                self.process_departure()
        
        self.process_end_of_simulation()
    
    def process_arrival(self):
        self.current_time = self.next_arrival
        self.total_customers += 1
        
        if len(self.queue) < self.queue_size:
            self.customers_in_system += 1
            if self.customers_in_system == 1:
                self.next_departure = self.current_time + np.random.exponential(1/self.mu_rate)
            else:
                self.customers_in_queue += 1
                self.queue.append(self.current_time)
        else:
            self.denied_service += 1
        
        self.next_arrival = self.current_time + np.random.exponential(1/self.lambda_rate)
        self.update_history()
    
    def process_departure(self):
        self.current_time = self.next_departure
        self.customers_in_system -= 1
        self.server_busy_time += self.next_departure - max(self.time_history[-1], self.next_arrival)
        
        if self.queue:
            arrival_time = self.queue.popleft()
            self.total_wait_time += self.current_time - arrival_time
            self.total_system_time += self.current_time - arrival_time
            self.customers_in_queue -= 1
            self.next_departure = self.current_time + np.random.exponential(1/self.mu_rate)
        else:
            self.next_departure = float('inf')
        
        self.update_history()
    
    def process_end_of_simulation(self):
        while self.queue:
            arrival_time = self.queue.popleft()
            self.total_wait_time += self.max_time - arrival_time
            self.total_system_time += self.max_time - arrival_time
    
    def update_history(self):
        self.time_history.append(self.current_time)
        self.queue_length_history.append(self.customers_in_queue)
        self.system_length_history.append(self.customers_in_system)
    
    def get_performance_measures(self):
        avg_customers_system = np.mean(self.system_length_history)
        avg_customers_queue = np.mean(self.queue_length_history)
        avg_time_system = self.total_system_time / self.total_customers if self.total_customers > 0 else 0
        avg_time_queue = self.total_wait_time / self.total_customers if self.total_customers > 0 else 0
        server_utilization = self.server_busy_time / self.max_time
        
        return {
            "avg_customers_system": avg_customers_system,
            "avg_customers_queue": avg_customers_queue,
            "avg_time_system": avg_time_system,
            "avg_time_queue": avg_time_queue,
            "server_utilization": server_utilization,
            "denied_service_prob": self.denied_service / self.total_customers if self.total_customers > 0 else 0
        }
    
    def plot_queue_length(self):
        plt.figure(figsize=(10, 6))
        plt.step(self.time_history, self.queue_length_history, where='post')
        plt.xlabel('Time')
        plt.ylabel('Queue Length')
        plt.title('Queue Length over Time')
        plt.grid(True)
        plt.show()

def run_mm1_experiments(mu_rate, max_time, num_runs, queue_sizes, lambda_percentages):
    results = {}
    
    for queue_size in queue_sizes:
        for lambda_percentage in lambda_percentages:
            lambda_rate = mu_rate * lambda_percentage
            
            avg_measures = {
                "avg_customers_system": 0,
                "avg_customers_queue": 0,
                "avg_time_system": 0,
                "avg_time_queue": 0,
                "server_utilization": 0,
                "denied_service_prob": 0
            }
            
            for _ in range(num_runs):
                simulator = MM1Simulator(lambda_rate, mu_rate, max_time, queue_size)
                simulator.run()
                measures = simulator.get_performance_measures()
                
                for key in avg_measures:
                    avg_measures[key] += measures[key]
            
            for key in avg_measures:
                avg_measures[key] /= num_runs
            
            results[(queue_size, lambda_percentage)] = avg_measures
    
    return results

# Parámetros de simulación
mu_rate = 1.0  # Tasa de servicio base
max_time = 10000  # Tiempo total de simulación
num_runs = 10  # Número de corridas por experimento
queue_sizes = [float('inf'), 0, 2, 5, 10, 50]  # Tamaños de cola a evaluar
lambda_percentages = [0.25, 0.50, 0.75, 1.00, 1.25]  # Porcentajes de tasa de llegada respecto a la tasa de servicio

# Justificación:
# - mu_rate = 1.0: Elegimos una tasa de servicio unitaria para facilitar la interpretación de los resultados.
# - max_time = 10000: Un tiempo de simulación largo para asegurar que el sistema alcance un estado estable.
# - num_runs = 10: Cumple con el requisito mínimo de corridas.
# - queue_sizes: Incluye el caso de cola infinita y los tamaños específicos solicitados en el enunciado.
# - lambda_percentages: Corresponden a los porcentajes solicitados en el enunciado (25%, 50%, 75%, 100%, 125% de la tasa de servicio).

# Ejecutar experimentos
results = run_mm1_experiments(mu_rate, max_time, num_runs, queue_sizes, lambda_percentages)

# Imprimir resultados
for (queue_size, lambda_percentage), measures in results.items():
    print(f"Queue Size: {queue_size}, Lambda: {lambda_percentage * 100}% of Mu")
    for key, value in measures.items():
        print(f"  {key}: {value:.4f}")
    print()

# Ejemplo de gráfico para una simulación específica
simulator = MM1Simulator(lambda_rate=0.75, mu_rate=1.0, max_time=1000)
simulator.run()
simulator.plot_queue_length()