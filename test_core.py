import random
import tempfile
import unittest
from pathlib import Path

from logic import draw_reward, farmer_bill, farmer_profit, total_bill
from models import FarmRegistry, Farmer, Prices
from storage import load_farmers, load_prices, save_farmers, save_prices


class ModelTests(unittest.TestCase):
    def test_five_field_row(self):
        farmer = Farmer.from_row(["Ravi", "North", "Wheat", "100", "2"])
        self.assertEqual(farmer, Farmer("ravi", "north", "wheat", 100, 2))

    def test_legacy_four_field_row(self):
        farmer = Farmer.from_row(["ravi", "north", "100", "2"])
        self.assertEqual(farmer.crop, "unknown")

    def test_invalid_rows(self):
        with self.assertRaises(ValueError):
            Farmer.from_row(["a", "b", "x", "1"])
        with self.assertRaises(ValueError):
            Farmer.from_row(["a", "b", "c", "-1", "1"])
        with self.assertRaises(ValueError):
            Farmer.from_row(["a"])


class RegistryTests(unittest.TestCase):
    def test_add_then_update(self):
        registry = FarmRegistry()
        self.assertEqual(registry.add_or_update("ravi", "north", "wheat", 100, 2), "Added")
        self.assertEqual(registry.add_or_update("ravi", "north", "rice", 50, 1), "Updated")
        farmer = registry.find("ravi", "north")
        self.assertEqual((farmer.crop, farmer.water, farmer.motor_hours), ("rice", 150, 3))
        self.assertEqual(registry.total_water, 150)


class LogicTests(unittest.TestCase):
    def setUp(self):
        self.prices = Prices()
        self.farmer = Farmer("ravi", "north", "wheat", 100, 2)

    def test_bill(self):
        self.assertEqual(farmer_bill(self.farmer, self.prices), 330)
        self.assertEqual(total_bill([self.farmer, self.farmer], self.prices), 660)

    def test_profit(self):
        self.assertEqual(farmer_profit(self.farmer, self.prices), 4670)

    def test_reward_range(self):
        rng = random.Random(1)
        for _ in range(100):
            percent, jackpot = draw_reward(rng)
            self.assertTrue(5 <= percent <= 30)
            self.assertEqual(jackpot, percent >= 25)


class StorageTests(unittest.TestCase):
    def test_round_trip_and_bad_lines(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "farm.txt"
            save_farmers(path, [Farmer("ravi", "north", "wheat", 100, 2)])
            with path.open("a") as handle:
                handle.write("broken,line\n")
            farmers, skipped = load_farmers(path)
            self.assertEqual(len(farmers), 1)
            self.assertEqual(skipped, 1)

    def test_prices_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "settings.json"
            save_prices(path, Prices(water_rate=9))
            self.assertEqual(load_prices(path).water_rate, 9)
            self.assertEqual(load_prices(Path(tmp) / "missing.json"), Prices())


if __name__ == "__main__":
    unittest.main()
