import random
import numpy as np

class MM1QueueSimulation:
    def __init__(self, arrival_rate, service_rate, simulation_time, queue_capacity=float('inf')):
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
        self.busy_time = 0
        self.num_denied = 0

    def simulate(self):
        next_arrival = random.expovariate(self.arrival_rate)
        next_departure = float('inf')

        while self.time < self.simulation_time:
            if next_arrival < next_departure:
                self.time = next_arrival
                self.handle_arrival()
                next_arrival = self.time + random.expovariate(self.arrival_rate)
            else:
                self.time = next_departure
                self.handle_departure()
                if self.queue:
                    next_departure = self.time + random.expovariate(self.service_rate)
                else:
                    next_departure = float('inf')

        self.print_results()

    def handle_arrival(self):
        if self.num_in_system < self.queue_capacity:
            self.num_in_system += 1
            self.queue.append(self.time)
            if self.num_in_system == 1:
                self.busy_time += random.expovariate(self.service_rate)
        else:
            self.num_denied += 1

    def handle_departure(self):
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
        service_denial_prob = self.num_denied / (self.num_denied + self.num_served) if (self.num_denied + self.num_served) > 0 else 0

        print(f"Total de clientes servidos: {self.num_served}")
        print(f"Tiempo promedio en sistema: {avg_time_in_system}")
        print(f"Tiempo promedio en cola: {avg_time_in_queue}")
        print(f"Utilización del servidor: {utilization}")
        print(f"Probabilidad de denegación de servicio: {service_denial_prob}")


arrival_rate = 3  # λ
service_rate = 17  # μ
simulation_time = 10000  # Tiempo de simulación
queue_capacity = 100  # Capacidad de la cola

simulation = MM1QueueSimulation(arrival_rate, service_rate, simulation_time, queue_capacity)
simulation.simulate()
