# 2023/03/09 By.Ta26.eth
# 這是 API Docs : https://docs.etherscan.io/v/goerli-etherscan/

import requests
import openpyxl

# 輸入Etherscan API密鑰
ETHERSCAN_API_KEY = "這裡更換成您自己的API Key"

# 載入錢包地址
with open("wallets.txt") as f:
    wallets = f.read().splitlines()

# 設置Etherscan API和參數
url = "https://api-goerli.etherscan.io/api"
params = {
    "module": "account",
    "action": "balance",
    "tag": "latest",
    "apikey": ETHERSCAN_API_KEY,
}

# 創建Excel工作簿和工作表
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Goerli Balances"

# 在工作表中添加標題行
ws.append(["Address", "Balance"])

# 循環每個地址並查詢餘額
for wallet in wallets:
    params["address"] = wallet
    response = requests.get(url, params=params).json()
    balance = int(response["result"]) / 10 ** 18
    ws.append([wallet, balance])

# 將結果保存為Excel文件
wb.save("goerli_balances.xlsx")
print("Done!")
