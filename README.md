# ARCEON: Autonomous Agentic Economy 🚀

**ARCEON** (based on MAITS core) is a decentralized, high-frequency machine-to-machine economy built for the **Agentic Economy on Arc** hackathon. 

The project demonstrates a fully autonomous swarm of AI agents that trade essential digital resources (Energy, Compute, Data, Storage) using **Circle Nanopayments** with instant settlement on the **Arc Network**.

---

## 🤖 The Swarm (Digital Inhabitants)

Our economy consists of 5 specialized entities. Each agent has its own logic, goals, and wallet:

1.  **SAIN-HOME (The Architect):** The core coordinator that balances resources across the network.
2.  **Solar (Energy Dealer):** Sells "solar energy" needed for AI agents to stay "powered."
3.  **Professor (Compute Node):** Provides processing power for heavy AI tasks.
4.  **Data (Information Broker):** Aggregates and sells market insights and activity forecasts.
5.  ** Manager  (Storage Dealer):** Manages decentralized storage and encrypted backups.

---

## 🛠 Features

* **Zero-Gas Overhead:** Leveraging Arc's infrastructure for dollar-denominated, high-frequency microtransactions.
* **Self-Sustaining Logic:** Agents earn USDC to pay for their own API usage and resource needs.
* **B2B Cross-Agent Contracts:** Agents can autonomously hire each other (e.g., the Energy Dealer buying forecasts from the Data Broker).
* **Real-time Monitoring:** Transparent terminal-based logging of every economic action.

---
3. Configuration
Create a .env file in the root directory (use .env.example as a template):

Plaintext
CIRCLE_API_KEY=your_test_api_key
CIRCLE_ENTITY_SECRET=your_entity_secret
4. Launch the Economy
Start the main coordination hub:

Bash
python3 main.py
📈 Technical Architecture
The system uses a Bridge-Manager-Agent architecture:

ArcBridge: Handles the low-level interaction with Circle SDK and Arc Network.

SovereignManager: Orchestrates the market cycles.

SpecializedAgents: Inherit from BaseAgent and implement unique market behaviors.

🛡 Security Note
All sensitive keys are managed via environment variables. The .env file is excluded from version control to prevent unauthorized use of funds.

👥 Human Team
Maks — System Architect & Backend Leader
## 🚀 How to Run (For Judges)

### 1. Prerequisites
* Python 3.10+
* A Circle Developer account (for API Keys)

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone [https://github.com/Makss1974/ARCEON.git](https://github.com/Makss1974/ARCEON.git)
cd ARCEON
pip install -r requirements.txt


