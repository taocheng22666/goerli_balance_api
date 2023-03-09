# Goerli測試網錢包餘額批量查詢腳本
##### 這是一個小工具，可以批量查詢Goerli測試網絡上以太坊錢包地址的餘額，並導出Excel文件。
This is a small tool that can batch query the balance of Ethereum wallet addresses 
on the Goerli test network and export the results to an Excel file.

## 使用方法  Usage
### 1 . 安裝依賴 Prerequisites
```text
pip install requests
pip install openpyxl
```

### 2 . 開始 Start
##### 1 . 將 api.py 中的 ETHERSCAN_API_KEY 更換成您在 Etherscan 上申請的 API Key
1. Replace the ETHERSCAN_API_KEY in api.py with the API Key you applied for on Etherscan.
##### 2 . 將您要查詢的錢包地址輸入 wallets.txt 
2. Enter the wallet addresses you want to query into wallets.txt
##### 3 . 查詢的結果會輸出在工具運行的同個路徑下
3. The query results will be output in the same path as the tool is running.
### 3 . Enjoy !
### 4 . 相關鏈結 Links
[Goerli Testnet Etherscan API Docs](https://docs.etherscan.io/v/goerli-etherscan/)  
[Etherscan APIs](https://etherscan.io/apis)
