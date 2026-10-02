# Repository navigation

This is a document archive, not an executable app. Start with [INDEX.md](INDEX.md) for direct reading links or [catalog.json](catalog.json) for machine-readable metadata.

- Canonical searchable reading representation: `letters-en-md/`.
- PDF copies: `letters-en-pdf/`; originals/alternate source formats: `letters-en-source/`.
- Source collections and indexes: `referance/` (the spelling is intentional in existing paths).
- `non-buffett/` contains six documents by Chace/Munger, excluded from the 91 Buffett-document total.
- Published translations/concept navigation live in [the separate vault repository](https://github.com/jayleecn/Warren-Buffett-Letters-Vault); no automatic sync is configured here.

Query one year/date with `python3 scripts/catalog.py --year 2024` or `--date 2025-02-22` instead of loading the full catalog. Use catalog fields to distinguish fiscal year from signing date and preserve month precision. Search one representation first; open source/PDF files when verification requires them. After catalog edits, run `python3 scripts/catalog.py --write`, then `python3 scripts/catalog.py --check`. The script validates local metadata/paths and generated documents, not external availability or textual accuracy.
