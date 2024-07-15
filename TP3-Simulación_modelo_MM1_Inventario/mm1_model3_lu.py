import random
import numpy as np
import matplotlib.pyplot as plt

class MM1QueueSimulation:
    def __init__(self, arrival_rate, service_rate, simulation_time, queue_capacity=None):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.simulation_time = simulation_time
        self.queue_capacity = queue_capacity
        self.reset()

    def reset(self):
        self.time = 0
        self.queue = []
        self.num_in_system = 0
        self.num_served = 0
        self.total_time_in_system = 0
        self.total_time_in_queue = 0
        self.num_arrivals = 0
        self.service_denials = 0
        self.busy_time = 0

    def simulate(self):
        next_arrival = random.expovariate(self.arrival_rate)
        next_departure = float('inf')
        events = []

        while self.time < self.simulation_time:
            if next_arrival < next_departure:
                self.time = next_arrival
                self.handle_arrival()
                next_arrival = self.time + random.expovariate(self.arrival_rate)
                events.append((self.time, 'arrival'))
            else:
                self.time = next_departure
                self.handle_departure()
                if self.queue:
                    next_departure = self.time + random.expovariate(self.service_rate)
                else:
                    next_departure = float('inf')
                events.append((self.time, 'departure'))

        self.print_results()
        return events

    def handle_arrival(self):
        if self.queue_capacity is None or self.num_in_system < self.queue_capacity:
            self.num_in_system += 1
            self.queue.append(self.time)
            self.num_arrivals += 1
            if self.num_in_system == 1:
                self.busy_time += random.expovariate(self.service_rate)
        else:
            self.service_denials += 1

    def handle_departure(self):
        if self.queue:
            arrival_time = self.queue.pop(0)
            self.num_in_system -= 1
            self.num_served += 1
            time_in_system = self.time - arrival_time
            self.total_time_in_system += time_in_system
            self.total_time_in_queue += (time_in_system - (1 / self.service_rate))

    def print_results(self):
        avg_num_in_system = self.total_time_in_system / self.simulation_time
        avg_num_in_queue = self.total_time_in_queue / self.simulation_time
        avg_time_in_system = self.total_time_in_system / self.num_served if self.num_served > 0 else 0
        avg_time_in_queue = self.total_time_in_queue / self.num_served if self.num_served > 0 else 0
        utilization = self.busy_time / self.simulation_time
        service_denial_prob = self.service_denials / self.num_arrivals if self.num_arrivals > 0 else 0

        print(f"Promedio de clientes en sistema (L): {avg_num_in_system}")
        print(f"Promedio de clientes en cola (Lq): {avg_num_in_queue}")
        print(f"Tiempo promedio en sistema (W): {avg_time_in_system}")
        print(f"Tiempo promedio en cola (Wq): {avg_time_in_queue}")
        print(f"Utilización del servidor (ρ): {utilization}")
        print(f"Probabilidad de denegación de servicio: {service_denial_prob}")

    def get_metrics(self):
        avg_num_in_system = self.total_time_in_system / self.simulation_time
        avg_num_in_queue = self.total_time_in_queue / self.simulation_time
        avg_time_in_system = self.total_time_in_system / self.num_served if self.num_served > 0 else 0
        avg_time_in_queue = self.total_time_in_queue / self.num_served if self.num_served > 0 else 0
        utilization = self.busy_time / self.simulation_time
        service_denial_prob = self.service_denials / self.num_arrivals if self.num_arrivals > 0 else 0

        return {
            'avg_num_in_system': avg_num_in_system,
            'avg_num_in_queue': avg_num_in_queue,
            'avg_time_in_system': avg_time_in_system,
            'avg_time_in_queue': avg_time_in_queue,
            'utilization': utilization,
            'service_denial_prob': service_denial_prob
        }

    def plot_results(self, events):
        times = [event[0] for event in events]
        states = [event[1] for event in events]
        num_in_system = [0]

        for event in states:
            if event == 'arrival':
                num_in_system.append(num_in_system[-1] + 1)
            elif event == 'departure':
                num_in_system.append(num_in_system[-1] - 1)

        plt.plot(times, num_in_system[1:])
        plt.xlabel('Time')
        plt.ylabel('Number in System')
        plt.title('Number of Customers in System Over Time')
        plt.show()

arrival_rate = 3  # λ
service_rate = 17  # μ
simulation_time = 1000  # Tiempo de simulación en unidades arbitrarias
queue_capacity = 10  # Capacidad de la cola para cola finita

simulation = MM1QueueSimulation(arrival_rate, service_rate, simulation_time, queue_capacity)
events = simulation.simulate()
simulation.plot_results(events)

def run_experiments(base_service_rate, simulation_time, queue_capacity=None):
    arrival_rates = [0.25, 0.5, 0.75, 1.0, 1.25]
    results = []

    for rate_factor in arrival_rates:
        arrival_rate = rate_factor * base_service_rate
        metrics = []

        for _ in range(10):  
            simulation = MM1QueueSimulation(arrival_rate, base_service_rate, simulation_time, queue_capacity)
            events = simulation.simulate()
            metrics.append(simulation.get_metrics())

        avg_metrics = {
            'Promedio de clientes en sistema': np.mean([m['avg_num_in_system'] for m in metrics]),
            'Promedio de clientes en cola': np.mean([m['avg_num_in_queue'] for m in metrics]),
            'Tiempo promedio en sistema:': np.mean([m['avg_time_in_system'] for m in metrics]),
            'Tiempo promedio en cola:': np.mean([m['avg_time_in_queue'] for m in metrics]),
            'Utilización del servidor:': np.mean([m['utilization'] for m in metrics]),
            'Probabilidad de denegación de servicio:': np.mean([m['service_denial_prob'] for m in metrics])
        }
        results.append((arrival_rate, avg_metrics))

    return results

base_service_rate = 5
simulation_time = 1000
queue_capacity = 10

experiment_results = run_experiments(base_service_rate, simulation_time, queue_capacity)
for arrival_rate, metrics in experiment_results:
    print(f"Tiempo de llegada: {arrival_rate}")
    for metric, value in metrics.items():
        print(f"  {metric}: {value}")
