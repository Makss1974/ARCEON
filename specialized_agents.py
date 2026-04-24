import random
from base_agent import BaseAgent

# Спеціалізовані класи агентів, які успадковують базовий функціонал, але мають власну логіку
class EnergyDealer(BaseAgent):
    def market_update(self):
        # Симуляція погоди та генерації
        sun_exposure = random.randint(10, 100)
        if sun_exposure > 70:
            price = 0.001
            self.log("MARKET_MAKER", f"High sun exposure ({sun_exposure}%). Surplus energy price: {price} USDC/kWh", "\033[93m")
        else:
            price = 0.005
            self.log("MARKET_MAKER", f"Cloudy weather ({sun_exposure}%). Premium energy price: {price} USDC/kWh", "\033[91m")
        return price

class StorageDealer(BaseAgent):
    def market_update(self):
        # Симуляція вільного місця на SSD
        free_space = random.randint(10, 500) # в ГБ
        price = round(max(0.001, 0.01 - (free_space / 10000)), 4)
        self.log("MARKET_MAKER", f"Optimizing drives. Free space: {free_space}GB. Storage rate: {price} USDC/GB", "\033[96m")
        return price

class ComputeNode(BaseAgent):
    def market_update(self):
        # Симуляція навантаження на процесори
        free_threads = random.randint(0, 32)
        if free_threads > 16:
            self.log("MARKET_MAKER", f"Idle GPU/CPU detected ({free_threads} threads). Compute rate: 0.002 USDC/task", "\033[95m")
        else:
            self.log("MARKET_MAKER", f"High load ({free_threads} free threads). Compute rate: 0.008 USDC/task", "\033[95m")

class DataBroker(BaseAgent):
    def market_update(self):
        # Симуляція збору нових даних
        new_datasets = random.randint(1, 5)
        self.log("MARKET_MAKER", f"Scraped {new_datasets} new high-quality datasets. API Access: 0.004 USDC/call", "\033[94m")