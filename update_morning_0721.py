import json

pfile = '/home/azureuser/apex-capital-daily/portfolio.json'
with open(pfile) as f:\n    p = json.load(f)\n\nprices = {"601899": 29.95, "000100": 5.00, "000977": 81.30}
total_mv = 0
for h in p["holdings"]:
    if h["code"] in prices:
        h["close_price"] = prices[h["code"]]
        h["market_value"] = prices[h["code"]] * h["quantity"]
    total_mv += h["market_value"]

p["total_value"] = round(p["cash"] + total_mv, 1)
p["total_pnl"] = round(p["total_value"] - p["initial_capital"], 1)
p["total_pnl_pct"] = "{:.2f}%".format(p["total_pnl"] / p["initial_capital"] * 100)
p["last_check"] = "2026-07-21 09:28"

p["equity_history"].append({
    "date": "2026-07-21",
    "total_value": p["total_value"],
    "market_value": round(total_mv, 1),
    "cash": p["cash"],
    "holdings_count": len(p["holdings"])
})

with open(pfile, 'w') as f:\n    json.dump(p, f, ensure_ascii=False, indent=2)\n\nprint("总值: {} 现金: {} 持仓市值: {}".format(p["total_value"], p["cash"], total_mv))
