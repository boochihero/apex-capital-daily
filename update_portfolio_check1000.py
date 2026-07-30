import json
PORTFOLIO = "/home/azureuser/apex-capital-daily/portfolio.json"
with open(PORTFOLIO) as f: p = json.load(f)
for h in p["holdings"]:
    if h["code"] == "000100":
        h["close_price"] = 4.80
        h["market_value"] = round(4.80 * h["quantity"], 2)
    elif h["code"] == "002558":
        h["close_price"] = 28.72
        h["market_value"] = round(28.72 * h["quantity"], 2)
total_mv = sum(h["market_value"] for h in p["holdings"])
total_value = round(total_mv + p["cash"], 2)
p["total_value"] = total_value
p["total_pnl"] = round(total_value - 50000, 2)
p["total_pnl_pct"] = f"{(total_value - 50000)/50000*100:.2f}%"
p["last_check"] = "2026-07-30 10:00"
p["equity_history"][-1] = {"date":"2026-07-30","total_value":total_value,"market_value":round(total_mv,2),"cash":p["cash"],"holdings_count":len(p["holdings"])}
with open(PORTFOLIO,"w") as f: json.dump(p, f, ensure_ascii=False, indent=2)
print(f"total_value={total_value}, mv={total_mv}")
