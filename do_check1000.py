import json

PORTFOLIO = '/home/azureuser/apex-capital-daily/portfolio.json'

with open(PORTFOLIO, 'r') as f:\n    p = json.load(f)\n\n# Update holdings with current prices\nfor h in p['holdings']:
    if h['code'] == '000100':
        h['close_price'] = 4.80
        h['market_value'] = round(4.80 * h['quantity'], 2)
    elif h['code'] == '002558':
        if 'close_price' not in h:\n            h['close_price'] = h['buy_price']\n        h['close_price'] = 28.72\n        h['market_value'] = round(28.72 * h['quantity'], 2)

total_mv = sum(h['market_value'] for h in p['holdings'])
total_value = total_mv + p['cash']
p['total_value'] = round(total_value, 2)
p['total_pnl'] = round(total_value - 50000, 2)
p['total_pnl_pct'] = f"{(total_value - 50000)/50000*100:.2f}%"
p['last_check'] = '2026-07-30 10:00'

# Update equity history last entry
p['equity_history'][-1] = {
    'date': '2026-07-30',
    'total_value': round(total_value, 2),
    'market_value': round(total_mv, 2),
    'cash': p['cash'],
    'holdings_count': len(p['holdings'])
}

with open(PORTFOLIO, 'w') as f:\n    json.dump(p, f, ensure_ascii=False, indent=2)\n\nprint(f"total_value={total_value}, mv={total_mv}")
