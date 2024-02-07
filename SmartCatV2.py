import time
import pandas as pd
import web3
from web3 import Web3
from web3.middleware import geth_poa_middleware
import requests
import json

def wait_for_receipt(w3, tx_hash, max_attempts=60):
    attempts = 0
    while attempts < max_attempts:
        print("Waiting for transaction receipt... (Attempt {}/{} )".format(attempts + 1, max_attempts))
        time.sleep(5)
        try:
            tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
            if tx_receipt is not None and tx_receipt['status'] is not None:
                return tx_receipt
        except web3.exceptions.TransactionNotFound:
            pass
        attempts += 1

    return None




def canLevelup(cat_id):
    url = 'https://polygon-mainnet.infura.io/v3/3ca8f1ba91f84e1f97c99f6218fe3743'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-platform': 'Windows',
        'sec-ch-ua-mobile': '?0',
        'origin': 'https://viewer.tokenscript.org',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://viewer.tokenscript.org/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    hex_64_cat_id = f'{cat_id:0>64x}'
    method_hex = '0x842b4d17'
    custom_param = method_hex + hex_64_cat_id

    data = {
        "method": "eth_call",
        "params": [{"to": "0x7573933eb12fa15d5557b74fdaff845b3baf0ba2", "data": custom_param}, "latest"],
        "id": 42,
        "jsonrpc": "2.0"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    result_hex = json.loads(response.text)["result"]



    # 分割第一列（66个字符）
    first_column = result_hex[:66]
    # 分割其他列（64个字符）
    other_columns = [result_hex[i:i+64] for i in range(66, len(result_hex), 64)]
    # 将所有分割后的值放到一个列表中
    all_columns = [first_column] + other_columns

    # # 获取第九个位置的数据，是否能升级
    flag = position_8_value = int(all_columns[8], 16)


    return flag

def levelUp(w3, config, private_key, id, method_hex):
    hex_64_result = f'{id:0>64x}'

    # Construct combined hex string
    combined_hex = method_hex + hex_64_result

    # Create transaction
    account = w3.eth.account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(account.address, 'latest')

    gas_price_base = w3.eth.gas_price
    gas_price = int(gas_price_base * 1.5)

    transaction = {
        'to': config["contract_address"],
        'value': 0,
        'gasPrice': gas_price,
        'nonce': nonce,
        'data': combined_hex,
        'chainId': config["chain_id"]
    }

    # Hardcoded estimated gas for simplicity
    gas_limit = config["gas_limit"]
    transaction['gas'] = gas_limit

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Output transaction hash
    # print(f"Transaction hash ({method_hex}): {tx_hash.hex()}")
    wallet_address = account.address
    print(f"Transaction hash ({wallet_address}_{id}): {tx_hash.hex()}")

    # Wait for transaction receipt
    tx_receipt = None
    # while tx_receipt is None or tx_receipt['status'] is None:
    #     print("Waiting for transaction receipt...")
    #     time.sleep(5)  # Add a delay of 5 seconds before checking the receipt again
    #     try:
    #         tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
    #     except web3.exceptions.TransactionNotFound:
    #         pass

    tx_receipt = wait_for_receipt(w3, tx_hash)

    if tx_receipt['status'] == 1:
        print("Transaction successful!")
        print("操作结束等待60秒冷却")
        time.sleep(60)
    else:
        print("Transaction failed!")

def acceptFriend(cat_id):
    url = 'https://polygon-mainnet.infura.io/v3/3ca8f1ba91f84e1f97c99f6218fe3743'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-platform': 'Windows',
        'sec-ch-ua-mobile': '?0',
        'origin': 'https://viewer.tokenscript.org',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://viewer.tokenscript.org/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    hex_64_cat_id = f'{cat_id:0>64x}'
    method_hex = '0xefc51df6'
    custom_param = method_hex + hex_64_cat_id

    data = {
        "method": "eth_call",
        "params": [{"to": "0x7573933eb12fa15d5557b74fdaff845b3baf0ba2", "data": custom_param}, "latest"],
        "id": 42,
        "jsonrpc": "2.0"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    result_hex = json.loads(response.text)["result"]

    # print(result_hex)

    # 分割第一列（66个字符）
    first_column = result_hex[:66]
    # 分割其他列（64个字符）
    other_columns = [result_hex[i:i + 64] for i in range(66, len(result_hex), 64)]
    # 将所有分割后的值放到一个列表中
    all_columns = [first_column] + other_columns

    # 获取第二个位置的数据
    position_2_value = int(all_columns[1], 16)

    # 根据位置数量处理返回值
    result_values = []
    index = 2 + position_2_value
    for i in range(position_2_value):
        result_values.append(int(all_columns[index], 16))
        index = index + 9  # 逐步增加索引，以适应不同位置的情况

    return result_values


def execute_transaction(w3, config, private_key, id, method_hex, num_executions):
    for _ in range(num_executions):
        hex_64_result = f'{id:0>64x}'

        # Construct combined hex string
        combined_hex = method_hex + hex_64_result

        # Create transaction
        account = w3.eth.account.from_key(private_key)
        nonce = w3.eth.get_transaction_count(account.address, 'latest')

        gas_price_base = w3.eth.gas_price
        gas_price = int(gas_price_base * 1.5)

        transaction = {
            'to': config["contract_address"],
            'value': 0,
            'gasPrice': gas_price,
            'nonce': nonce,
            'data': combined_hex,
            'chainId': config["chain_id"]
        }

        # Hardcoded estimated gas for simplicity
        gas_limit = config["gas_limit"]
        transaction['gas'] = gas_limit

        # Sign transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

        # Send transaction
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Output transaction hash
        # print(f"Transaction hash ({method_hex}): {tx_hash.hex()}")
        wallet_address = account.address
        print(f"Transaction hash ({wallet_address}_{id}): {tx_hash.hex()}")

        # Wait for transaction receipt
        tx_receipt = None
        # while tx_receipt is None or tx_receipt['status'] is None:
        #     print("Waiting for transaction receipt...")
        #     time.sleep(5)  # Add a delay of 5 seconds before checking the receipt again
        #     try:
        #         tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
        #     except web3.exceptions.TransactionNotFound:
        #         pass

        tx_receipt = wait_for_receipt(w3, tx_hash)

        if tx_receipt['status'] == 1:
            print("Transaction successful!")
            print("操作结束等待60秒冷却")
            time.sleep(60)
        else:
            print("Transaction failed!")


def invite(w3, config, private_key, myid, method_hex, friendid):
    line1 = f'{myid:0>64x}'
    line2 = f'{friendid:0>64x}'

    # Construct combined hex string
    combined_hex = method_hex + line1 + line2

    # Create transaction
    account = w3.eth.account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(account.address, 'latest')

    gas_price_base = w3.eth.gas_price
    gas_price = int(gas_price_base * 1.5)

    transaction = {
        'to': config["contract_address"],
        'value': 0,
        'gasPrice': gas_price,
        'nonce': nonce,
        'data': combined_hex,
        'chainId': config["chain_id"]
    }

    # Hardcoded estimated gas for simplicity
    gas_limit = config["gas_limit"]
    transaction['gas'] = gas_limit

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Output transaction hash
    # print(f"Transaction hash ({method_hex}): {tx_hash.hex()}")
    wallet_address = account.address
    print(f"Transaction hash ({wallet_address}_{myid}): {tx_hash.hex()}")

    # Wait for transaction receipt
    tx_receipt = None
    # while tx_receipt is None or tx_receipt['status'] is None:
    #     print("Waiting for transaction receipt...")
    #     time.sleep(5)  # Add a delay of 5 seconds before checking the receipt again
    #     try:
    #         tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
    #     except web3.exceptions.TransactionNotFound:
    #         pass

    tx_receipt = wait_for_receipt(w3, tx_hash)

    if tx_receipt['status'] == 1:
        print("Transaction successful!")
        print("操作结束等待60秒冷却")
        time.sleep(60)
    else:
        print("Transaction failed!")


if __name__ == "__main__":
    # Load configuration from config.json
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    # Initialize web3
    w3 = Web3(Web3.HTTPProvider(config["rpc_url"]))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # Load user parameters from Excel file
    df = pd.read_csv("user_parameters.csv", dtype=str)

    # Execute transactions based on user parameters
    for index, row in df.iterrows():
        private_key = row['Private Key']
        id_my = int(row['myID'])
        num_feed = int(row['Feed'])
        num_clean = int(row['Clean'])
        friend_ids = str(row['friendID'])

        # 默认检查是否需要升级，如果需要则升级，不需要则不升级
        flag = canLevelup(id_my)
        if flag == True:
            print('可以升级')
            levelUp(w3, config, private_key, id_my, '0x0ce90ec2')
        else:
            print('不可以升级')



        # 喂猫
        execute_transaction(w3, config, private_key, id_my, '0x350f7198', num_feed)
        # 清洗猫
        execute_transaction(w3, config, private_key, id_my, '0x0ce81dfd', num_clean)

        # 假如有填了邀请的好友，那么就邀请他们
        if friend_ids  != '0':
            friend_ids = [int(id) for id in friend_ids.split(',')]
            for id_friend in friend_ids:
                invite(w3, config, private_key, id_my, '0x5e2b9146', id_friend)

        # 默认检查是否有需要接收邀请的好友，如果有的话，就接收邀请
        accept_id_result = acceptFriend(id_my)
        if accept_id_result is not None:
            accept_id_result = [int(id) for id in accept_id_result]
            for id_friend in accept_id_result:
                invite(w3, config, private_key, id_my, '0x64fb0965', id_friend)
                print('接受了一个好友邀请')
