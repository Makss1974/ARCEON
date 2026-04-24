import time
import requests

# Всі твої бойові адреси
wallets = [
    "0xd9fb07f8a285e0deb21751b0c26f0000bd0848ab", # Завгосп
    "0xbe2f50b573210885142645769cf857a545b83b3d", # Барига
    "0x8b3fcde91e0d9688a03c8ee9bad99b0a0b5672fa", # Професор
    "0xfcc315b35fd3d83af8f050384a067ad2162f27fc", # Папараці
    "0xe51e63101666fe0877b07ef53c7f56a53aa257c5"  # Кладовщик
]

def refill_wallet(address):
    print(f"[{time.strftime('%H:%M:%S')}] Спроба поповнити: {address}...")
    
    # URL та заголовки для імітації запиту (якщо кран працює через API)
    url = "https://faucet.circle.com/api/request" # Гіпотетичний ендпоінт
    payload = {"address": address, "blockchain": "ARC-TESTNET"}
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Відправляємо запит. Якщо кран вимагає капчу, це може видати помилку 403
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in [200, 201]:
            print(f"✅ Успіх для {address[-6:]}!")
        else:
            print(f"⚠️ Статус {response.status_code}. Можливо, потрібна капча або ліміт IP.")
    except Exception as e:
        print(f"❌ Помилка: {e}")

print("🚀 Нічний авто-кран запущено!")

# Цикл буде працювати безкінечно
while True:
    for wallet in wallets:
        refill_wallet(wallet)
        time.sleep(10) # Пауза 10 секунд між гаманцями, щоб не забанили
    
    print("\n💤 Всі гаманці оброблені. Йду спати на 2 години...")
    time.sleep(7200) # Пауза рівно 2 години (7200 секунд)
