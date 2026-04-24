import requests

# ВСТАВ СВІЙ РЕАЛЬНИЙ API KEY (той самий, що в main.py)
api_key = "6e20e2cf72fad038e6c606dde6b8ab03:1b380273c64d8749fc2dc37502a1a5f4" 

headers = {"Authorization": f"Bearer {api_key}"}

# ID ваших гаманців з main.py
wallets = {
    "SAIN-HOME (Завгосп)": "f1aeee59-c0cd-5fc2-a03c-0d6b478267e6",
    "Solar-Baryga (Енергія)": "c3cded8a-409c-5680-bc17-d82665315591",
    "Professor (Обчислення)": "34aab256-96e2-53db-b51c-c36e8f562d7b",
    "Paparazzi (Дані)": "4160f877-a9bb-53fa-9921-a5389144d3a4",
    "Junkie (Пам'ять)": "479aa4ec-1287-5de0-950a-af384cd67565"
}

print("\n🔍 Перевірка балансів у мережі Arc Testnet...")
print("-" * 50)

for name, w_id in wallets.items():
    url = f"https://api.circle.com/v1/w3s/wallets/{w_id}/balances"
    resp = requests.get(url, headers=headers)
    
    if resp.status_code == 200:
        balances = resp.json().get('data', {}).get('tokenBalances', [])
        if balances:
            for b in balances:
                print(f"✅ {name}: {b['amount']} {b['token']['symbol']}")
        else:
            print(f"⚠️ {name}: 0 USDC (гаманець порожній, чекаємо транзакцію)")
    else:
        print(f"❌ {name}: Помилка Circle API ({resp.status_code})")
        
print("-" * 50 + "\n")
