import { initiateDeveloperControlledWalletsClient } from "@circle-fin/developer-controlled-wallets";

async function main() {
  const apiKey = process.env.CIRCLE_API_KEY;
  const entitySecret = process.env.CIRCLE_ENTITY_SECRET;

  if (!apiKey || !entitySecret) {
     console.error("Помилка: Не знайдено ключі у файлі .env!");
     return;
  }

  const client = initiateDeveloperControlledWalletsClient({ apiKey, entitySecret });
  const myWalletSetId = "c73d7124-e012-52cc-a70e-e62b3bffed05"; // Ваш ідентифікатор з попередніх логів

  console.log("🚀 Магія починається: генеруємо ще 3 гаманці для команди...");

  const response = await client.createWallets({
    walletSetId: myWalletSetId,
    blockchains: ["ARC-TESTNET"],
    count: 3,
    accountType: "EOA",
  });

  const wallets = response.data?.wallets;

  if (wallets) {
      console.log("\n✅ ГОТОВО! Ваші нові гаманці:");
      wallets.forEach((w, index) => {
          console.log(`Бот №${index + 3}:`);
          console.log(`  ID (для коду): ${w.id}`);
          console.log(`  Address (для крана): ${w.address}\n`);
      });
  } else {
      console.log("Щось пішло не так. Перевірте логи.", response);
  }
}

main();
