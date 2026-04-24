import time
import random
from datetime import datetime
from arc_bridge import ArcBridge

# Кольори для вайбу
GREEN, YELLOW, RED, BLUE, RESET = "\033[92m", "\033[93m", "\033[91m", "\033[94m", "\033[0m"

class SovereignManager:
    def __init__(self, node_id, bridge, wallet_id):
        self.node_id = node_id
        self.bridge = bridge
        self.wallet_id = wallet_id
        self.balance = 1.0  # Початковий баланс для логів
        self.uptime = 0

    def log(self, category, msg, color=RESET):
        t = datetime.now().strftime("%H:%M:%S")
        print(f"[{t}] {color}🤖 {self.node_id} | {category} | {msg}{RESET}")

    def run_cycle(self):
        self.uptime += 1
        print(f"\n--- [ ЦИКЛ АВТОНОМНОСТІ №{self.uptime} ] ---")
        
        # Стан системи
        energy = random.randint(5, 100)
        
        if energy < 20:
            self.log("CRISIS", "Енергія 15%. Господар спить. Треба купувати 'лівий' кіловат.", RED)
            # РЕАЛЬНА ДІЯ: Виклик блокчейн-транзакції
            tx = self.bridge.transfer_usdc(self.wallet_id, "0x_Baryga_Address", 0.001)
            
            if tx["status"] == "SUCCESS":
                self.log("PAYMENT", f"Транзакція Arc підтверджена! Hash: {tx['txHash'][:15]}...", GREEN)
                self.log("SURVIVAL", "Енергію отримано. Система стабільна.", BLUE)
            else:
                self.log("ERROR", "Платіж не пройшов. Загроза відключення!", RED)
        
        elif energy > 80:
            self.log("SURPLUS", "Акумулятори повні. Виставляю надлишок на продаж.", YELLOW)
            # Тут логіка отримання платежу (в реальності чекаємо webhook від Circle)
            self.log("TRADE", "Продано 200Wh. Отримано 0.002 USDC.", GREEN)
        
        else:
            self.log("STABLE", "Ресурсів достатньо. Проводжу внутрішній аудит /home/ubuntu/.", RESET)

# --- ЗАПУСК КОМАНДОЮ ---
if __name__ == "__main__":
    # Ці дані має принести Сергій Потужний
    MY_API_KEY = "TEST_KEY_FROM_CIRCLE"
    MY_ENTITY_SECRET = "TEST_SECRET"
    MY_WALLET = "WALLET_ID_1"

    bridge = ArcBridge(MY_API_KEY, MY_ENTITY_SECRET)
    sain = SovereignManager("MAITS-CORE-S1", bridge, MY_WALLET)

    print(f"{BLUE}Маніфест: Я купую свій ресурс — отже, я існую.{RESET}")
    
    try:
        while True:
            sain.run_cycle()
            time.sleep(5) # Швидкість для хакатону
    except KeyboardInterrupt:
        print(f"\n{YELLOW}⚠️ Вузол SAIN переходить у режим збереження.{RESET}")