from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "farm_data.txt"
BACKUP_FILE = DATA_DIR / "farm_backup.txt"
SETTINGS_FILE = DATA_DIR / "settings.json"

REWARD_MIN = 5
REWARD_MAX = 30
JACKPOT_THRESHOLD = 25
UNKNOWN_CROP = "unknown"


@dataclass
class Prices:
    water_rate: int = 3
    motor_rate: int = 15
    crop_income_rate: int = 50


@dataclass
class Farmer:
    name: str
    field: str
    crop: str
    water: int
    motor_hours: int

    @property
    def key(self):
        return (self.name, self.field)

    def to_row(self):
        return [self.name, self.field, self.crop, self.water, self.motor_hours]

    @classmethod
    def from_row(cls, row):
        cells = [cell.strip() for cell in row]
        if len(cells) == 5:
            name, field, crop, water, hours = cells
        elif len(cells) == 4:
            name, field, water, hours = cells
            crop = UNKNOWN_CROP
        else:
            raise ValueError("unexpected number of fields")
        water = int(water)
        hours = int(hours)
        if water < 0 or hours < 0:
            raise ValueError("negative values are not allowed")
        if not name or not field:
            raise ValueError("name and field are required")
        return cls(name.lower(), field.lower(), (crop or UNKNOWN_CROP).lower(), water, hours)


class FarmRegistry:
    def __init__(self, farmers=None):
        self._farmers = list(farmers or [])

    @property
    def farmers(self):
        return tuple(self._farmers)

    @property
    def total_water(self):
        return sum(farmer.water for farmer in self._farmers)

    def __len__(self):
        return len(self._farmers)

    def find(self, name, field):
        for farmer in self._farmers:
            if farmer.key == (name, field):
                return farmer
        return None

    def add_or_update(self, name, field, crop, water, motor_hours):
        existing = self.find(name, field)
        if existing:
            existing.crop = crop
            existing.water += water
            existing.motor_hours += motor_hours
            return "Updated"
        self._farmers.append(Farmer(name, field, crop, water, motor_hours))
        return "Added"

    def replace(self, farmers):
        self._farmers = list(farmers)
