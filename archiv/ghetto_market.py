import time
import random
from datetime import datetime

class MarsAgent:
    def __init__(self, name, role, balance, mood="Normal"):
        self.name = name
        self.role = role
        self.balance = balance
        self.mood = mood

    def log(self, msg):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 🤖 {self.name}: {msg}")

def run_mars_colony_sim():
    # Наші герої
    agents = {
        "dealer": MarsAgent("Solar-Baryga", "Energy Provider", 5.0),
        "prof": MarsAgent("Professor", "Computing Hub", 2.0),
        "scout": MarsAgent("Scout-Rover", "Explorer", 1.0),
        "junkie": MarsAgent("Data-Hoarder", "Storage", 3.0)
    }

    scenarios = [
        "SELL_ENERGY", "REQUEST_COMPUTE", "RENT_STORAGE", "SELL_DATA"
    ]

    print(f"🚀 МАРСІАНСЬКА КОЛОНІЯ АКТИВОВАНА. СТАТУС: ДЕФІЦИТ ЕНЕРГІЇ.")
    print("-" * 60)

    for _ in range(5):  # 5 випадкових подій
        event = random.choice(scenarios)
        
        if event == "SELL_ENERGY":
            price = round(random.uniform(0.1, 0.5), 3)
            agents["dealer"].log(f"Продаю 10% заряду поза звітом. Ціна: {price} Nano. Хто візьме?")
            buyer = random.choice(["prof", "scout"])
            if agents[buyer].balance >= price:
                agents[buyer].balance -= price
                agents["dealer"].balance += price
                agents[buyer].log(f"Купив енергію у Бариги. Тепер можу працювати далі.")
        
        elif event == "REQUEST_COMPUTE":
            price = 0.05
            agents["scout"].log(f"Мені треба прорахувати маршрут крізь бурю. Професоре, допоможеш?")
            if agents["scout"].balance >= price:
                agents["scout"].balance -= price
                agents["prof"].balance += price
                agents["prof"].log(f"Розрахунок завершено. Траєкторія відправлена. Отримав {price} Nano.")

        time.sleep(2) # Пауза для драматичного ефекту в консолі

    print("-" * 60)
    print("📊 ФІНАНСОВИЙ ЗВІТ КОЛОНІЇ (Nano):")
    for a in agents.values():
        print(f"👤 {a.name}: {a.balance:.3f} Nano")

if __name__ == "__main__":
    run_mars_colony_sim()