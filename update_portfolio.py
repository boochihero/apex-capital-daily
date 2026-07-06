import json

with open('/home/azureuser/apex-capital-daily/portfolio.json', 'r') as f:\n    p = json.load(f)\n\n# Update holdings with today's closing prices\nfor h in p['holdings']:
    if h['code'] == '601899':
        h['close_price'] = 28.28
        h['market_value'] = round(28.28 * h['quantity'], 2)
    elif h['code'] == '002245':
        h['close_price'] = 22.37
        h['market_value'] = round(22.37 * h['quantity'], 2)

# Recalculate totals
cash = p['cash']  # 24506
market_value = sum(h['market_value'] for h in p['holdings'])
total_value = cash + market_value

p['total_value'] = round(total_value, 2)
p['total_pnl'] = round(total_value - 50000, 2)
p['total_pnl_pct'] = f"{(total_value/50000-1)*100:+.2f}%"

# Update equity_history - remove duplicate 2026-07-06 entries and add final one
eq_history = [e for e in p['equity_history'] if e['date'] != '2026-07-06']
eq_history.append({
    "date": "2026-07-06",
    "total_value": round(total_value, 2),
    "market_value": round(market_value, 2),
    "cash": cash,
    "holdings_count": len(p['holdings'])
})
p['equity_history'] = eq_history
p['last_check'] = "2026-07-06 15:05"

with open('/home/azureuser/apex-capital-daily/portfolio.json', 'w') as f:\n    json.dump(p, f, ensure_ascii=False, indent=2)\n\nprint(f"Updated: total_value={total_value}, market_value={market_value}, cash={cash}")
print(f"equity_history entries: {len(eq_history)}")
print(f"Last 5: {[(e['date'], e['total_value']) for e in eq_history[-5:]]}")
