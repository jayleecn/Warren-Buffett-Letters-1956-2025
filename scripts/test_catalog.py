"""Protect navigation invariants without rewriting the document corpus."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

import catalog


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.documents = json.loads((catalog.ROOT / "catalog.json").read_text())["documents"]

    def test_all_catalogued_representations_exist(self):
        catalog.validate(self.documents)
        self.assertEqual(sum(d["primary"] for d in self.documents), 91)
        self.assertEqual(sum(not d["primary"] for d in self.documents), 6)

    def test_missing_reading_target_is_rejected(self):
        docs = copy.deepcopy(self.documents)
        docs[0]["markdown_path"] = "letters-en-md/missing/" + docs[0]["id"] + ".md"
        with self.assertRaisesRegex(ValueError, "Missing/duplicate document file"):
            catalog.validate(docs)

    def test_author_cannot_be_silently_reclassified(self):
        docs = copy.deepcopy(self.documents)
        docs[-1]["primary"] = True
        with self.assertRaisesRegex(ValueError, "Primary-author mismatch"):
            catalog.validate(docs)

    def test_month_precision_cannot_invent_a_day(self):
        docs = copy.deepcopy(self.documents)
        doc = next(d for d in docs if d["id"] == "1957_Letter_195802")
        doc["signing_date"] = "1958-02-01"
        doc["signing_date_precision"] = "day"
        with self.assertRaisesRegex(ValueError, "Filename-date mismatch"):
            catalog.validate(docs)

    def test_year_and_signing_date_are_separate_queries(self):
        script = Path(catalog.__file__)
        by_year = json.loads(subprocess.check_output([sys.executable, str(script), "--year", "2024"], text=True))
        by_date = json.loads(subprocess.check_output([sys.executable, str(script), "--date", "2025-02-22"], text=True))
        self.assertEqual(len(by_year), 2)
        self.assertEqual(len(by_date), 1)
        self.assertEqual(by_date[0]["fiscal_year"], 2024)


if __name__ == "__main__":
    unittest.main()
