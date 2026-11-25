import copy
from pathlib import Path
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from compare import load, compare, validate_model
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=load(ROOT/"snapshots/2006-current.json")
        cls.b=load(ROOT/"snapshots/2006-future.json")
        cls.c=load(ROOT/"snapshots/2026-coo.json")
        cls.ab=load(ROOT/"crosswalks/current-to-future.json")
        cls.bc=load(ROOT/"crosswalks/future-to-coo.json")
    def test_records_valid(self):
        for x in (self.a,self.b,self.c): validate_model(x)
    def test_source_viewpoint_comparison_not_history(self):
        d=compare(self.a,self.b,self.ab)
        self.assertEqual(d["comparison_kind"],"same_era_different_viewpoints")
        self.assertTrue(any(x["relation"]=="abstracted_into" for x in d["crosswalk_assertions"]))
    def test_2026_coo_is_new_interpretation(self):
        d=compare(self.b,self.c,self.bc)
        self.assertEqual(d["comparison_kind"],"historical_source_to_modern_interpretation")
        self.assertTrue(any(x["relation"]=="introduced_distinction" for x in d["crosswalk_assertions"]))
    def test_false_chronological_revision_rejected(self):
        wrong=copy.deepcopy(self.ab);wrong["comparison_kind"]="chronological_model_release"
        with self.assertRaises(ValueError): compare(self.a,self.b,wrong)
    def test_missing_mapping_concept_rejected(self):
        wrong=copy.deepcopy(self.bc); wrong["mappings"][0]["to"]="COO.DOES_NOT_EXIST"
        with self.assertRaises(ValueError): compare(self.b,self.c,wrong)
    def test_copy_year_not_invented_date(self):
        wrong=copy.deepcopy(self.a); wrong["original"]["exact_creation_date"]="2006-01-01"
        with self.assertRaises(ValueError):validate_model(wrong)
if __name__=="__main__": unittest.main()
