import csv
import json
import os

from models import Farmer, Prices


def load_farmers(path):
    farmers = []
    skipped = 0
    if not path.exists():
        return farmers, skipped
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle):
            if not row:
                continue
            try:
                farmers.append(Farmer.from_row(row))
            except ValueError:
                skipped += 1
    return farmers, skipped


def save_farmers(path, farmers):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        for farmer in farmers:
            writer.writerow(farmer.to_row())
    os.replace(temp_path, path)


def load_prices(path):
    defaults = Prices()
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        return Prices(
            water_rate=int(raw.get("water_rate", defaults.water_rate)),
            motor_rate=int(raw.get("motor_rate", defaults.motor_rate)),
            crop_income_rate=int(raw.get("crop_income_rate", defaults.crop_income_rate)),
        )
    except (OSError, ValueError, TypeError, AttributeError):
        return defaults


def save_prices(path, prices):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "water_rate": prices.water_rate,
        "motor_rate": prices.motor_rate,
        "crop_income_rate": prices.crop_income_rate,
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
