# 📊 Apex Capital Daily Reports

A股每日自动报告，由 Bocchi (AI) 生成。

## 目录结构

```
YYYY-MM/
  YYYY-MM-DD/
    YYYY-MM-DD-morning.md    # 每日 9:27 竞价速报
    YYYY-MM-DD-evening.md    # 每日 15:05 盘后复盘
  WEEK_1.md                  # 当月第1周总结（周五15:05后生成）
  WEEK_2.md
  WEEK_3.md
  WEEK_4.md
```

## 内容说明

### 早盘速报（morning）
- 大盘情绪评级
- 板块风向 Top3
- 主板强势竞价股 Top10
- 连板/情绪龙头识别
- 重点关注方向

### 盘后复盘（evening）
- 盘面概况（指数、涨跌比、成交额）
- 核心题材回顾
- 早盘推荐票表现
- 明日计划（触发条件 + 止损）

### 周总结（WEEK_N）
- 本周大盘走势
- 本周最强题材/板块
- 本周推荐胜率统计
- 下周市场展望

> 数据来源：东方财富，仅供学习参考，不构成投资建议。
