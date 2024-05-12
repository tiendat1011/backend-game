from efficient_apriori import apriori
import json
import random

TRANSACTION_FILE = 'transaction_data.json'
EXPORT_PATH = 'rules.json'

def create_transaction():
    num_transactions = 10000

    transactions = []
    
    for i in range(num_transactions):
        # Số lượng game trong mỗi giao dịch (ngẫu nhiên từ 1 đến 10)
        num_games = random.randint(1, 10)
        
        # Danh sách chứa ID của các game trong giao dịch
        game_ids = []
        for _ in range(num_games):
            # ID của game (ngẫu nhiên từ 1 đến 57)
            game_id = random.randint(1, 57)
            game_ids.append(game_id)
        
        # Thêm giao dịch vào danh sách các giao dịch
        transactions.append(game_ids)
    
    # Tạo định dạng JSON
    data = {}
    for i, transaction in enumerate(transactions, 1):
        data[i] = transaction

    # Ghi dữ liệu vào file JSON
    with open(TRANSACTION_FILE, "w") as json_file:
        json.dump(data, json_file, indent=4)

    return data

def convert_to_records(data):
    records = []
    for i in range(len(data)):
        records.append(data[i + 1])
    
    return records

def get_rules(records):
    itemsets, rules = apriori(records, min_support=0.01, min_confidence=0.02)
    return itemsets, rules

def export_rules(rules):
    results = []
    for rule in rules:
        base_items = ", ".join(map(str, rule.lhs))
        add_items = ", ".join(map(str, rule.rhs))
        support = rule.support
        confidence = rule.confidence
        lift = rule.lift

        results.append({
            'base_items': base_items,
            'add_items': add_items,
            'support': support,
            'confidence': confidence,
            'lift': lift
    })
    results = sorted(results, key=lambda x: x['support'], reverse=True)
    with open(EXPORT_PATH, 'w') as json_file:
        json.dump(results, json_file, indent=4)



def main():
    transaction_data = create_transaction()
    records = convert_to_records(transaction_data)
    _, rules = get_rules(records)
    export_rules(rules)

main()