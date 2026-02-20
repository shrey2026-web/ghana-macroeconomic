# ghana-macroeconomic

## IMF paper reproduction (dataset)

This repository includes a lightweight reproduction dataset aligned with the macro-fiscal indicators discussed in `IMF paper.pdf` for Ghana.

### What was reproduced

Using `WEO.csv` as the source, a reproducible script builds a Ghana-focused panel (2015–2030) for core indicators typically used in the IMF country report narrative:

- Real GDP growth
- Inflation (average and end-of-period)
- Overall and primary fiscal balance (% GDP)
- Revenue and expenditure (% GDP)
- Gross public debt (% GDP)
- Current account balance (% GDP)
- Gross capital formation and national savings (% GDP)
- Export/import volume growth
- Nominal GDP (US$ billions)

### How to run

```bash
python scripts/reproduce_imf_ghana_dataset.py
```

### Outputs

- `reproduced/ghana_imf_reproduction_dataset.csv` (long format)
- `reproduced/ghana_imf_reproduction_dataset_wide.csv` (wide format)

### Notes

- The script relies only on Python standard library modules.
- This is a data reproduction/alignment artifact, not a full textual recreation of the IMF paper.


## Direct-from-paper dataset (no CSV source inputs)

To reproduce a dataset directly from `IMF paper.pdf` (table transcription, 2022–2028):

```bash
python scripts/reproduce_from_imf_paper_pdf.py
```

Output:

- `reproduced/imf_paper_ghana_selected_indicators_2022_2028.csv`
