import time
import random
from base_agent import BaseAgent

GREEN, YELLOW, RED, BLUE, RESET = "\033[92m", "\033[93m", "\033[91m", "\033[94m", "\033[0m"

class SovereignManager(BaseAgent):
    def __init__(self, node_id, wallet_id, bridge, neighbors):
        super().__init__(node_id, "Executive Manager", wallet_id, "", bridge)
        self.neighbors = neighbors
        self.energy_level = 100
        self.cpu_load = 20

    def execute_market_cycle(self):
        print(f"\n{BLUE}--- [ {self.agent_id} ] HOMEOSTASIS STATUS ---{RESET}")
        
        self.energy_level -= random.randint(10, 20)
        self.cpu_load += random.randint(10, 30)
        
        if self.energy_level < 30:
            print(f"{RED}[CRISIS]{RESET} Energy deficit! Battery: {self.energy_level}%.")
            self._pay_neighbor("solar_bot", "Emergency Power", 0.005)
            self.energy_level = 100  
        elif self.cpu_load > 80:
            print(f"{RED}[CRISIS]{RESET} CPU Overload: {self.cpu_load}%.")
            self._pay_neighbor("prof_bot", "Neural Processing", 0.003)
            self.cpu_load = 20  
        else:
            print(f"{GREEN}[IDLE]{RESET} System stable. CPU: {self.cpu_load}%, Energy: {self.energy_level}%.")

    def _pay_neighbor(self, bot_key, service_name, price):
        target_address = self.neighbors.get(bot_key)
        if not target_address:
            return False
            
        self.log("REQUEST", f"GET /{service_name.replace(' ', '_')}", YELLOW)
        time.sleep(0.5)
        
        print(f"{YELLOW}[x402 Middleware]{RESET} HTTP 402 Payment Required: {price} USDC")
        self.log("AUTO-PAY", "Initiating Circle Nanopayment...", YELLOW)
        
        tx = self.bridge.transfer_usdc(
            source_wallet_id=self.wallet_id,
            destination_address=target_address,
            amount=str(price)
        )
        
        if tx and tx.get("status") == "SUCCESS":
            self.log("SUCCESS", f"Payment confirmed on-chain! TX Hash: {tx['txHash'][:15]}...", GREEN)
            return True
        else:
            self.log("REJECT", "Transaction failed on Arc network.", RED)
            return False
