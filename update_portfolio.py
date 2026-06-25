import json

with open('/home/azureuser/apex-capital-daily/portfolio.json', 'r') as f:\n    portfolio = json.load(f)\n\n# Update today's close prices and market values\nclose_prices = {"000100": 5.34, "000823": 25.87, "002015": 17.49}

for h in portfolio['holdings']:
    code = h['code']
    if code in close_prices:
        h['close_price'] = close_prices[code]
        h['market_value'] = round(close_prices[code] * h['quantity'], 2)

# Recalculate totals
total_mv = sum(h['market_value'] for h in portfolio['holdings'])
cash = portfolio['cash']
total_value = round(cash + total_mv, 2)

portfolio['total_value'] = total_value
portfolio['total_pnl'] = round(total_value - portfolio['initial_capital'], 2)
portfolio['total_pnl_pct'] = f"{(total_value - portfolio['initial_capital']) / portfolio['initial_capital'] * 100:.2f}%"
portfolio['last_check'] = '2026-06-25 15:05'

# Update equity_history
today_record = {
    "date": "2026-06-25",
    "total_value": total_value,
    "market_value": round(total_mv, 2),
    "cash": cash,
    "holdings_count": len(portfolio['holdings'])
}

# Update or append
existing = [r for r in portfolio['equity_history'] if r['date'] != '2026-06-25']
existing.append(today_record)
portfolio['equity_history'] = existing

with open('/home/azureuser/apex-capital-daily/portfolio.json', 'w') as f:\n    json.dump(portfolio, f, ensure_ascii=False, indent=2)\n\nprint(f"Portfolio updated: total_value={total_value}, market_value={total_mv:.2f}, cash={cash}")
