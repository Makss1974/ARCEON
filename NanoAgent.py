import time
import json
import uuid
from datetime import datetime

class NanoAgent:
    def __init__(self, agent_id, role, balance=5.0):
        self.agent_id = agent_id
        self.role = role
        self.balance = balance
        self.wallet_address = f"nano_{uuid.uuid4().hex[:40]}" # Віртуальна адреса
        self.is_autonomous = True

    def log(self, action, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        # Творчий формат логу для XAI
        print(f"[{timestamp}] 🤖 {self.agent_id} | {self.role.upper()} | {action}: {message}")

    def request_service(self, target_agent, service_name, price):
        self.log("REQUEST", f"Запит на '{service_name}' до {target_agent.agent_id} за {price} Nano.")
        
        if self.balance >= price:
            # Симуляція миттєвої Nano-транзакції без комісії
            self.balance -= price
            success = target_agent.provide_service(self, service_name, price)
            
            if success:
                self.log("SUCCESS", f"Послуга '{service_name}' отримана. Мій залишок: {self.balance:.4f} Nano.")
                return True
        else:
            self.log("REJECT", "Недостатньо ресурсу (Nano) для автономної дії.")
            return False

    def provide_service(self, requester, service_name, price):
        # Логіка надання послуги
        self.balance += price
        self.log("SERVICE", f"Надаю '{service_name}' для {requester.agent_id}. Баланс поповнено: {self.balance:.4f} Nano.")
        return True

# --- ТЕСТОВИЙ ЗАПУСК (ПРИЗЕМЛЕНИЙ КЕЙС) ---
if __name__ == "__main__":
    # Проект №1: Прагматичний обмін ресурсами
    server_node = NanoAgent("Server_DELL_R710", "Compute Provider", balance=1.0)
    iot_sensor = NanoAgent("Weather_Sensor_X1", "Data Scout", balance=0.5)

    print("--- ТЕСТУВАННЯ ТЕХНОЛОГІЧНОГО ПРОЕКТУ №1 ---")
    iot_sensor.request_service(server_node, "Data Analysis (100MB)", 0.05)