# 2023/03/09 By.Ta26.eth
# 這是 API Docs : https://docs.etherscan.io/v/goerli-etherscan/

import requests
import pandas as pd

# set API endpoint & API key
ETHERSCAN_ENDPOINT = "https://api-goerli.etherscan.io/api" # Goerli 測試網的 API endpoint
api_key = "這裡替換成你的API密鑰"  # Etherscan API key

# def 要查詢的錢包地址列表
wallets = [
    "0x3",
    "0x3",
    "0x1"
]  # 替換 Goerli 測試網錢包地址....

# 建立一個空的DataFrame
df = pd.DataFrame(columns=["Address", "Balance (ETH)"])

# 查詢每個錢包地址的餘額
for wallet in wallets:
    # 設置查詢餘額的API請求
    params = {
        "module": "account",
        "action": "balance",
        "address": wallet,
        "tag": "latest",
        "apikey": api_key,
    }

    # 用Etherscan API查詢餘額
    response = requests.get(ETHERSCAN_ENDPOINT, params=params)

    # 因為 API 返回的 result 是 wei 單位，所以要解析轉換成正常以太幣數量 (10^18)
    balance_wei = int(response.json()["result"])
    balance_eth = balance_wei / 10 ** 18

    # 將餘額添加到DataFrame中，用 frame.append() 會出現FutureWarning，所以這裡用 pandas.concat()
    df = pd.concat([df, pd.DataFrame({"Address": [wallet], "Balance (ETH)": [balance_eth]})], ignore_index=True)

# 將DataFrame匯出到Excel檔案
output_file = "goerli_balances.xlsx"
df.to_excel(output_file, index=False)
print(f"Balances saved to {output_file}")
