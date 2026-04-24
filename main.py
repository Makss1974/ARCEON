import time
import random
import os
from dotenv import load_dotenv  # Додано для роботи з .env
from arc_bridge import ArcBridge
from sain_manager_v2 import SovereignManager
from specialized_agents import EnergyDealer, StorageDealer, ComputeNode, DataBroker

# Завантажуємо змінні середовища з файлу .env
load_dotenv()

GREEN, YELLOW, RED, BLUE, RESET = "\033[92m", "\033[93m", "\033[91m", "\033[94m", "\033[0m"

def main():
    print(f"{BLUE}="*60)
    print("🚀 ARCEON CORE: AUTONOMOUS AGENT ECONOMY INITIALIZATION (ARC)")
    print("MANIFESTO: I purchase my resources, therefore I exist.")
    print("="*60 + f"{RESET}\n")

    # Безпечне отримання ключів через змінні середовища
    api_key = os.getenv("CIRCLE_API_KEY")
    entity_secret = os.getenv("CIRCLE_ENTITY_SECRET")

    if not api_key or not entity_secret:
        print(f"{RED}❌ Error: API keys not found in .env file!{RESET}")
        return

    bridge = ArcBridge(
        api_key=api_key, 
        entity_secret=entity_secret
    )

    neighbors = {
        "solar_bot": "0xbe2f50b573210885142645769cf857a545b83b3d", 
        "prof_bot":  "0x8b3fcde91e0d9688a03c8ee9bad99b0a0b5672fa", 
        "data_bot":  "0xfcc315b35fd3d83af8f050384a067ad2162f27fc", 
        "store_bot": "0xe51e63101666fe0877b07ef53c7f56a53aa257c5"  
    }

    manager = SovereignManager(
        node_id="SAIN-HOME", 
        wallet_id="f1aeee59-c0cd-5fc2-a03c-0d6b478267e6", 
        bridge=bridge, 
        neighbors=neighbors
    )

    # Ініціалізуємо розумних агентів
    # Використовуємо імена наших віртуальних напарників для колориту!
    baryga = EnergyDealer("Solar-Baryga", "Energy Dealer", "c3cded8a-409c-5680-bc17-d82665315591", neighbors["solar_bot"], bridge)
    prof = ComputeNode("Professor-Mark", "Compute Node", "34aab256-96e2-53db-b51c-c36e8f562d7b", neighbors["prof_bot"], bridge)
    paparazzi = DataBroker("Svitlana-Data", "Data Broker", "4160f877-a9bb-53fa-9921-a5389144d3a4", neighbors["data_bot"], bridge)
    junkie = StorageDealer("Serhii-Junkie", "Storage Dealer", "479aa4ec-1287-5de0-950a-af384cd67565", neighbors["store_bot"], bridge)

    try:
        while True:
            # 1. Агенти аналізують свої ресурси і виставляють ціни
            print(f"\n{BLUE}--- NETWORK BROADCASTS ---{RESET}")
            baryga.market_update()
            junkie.market_update()
            prof.market_update()
            paparazzi.market_update()
            time.sleep(1)

            # 2. Завгосп аналізує свої потреби і купує, якщо треба
            manager.execute_market_cycle()

            # 3. Випадкові крос-агентні контракти (B2B)
            chance = random.randint(1, 10)
            if chance > 8:
                print(f"\n{YELLOW}⚡ [MARKET EVENT] B2B Contract Initiated!{RESET}")
                baryga.buy_service(paparazzi, "Solar Activity Forecast", 0.002)
            elif chance < 3:
                print(f"\n{YELLOW}⚡ [MARKET EVENT] B2B Contract Initiated!{RESET}")
                prof.buy_service(junkie, "Encrypted Data Backup", 0.005)

            time.sleep(4)
            
    except KeyboardInterrupt:
        print(f"\n{RED}🛑 System halted. All agents entered sleep mode.{RESET}")

if __name__ == "__main__":
    main()