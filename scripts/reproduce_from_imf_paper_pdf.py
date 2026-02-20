#!/usr/bin/env python3
"""Build a CSV dataset transcribed from the IMF paper table for Ghana (2022-2028).

Source table in `IMF paper.pdf`:
"Ghana: Selected Economic and Financial Indicators, 2022-28".
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reproduced" / "imf_paper_ghana_selected_indicators_2022_2028.csv"

# Values transcribed directly from IMF table in IMF paper.pdf (no repository CSV inputs).
SERIES = [
    ("GDP at constant prices", "annual percentage change", {2022: 3.1, 2023: 2.3, 2024: 2.8, 2025: 4.4, 2026: 4.9, 2027: 5.0, 2028: 5.0}),
    ("Non-extractive GDP", "annual percentage change", {2022: 2.4, 2023: 2.5, 2024: 2.3, 2025: 4.4, 2026: 4.8, 2027: 5.0, 2028: 5.0}),
    ("Extractive GDP", "annual percentage change", {2022: 8.1, 2023: 0.4, 2024: 6.2, 2025: 4.2, 2026: 5.9, 2027: 5.0, 2028: 5.0}),
    ("Real GDP per capita", "annual percentage change", {2022: 0.9, 2023: -0.3, 2024: 0.2, 2025: 1.8, 2026: 2.3, 2027: 2.4, 2028: 2.4}),
    ("GDP deflator", "annual percentage change", {2022: 28.2, 2023: 36.3, 2024: 20.2, 2025: 10.9, 2026: 7.5, 2027: 7.5, 2028: 7.5}),
    ("Consumer price index (end of period)", "annual percentage change", {2022: 54.1, 2023: 27.6, 2024: 15.0, 2025: 8.0, 2026: 8.0, 2027: 8.0, 2028: 8.0}),
    ("Consumer price index (annual average)", "annual percentage change", {2022: 31.9, 2023: 40.2, 2024: 22.3, 2025: 11.5, 2026: 8.0, 2027: 8.0, 2028: 8.0}),
    ("Revenue", "percent of GDP", {2022: 15.8, 2023: 15.7, 2024: 16.7, 2025: 17.3, 2026: 18.2, 2027: 18.1, 2028: 18.0}),
    ("Expenditure (commitment basis)", "percent of GDP", {2022: 27.7, 2023: 20.4, 2024: 21.7, 2025: 21.6, 2026: 21.8, 2027: 21.2, 2028: 21.1}),
    ("Overall balance (commitment basis)", "percent of GDP", {2022: -11.8, 2023: -4.6, 2024: -5.0, 2025: -4.3, 2026: -3.6, 2027: -3.1, 2028: -3.0}),
    ("Primary balance (commitment basis)", "percent of GDP", {2022: -4.4, 2023: -0.5, 2024: 0.5, 2025: 1.5, 2026: 1.5, 2027: 1.5, 2028: 1.5}),
    ("Non-oil primary balance (commitment basis)", "percent of GDP", {2022: -6.3, 2023: -1.8, 2024: -0.8, 2025: 0.0, 2026: 0.0, 2027: 0.1, 2028: 0.0}),
    ("Public debt (gross)", "percent of GDP", {2022: 93.3, 2023: 86.1, 2024: 83.6, 2025: 80.9, 2026: 77.9, 2027: 74.9, 2028: 72.0}),
    ("Domestic debt", "percent of GDP", {2022: 50.0, 2023: 37.0, 2024: 33.7, 2025: 31.8, 2026: 29.4, 2027: 27.8, 2028: 26.4}),
    ("External debt", "percent of GDP", {2022: 43.3, 2023: 49.1, 2024: 49.9, 2025: 49.1, 2026: 48.6, 2027: 47.1, 2028: 45.6}),
    ("Credit to the private sector", "annual percentage change", {2022: 31.8, 2023: 12.6, 2024: 22.0, 2025: 13.0, 2026: 15.0, 2027: 15.0, 2028: 15.0}),
    ("Broad money (M2+)", "annual percentage change", {2022: 32.9, 2023: 22.8, 2024: 17.4, 2025: 16.9, 2026: 16.0, 2027: 16.0, 2028: 16.0}),
    ("Velocity (GDP/M2+, end of period)", "ratio", {2022: 3.4, 2023: 3.8, 2024: 4.0, 2025: 4.0, 2026: 3.9, 2027: 3.8, 2028: 3.7}),
    ("Base money", "annual percentage change", {2022: 57.3, 2023: 6.0, 2024: 17.4, 2025: 12.1, 2026: 13.6, 2027: 11.5, 2028: 13.8}),
    ("Policy rate (end of period)", "percent", {2022: 27.0}),
    ("Current account balance", "percent of GDP", {2022: -2.1, 2023: -1.7, 2024: -1.9, 2025: -2.2, 2026: -2.4, 2027: -2.4, 2028: -2.4}),
    ("BOP financing gap", "US$ million", {2023: 4216, 2024: 3312, 2025: 3910, 2026: 3321, 2027: 1410, 2028: 937}),
    ("IMF", "US$ million", {2023: 1200, 2024: 720, 2025: 720, 2026: 360, 2027: 0, 2028: 0}),
    ("World Bank", "US$ million", {2023: 330, 2024: 620, 2025: 350, 2026: 250, 2027: 0, 2028: 0}),
    ("AfDB", "US$ million", {2023: 59, 2024: 44, 2025: 0, 2026: 0, 2027: 0, 2028: 0}),
    ("Residual gap", "US$ million", {2023: 2627, 2024: 1928, 2025: 2840, 2026: 2711, 2027: 1410, 2028: 937}),
    ("Gross international reserves (program)", "US$ million", {2022: 1441, 2023: 2388, 2024: 3852, 2025: 5501, 2026: 7677, 2027: 9250, 2028: 10874}),
    ("Gross international reserves in months of prospective imports", "months", {2022: 0.7, 2023: 1.1, 2024: 1.7, 2025: 2.3, 2026: 3.0, 2027: 3.5, 2028: 3.9}),
    ("Gross international reserves", "US$ million", {2022: 6238}),
    ("Nominal GDP", "million GHc", {2022: 610222, 2023: 850656, 2024: 1050978, 2025: 1216854, 2026: 1372186, 2027: 1548313, 2028: 1746882}),
]


def main() -> None:
    rows = []
    for indicator, unit, values in SERIES:
        for year, value in sorted(values.items()):
            rows.append(
                {
                    "country": "Ghana",
                    "year": year,
                    "period_type": "Actual" if year == 2022 else "Projection",
                    "indicator": indicator,
                    "unit": unit,
                    "value": value,
                    "source": "IMF paper.pdf - Ghana: Selected Economic and Financial Indicators, 2022-28",
                }
            )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["country", "year", "period_type", "indicator", "unit", "value", "source"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
