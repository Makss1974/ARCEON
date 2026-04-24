import requests
import uuid
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

class ArcBridge:
    def __init__(self, api_key, entity_secret):
        self.api_key = api_key
        self.entity_secret = entity_secret
        self.base_url = "https://api.circle.com/v1/w3s"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _get_ciphertext(self):
        # 1. Fetch the public key from Circle
        resp = requests.get(f"{self.base_url}/config/entity/publicKey", headers=self.headers)
        pub_key_pem = resp.json()['data']['publicKey']
        
        # 2. Encrypt the raw Entity Secret (32-byte hex)
        secret_bytes = bytes.fromhex(self.entity_secret)
        rsa_key = RSA.import_key(pub_key_pem)
        cipher = PKCS1_OAEP.new(rsa_key, hashAlgo=SHA256)
        encrypted_bytes = cipher.encrypt(secret_bytes)
        
        # 3. Return Base64 encoded ciphertext
        return base64.b64encode(encrypted_bytes).decode('utf-8')

    def transfer_usdc(self, source_wallet_id, destination_address, amount):
        ciphertext = self._get_ciphertext()
        
        payload = {
            "idempotencyKey": str(uuid.uuid4()),
            "walletId": source_wallet_id,
            "destinationAddress": destination_address,
            "amounts": [str(amount)],
            "feeLevel": "MEDIUM",
            "blockchain": "ARC-TESTNET",
            "tokenAddress": "0x3600000000000000000000000000000000000000",
            "entitySecretCiphertext": ciphertext
        }
        
        response = requests.post(f"{self.base_url}/developer/transactions/transfer", json=payload, headers=self.headers)
        
        if response.status_code == 201:
            return {"status": "SUCCESS", "txHash": response.json()['data']['id']} 
        else:
            print(f"Circle API Error: {response.text}")
            return {"status": "FAILED"}
