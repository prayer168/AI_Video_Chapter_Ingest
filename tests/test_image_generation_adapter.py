from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from production.image_generation.adapter import (
    AdapterBlocked,
    BlockedAdapter,
    GenerationRequest,
    TestDoubleAdapter,
    require_paid_authorization,
)


class ImageGenerationAdapterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.out = Path(self.tmp.name)
        self.request = GenerationRequest("CH01-HOMAGE-FIG-TEST", "test prompt", self.out)

    def tearDown(self):
        self.tmp.cleanup()

    def test_default_adapter_blocks_and_writes_nothing(self):
        with self.assertRaises(AdapterBlocked):
            BlockedAdapter().generate(self.request)
        self.assertEqual(list(self.out.iterdir()), [])

    def test_test_double_returns_simulation_without_fake_asset(self):
        result = TestDoubleAdapter().generate(self.request)
        self.assertEqual(result.status, "simulated")
        self.assertIsNone(result.output_path)
        self.assertIsNone(result.sha256)
        self.assertEqual(list(self.out.iterdir()), [])

    def test_paid_generation_requires_explicit_enablement_budget_and_cap(self):
        base = dict(provider="provider-x", enabled=True, budget_approved=True, max_spend_usd=1.0, estimated_cost_usd=0.5)
        for overrides in (
            {"enabled": False},
            {"budget_approved": False},
            {"max_spend_usd": 0.0},
            {"estimated_cost_usd": 1.1},
        ):
            with self.subTest(overrides=overrides), self.assertRaises(AdapterBlocked):
                require_paid_authorization(**(base | overrides))
        require_paid_authorization(**base)


if __name__ == "__main__":
    unittest.main()
