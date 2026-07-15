import json

with open("portfolio.json") as f:
    p = json.load(f)

current_prices = {"601899": 29.05, "000100": 5.12, "002636": 97.19}

for h in p["holdings"]:
    cur = current_prices[h["code"]]
    h["close_price"] = cur
    h["market_value"] = cur * h["quantity"]

total_mv = sum(h["market_value"] for h in p["holdings"])
p["cash"] = 8828.0
p["total_value"] = p["cash"] + total_mv
p["total_pnl"] = p["total_value"] - 50000
p["total_pnl_pct"] = "{:.2f}%".format(p["total_pnl"]/50000*100)
p["last_check"] = "2026-07-15 10:00"

today = "2026-07-15"
today_entry = {"date": today, "total_value": p["total_value"], "market_value": total_mv, "cash": p["cash"], "holdings_count": len(p["holdings"])}
if p["equity_history"] and p["equity_history"][-1]["date"] == today:
    p["equity_history"][-1] = today_entry
else:
    p["equity_history"].append(today_entry)

with open("portfolio.json", "w") as f:
    json.dump(p, f, ensure_ascii=False, indent=2)

print("OK total=", p["total_value"], "cash=", p["cash"])
