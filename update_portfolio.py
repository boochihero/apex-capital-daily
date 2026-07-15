import json

portfolio_path = '/home/azureuser/apex-capital-daily/portfolio.json'
with open(portfolio_path) as f:\n    p = json.load(f)\n\n# 买入金安国纪\nbuy_code = "002636"
buy_name = "金安国纪"
buy_price = 102.20
buy_qty = 100
buy_amt = buy_price * buy_qty  # 10220

p["cash"] = round(p["cash"] - buy_amt, 2)
p["holdings"].append({
    "code": buy_code,
    "name": buy_name,
    "buy_price": buy_price,
    "quantity": buy_qty,
    "buy_date": "2026-07-15",
    "cost": buy_amt,
    "close_price": buy_price,
    "market_value": buy_amt
})

# 更新总值
mv = sum(h["market_value"] for h in p["holdings"])
p["total_value"] = round(p["cash"] + mv, 2)
p["total_pnl"] = round(p["total_value"] - p["initial_capital"], 2)
p["total_pnl_pct"] = f"{(p['total_pnl']/p['initial_capital']*100):.2f}%"

# 添加交易记录
p["trade_log"].append({
    "date": "2026-07-15",
    "time": "09:28",
    "action": "BUY",
    "code": buy_code,
    "name": buy_name,
    "price": buy_price,
    "quantity": buy_qty,
    "amount": buy_amt
})

p["last_check"] = "2026-07-15 09:28"

p["equity_history"].append({
    "date": "2026-07-15",
    "total_value": p["total_value"],
    "market_value": mv,
    "cash": p["cash"],
    "holdings_count": len(p["holdings"])
})

with open(portfolio_path, 'w', encoding='utf-8') as f:\n    json.dump(p, f, ensure_ascii=False, indent=2)\n\nprint(f"更新完成: 现金={p['cash']}, 持仓={len(p['holdings'])}只, 总值={p['total_value']}")
for h in p["holdings"]:
    print(f"  {h['code']} {h['name']} {h['quantity']}股 @ {h['buy_price']}")
