import json

with open('/home/azureuser/apex-capital-daily/portfolio.json') as f:\n    p = json.load(f)\n\nprice_map = {\n    '002025': 59.62,
    '601899': 29.95,
    '603663': 100.00
}

for h in p['holdings']:
    if h['code'] in price_map:
        h['close_price'] = price_map[h['code']]
        h['market_value'] = round(h['quantity'] * price_map[h['code']], 2)

mv = sum(h['market_value'] for h in p['holdings'])
total = round(p['cash'] + mv, 2)
p['total_value'] = total
p['total_pnl'] = round(total - p['initial_capital'], 2)
p['total_pnl_pct'] = str(round((total - p['initial_capital']) / p['initial_capital'] * 100, 2)) + '%'
p['last_check'] = '2026-06-23 09:28'

p['equity_history'].append({
    'date': '2026-06-23',
    'total_value': total,
    'market_value': round(mv, 2),
    'cash': p['cash'],
    'holdings_count': len(p['holdings'])
})

with open('/home/azureuser/apex-capital-daily/portfolio.json', 'w', encoding='utf-8') as f:\n    json.dump(p, f, ensure_ascii=False, indent=2)\n\nprint('total=' + str(total) + ' mv=' + str(round(mv, 2)) + ' cash=' + str(p['cash']))\nPYEOF\npython3 /home/azureuser/apex-capital-daily/update_portfolio_0623.py
