import random
import numpy as np

class MM1QueueSimulation:
    def __init__(self, arrival_rate, service_rate, simulation_time):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.simulation_time = simulation_time
        self.time = 0
        self.queue = []
        self.num_in_system = 0
        self.num_served = 0
        self.total_time_in_system = 0

    def simulate(self):
        next_arrival = random.expovariate(self.arrival_rate)
        next_departure = float('inf')  # Sin fecha de salida inicialmente

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
        self.num_in_system += 1
        self.queue.append(self.time)
        if self.num_in_system == 1:  # Si el sistema esta vacio, programar una salida
            next_departure = self.time + random.expovariate(self.service_rate)

    def handle_departure(self):
        arrival_time = self.queue.pop(0)
        self.num_in_system -= 1
        self.num_served += 1
        self.total_time_in_system += self.time - arrival_time

    def print_results(self):
        print(f"Total de clientes servidos: {self.num_served}")
        print(f"Tiempo promedio en sistema: {self.total_time_in_system / self.num_served if self.num_served > 0 else 0}")

# Example usage
arrival_rate = 5  # λ
service_rate = 8  # μ
simulation_time = 100  # Simulation time in arbitrary time units

simulation = MM1QueueSimulation(arrival_rate, service_rate, simulation_time)
simulation.simulate()
