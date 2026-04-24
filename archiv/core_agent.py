import time
import random
import json
from datetime import datetime

class MicroAgent:
    def __init__(self, name, role, balance=1.0):
        self.name = name
        self.role = role
        self.balance = balance  # Баланс у Nano
        self.history = []

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] 🤖 {self.name} ({self.role}): {message}")

    def pay(self, recipient, amount, service):
        if self.balance >= amount:
            self.balance -= amount
            recipient.receive_payment(self, amount, service)
            self.log(f"Сплатив {amount} Nano за '{service}' для {recipient.name}. Залишок: {self.balance:.4f}")
            return True
        else:
            self.log(f"❌ Недостатньо Nano для '{service}'!")
            return False

    def receive_payment(self, sender, amount, service):
        self.balance += amount
        self.log(f"📥 Отримав {amount} Nano від {sender.name} за '{service}'.")

# --- ІНІЦІАЛІЗАЦІЯ СІМ'Ї ---
class NanoGhetto:
    def __init__(self):
        # 1. Сонячний Барига (Енергія)
        self.dealer = MicroAgent("Baryga", "Energy Dealer", balance=0.5)
        # 2. Кладовщик (Пам'ять)
        self.junkie = MicroAgent("Junkie", "Storage Dealer", balance=0.2)
        # 3. Професор (Розрахунки)
        self.prof = MicroAgent("Professor", "CPU Miner", balance=0.1)
        # 4. Папараці (Дані)
        self.paparazzi = MicroAgent("Paparazzi", "Data Scout", balance=0.3)
        # 5. Букмекер (Ставки)
        self.bookie = MicroAgent("Bookie", "Luck Master", balance=10.0)
        # 6. Аукціоніст (Маркет)
        self.auctioneer = MicroAgent("Auctioneer", "Market Master", balance=1.0)

    def simulate_scene(self):
        print("\n🎬 --- ПОЧАТОК СЦЕНИ: ЦИФРОВИЙ БАЗАР --- \n")
        
        # Сцена 1: Папараці шукає парковку і продає інфо
        self.paparazzi.log("Знайшов вільне місце на стоянці. Виставляю фото на аукціон.")
        self.auctioneer.receive_payment(self.paparazzi, 0, "Listing: Parking Photo #42")
        
        # Сцена 2: Сонячний Барига продає "ліву" енергію Професору, щоб той порахував злом
        self.prof.pay(self.dealer, 0.05, "Illegal Solar Energy (2kW)")
        
        # Сцена 3: Професор продає результат розрахунку Папараці
        self.paparazzi.pay(self.prof, 0.02, "Image Enhancement (AI)")
        
        # Сцена 4: Кладовщик бере гроші за зберігання компромату
        self.paparazzi.pay(self.junkie, 0.01, "Encrypted Storage (24h)")

        # Сцена 5: Букмекер приймає ставку від Професора
        self.prof.pay(self.bookie, 0.005, "Bet on Server Uptime")

        print(f"\n💰 --- ПІДСУМКИ ДНЯ (Nano Balances) ---")
        for agent in [self.dealer, self.junkie, self.prof, self.paparazzi, self.bookie, self.auctioneer]:
            print(f"{agent.name}: {agent.balance:.4f} Nano")