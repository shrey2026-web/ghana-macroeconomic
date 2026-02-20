# Reproduced dataset aligned to `IMF paper.pdf`

This folder contains a reproducible Ghana macroeconomic dataset constructed from `WEO.csv`.

## Files

- `ghana_imf_reproduction_dataset.csv`: long format (`country`, `year`, `series_code`, `indicator`, `value`)
- `ghana_imf_reproduction_dataset_wide.csv`: wide format (one row per year)

## Coverage

- Country: Ghana
- Years: 2015–2030
- Source: IMF WEO 9.0.0 records present in `WEO.csv`

## Indicator mapping from WEO series codes

- `GHA.NGDP_RPCH.A` → Real GDP growth (%)
- `GHA.PCPIPCH.A` → Inflation, average CPI (%)
- `GHA.PCPIEPCH.A` → Inflation, end-of-period CPI (%)
- `GHA.GGXCNL_NGDP.A` → Overall fiscal balance (% of GDP)
- `GHA.GGXONLB_NGDP.A` → Primary fiscal balance (% of GDP)
- `GHA.GGR_NGDP.A` → General government revenue (% of GDP)
- `GHA.GGX_NGDP.A` → General government expenditure (% of GDP)
- `GHA.GGXWDG_NGDP.A` → General government gross debt (% of GDP)
- `GHA.BCA_NGDPD.A` → Current account balance (% of GDP)
- `GHA.NID_NGDP.A` → Gross capital formation (% of GDP)
- `GHA.NGSD_NGDP.A` → Gross national savings (% of GDP)
- `GHA.TX_RPCH.A` → Exports of goods and services volume growth (%)
- `GHA.TM_RPCH.A` → Imports of goods and services volume growth (%)
- `GHA.NGDPD.A` → Nominal GDP (US$ billions)
