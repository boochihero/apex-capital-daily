import json

portfolio_path = '/home/azureuser/apex-capital-daily/portfolio.json'

with open(portfolio_path, 'r') as f:\n    p = json.load(f)\n\nbuy_code = '002202'\nbuy_name = '金风科技'\nbuy_price = 22.89\nbuy_qty = 600\nbuy_amount = round(buy_price * buy_qty, 2)
date_str = '2026-06-30'

p['cash'] = round(p['cash'] - buy_amount, 2)

p['holdings'].append({
    'code': buy_code,
    'name': buy_name,
    'buy_price': buy_price,
    'quantity': buy_qty,
    'buy_date': date_str,
    'cost': buy_amount,
    'close_price': buy_price,
    'market_value': buy_amount
})

holdings_prices = {'600460': 53.50, '000021': 59.45, '002202': 22.89}
total_mv = 0.0
for h in p['holdings']:
    if h['code'] in holdings_prices:
        h['close_price'] = holdings_prices[h['code']]
        h['market_value'] = round(h['quantity'] * holdings_prices[h['code']], 2)
    total_mv += h['market_value']

total_mv = round(total_mv, 2)
p['total_value'] = round(p['cash'] + total_mv, 2)
p['total_pnl'] = round(p['total_value'] - p['initial_capital'], 2)
p['total_pnl_pct'] = '{:.2f}%'.format(p['total_pnl'] / p['initial_capital'] * 100)
p['last_check'] = date_str + ' 09:28'

p['equity_history'].append({
    'date': date_str,
    'total_value': p['total_value'],
    'market_value': total_mv,
    'cash': p['cash'],
    'holdings_count': len(p['holdings'])
})

p['trade_log'].append({
    'date': date_str,
    'time': '09:28',
    'action': 'BUY',
    'code': buy_code,
    'name': buy_name,
    'price': buy_price,
    'quantity': buy_qty,
    'amount': buy_amount
})

with open(portfolio_path, 'w') as f:\n    json.dump(p, f, ensure_ascii=False, indent=2)\n\nprint('买入：' + buy_name + '(' + buy_code + ') ' + str(buy_qty) + '股 @ ' + str(buy_price) + '元 = ' + str(buy_amount) + '元')
print('剩余现金：' + str(p['cash']) + '元')
print('账户总值：' + str(p['total_value']) + '元')
print('持仓：' + str(len(p['holdings'])) + '只')
for h in p['holdings']:
    print('  - ' + h['name'] + '(' + h['code'] + '): ' + str(h['quantity']) + '股 @ ' + str(h['buy_price']) + ' 市值=' + str(h['market_value']))
