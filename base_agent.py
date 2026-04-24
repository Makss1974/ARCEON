import time
from datetime import datetime

class BaseAgent:
    def __init__(self, agent_id, role, wallet_id, wallet_address, bridge):
        self.agent_id = agent_id
        self.role = role
        self.wallet_id = wallet_id
        self.wallet_address = wallet_address
        self.bridge = bridge

    def log(self, action_type, message, color="\033[0m"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {color}🤖 {self.agent_id} | {self.role.upper()} | {action_type}: {message}\033[0m")

    def buy_service(self, target_bot, service_name, price):
        self.log("REQUEST", f"GET /{service_name.replace(' ', '_')} from {target_bot.agent_id}", "\033[93m")
        time.sleep(0.5)
        
        target_bot.log("x402_MIDDLEWARE", f"HTTP 402 Payment Required. Price: {price} USDC", "\033[93m")
        time.sleep(0.5)
        
        self.log("AUTO-PAY", "Intercepted 402. Initiating Circle Nanopayment...", "\033[93m")
        
        tx = self.bridge.transfer_usdc(
            source_wallet_id=self.wallet_id,
            destination_address=target_bot.wallet_address,
            amount=str(price)
        )
        
        if tx and tx.get("status") == "SUCCESS":
            self.log("SUCCESS", f"Payment confirmed on-chain! TX Hash: {tx['txHash'][:15]}...", "\033[92m")
            return True
        else:
            self.log("REJECT", "Transaction failed on Arc network.", "\033[91m")
            return False
