#!/usr/bin/env python3
"""Reproduce a Ghana macro dataset aligned with IMF Country Report indicators.

Inputs:
- WEO.csv (repository root)

Outputs:
- reproduced/ghana_imf_reproduction_dataset.csv (long format)
- reproduced/ghana_imf_reproduction_dataset_wide.csv (wide format)
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "WEO.csv"
OUT_LONG = ROOT / "reproduced" / "ghana_imf_reproduction_dataset.csv"
OUT_WIDE = ROOT / "reproduced" / "ghana_imf_reproduction_dataset_wide.csv"

# Indicators chosen to align with the IMF Ghana country report macro/fiscal/external discussion.
SERIES = {
    "GHA.NGDP_RPCH.A": "Real GDP growth (%)",
    "GHA.PCPIPCH.A": "Inflation, average CPI (%)",
    "GHA.PCPIEPCH.A": "Inflation, end-of-period CPI (%)",
    "GHA.GGXCNL_NGDP.A": "Overall fiscal balance (% of GDP)",
    "GHA.GGXONLB_NGDP.A": "Primary fiscal balance (% of GDP)",
    "GHA.GGR_NGDP.A": "General government revenue (% of GDP)",
    "GHA.GGX_NGDP.A": "General government expenditure (% of GDP)",
    "GHA.GGXWDG_NGDP.A": "General government gross debt (% of GDP)",
    "GHA.BCA_NGDPD.A": "Current account balance (% of GDP)",
    "GHA.NID_NGDP.A": "Gross capital formation (% of GDP)",
    "GHA.NGSD_NGDP.A": "Gross national savings (% of GDP)",
    "GHA.TX_RPCH.A": "Exports of goods and services volume growth (%)",
    "GHA.TM_RPCH.A": "Imports of goods and services volume growth (%)",
    "GHA.NGDPD.A": "Nominal GDP (US$ billions)",
}

YEARS = [str(y) for y in range(2015, 2031)]


def to_float(value: str):
    value = (value or "").strip()
    if value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def main():
    long_rows = []
    with INPUT.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("COUNTRY") != "Ghana":
                continue
            code = row.get("SERIES_CODE")
            if code not in SERIES:
                continue

            for year in YEARS:
                val = to_float(row.get(year, ""))
                if val is None:
                    continue
                long_rows.append(
                    {
                        "country": "Ghana",
                        "year": int(year),
                        "series_code": code,
                        "indicator": SERIES[code],
                        "value": round(val, 3),
                        "source_dataset": "IMF WEO 9.0.0 (via repository WEO.csv)",
                    }
                )

    long_rows.sort(key=lambda r: (r["year"], r["indicator"]))
    OUT_LONG.parent.mkdir(parents=True, exist_ok=True)

    with OUT_LONG.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "country",
                "year",
                "series_code",
                "indicator",
                "value",
                "source_dataset",
            ],
        )
        writer.writeheader()
        writer.writerows(long_rows)

    # Wide export (one row per year).
    by_year = {int(y): {"country": "Ghana", "year": int(y)} for y in YEARS}
    for row in long_rows:
        by_year[row["year"]][row["indicator"]] = row["value"]

    wide_cols = ["country", "year"] + [SERIES[c] for c in SERIES]
    with OUT_WIDE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=wide_cols)
        writer.writeheader()
        for y in sorted(by_year):
            writer.writerow(by_year[y])

    print(f"Wrote {len(long_rows)} long rows to {OUT_LONG}")
    print(f"Wrote {len(by_year)} wide rows to {OUT_WIDE}")


if __name__ == "__main__":
    main()
