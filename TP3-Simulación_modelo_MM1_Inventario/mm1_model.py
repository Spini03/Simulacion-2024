class MM1Queue:
    def __init__(self, arrival_rate, service_rate):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.utilization = self.arrival_rate / self.service_rate

    def average_number_in_system(self):
        return self.utilization / (1 - self.utilization)

    def average_number_in_queue(self):
        return (self.utilization ** 2) / (1 - self.utilization)

    def average_time_in_system(self):
        return 1 / (self.service_rate - self.arrival_rate)

    def average_time_in_queue(self):
        return self.utilization / (self.service_rate - self.arrival_rate)

# Example usage
arrival_rate = 5  # λ
service_rate = 8  # μ

queue = MM1Queue(arrival_rate, service_rate)

print("Utilizacion (ρ):", queue.utilization)
print("Numero promedio de clientes en sistema (L):", queue.average_number_in_system())
print("Numero promedio de clientes en cola (Lq):", queue.average_number_in_queue())
print("Timpo promedio de clientes en el sistema (W):", queue.average_time_in_system())
print("Tiempo promedio de clientes en cola (Wq):", queue.average_time_in_queue())

