import { initiateDeveloperControlledWalletsClient } from "@circle-fin/developer-controlled-wallets";

async function main() {
  const apiKey = process.env.CIRCLE_API_KEY;
  const entitySecret = process.env.CIRCLE_ENTITY_SECRET;

  if (!apiKey || !entitySecret) {
     console.error("Помилка: Не знайдено ключі у файлі .env!");
     return;
  }

  const client = initiateDeveloperControlledWalletsClient({ apiKey, entitySecret });
  const myWalletSetId = "c73d7124-e012-52cc-a70e-e62b3bffed05"; // Ваш ідентифікатор Сім'ї

  console.log("🔍 Стукаємо в Circle: завантажуємо повний список ваших гаманців...");

  // ВИПРАВЛЕНО: listWallets замість getWallets
  const response = await client.listWallets({
    walletSetId: myWalletSetId
  });

  const wallets = response.data?.wallets;

  if (wallets && wallets.length > 0) {
      console.log(`\n✅ ЗНАЙДЕНО ${wallets.length} ГАМАНЦІВ. Ось ваш бойовий склад:\n`);
      
      wallets.forEach((w, index) => {
          let role = "";
          if (index === 0) role = " (Завгосп / Manager)";
          if (index === 1) role = " (Сонячний Барига)";
          if (index === 2) role = " (Професор)";
          if (index === 3) role = " (Папараці)";
          if (index === 4) role = " (Кладовщик)";

          console.log(`Бот №${index + 1}${role}:`);
          console.log(`  ID (для коду): ${w.id}`);
          console.log(`  Address (для крана): ${w.address}\n`);
      });
  } else {
      console.log("Щось пішло не так.", response);
  }
}

main();
