# Supplement Formula Wars — first working project slice

**Goal:** Use Python to fetch a real dietary supplement label from NIH's Dietary Supplement Label Database (DSLD) and preserve its original JSON locally. This is the first step toward a Snowflake raw layer and dbt models.

## Run

1. Install Python 3.10+ if not already installed.
2. Open a terminal in this folder.
3. Run:

   ```bash
   python src/ingest_label.py --label-id 82118
   ```

   On Windows, if `python` does not work, try `py` instead.

4. Confirm that `data/raw/label_82118.json` exists and contains `id`, `servingSizes`, and `ingredientRows`.

This uses only Python's standard library: no `pip install`, no credentials, and no Snowflake credits required.

## Optional second label

Once the first request works, try:

```bash
python src/ingest_label.py --label-id 322544
```

This is a previously identified pre-workout label ID; if it is unavailable via the API, use the first one and tell your mentor the exact error.

## Project notes

- Source: NIH ODS Dietary Supplement Label Database — https://dsld.od.nih.gov/api-guide
- This starter downloads **one record at a time**, rather than the entire NIH database.
- `data/raw/*.json` is gitignored for now to avoid committing large source data files.
- The stored JSON is a source snapshot, not proof that product label claims are accurate.
- Next vertical slice: inspect the saved JSON; then load raw JSON into Snowflake, and use dbt to create a small model.

## Next engineering improvements (you will implement)

- Capture ingestion metadata and source checksums.
- Write tests for the source parser and for repeatable loads.
- Discover and ingest a targeted cohort of pre-workout labels.
- Handle pagination, API retry limits, and historical changes.
