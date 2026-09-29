# Farm Water Manager

A small console program that tracks how much irrigation water and motor time each farmer uses, then calculates bills, profit, and a random reward.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Run

From the project folder:

```
python main.py
```

## Menu

| Option | What it does |
|--------|--------------|
| 1 Add | Add a farmer, or add usage to an existing farmer (same name and field) |
| 2 View | List all farmers and the total water used |
| 3 Bill | Show each farmer's bill and the grand total |
| 4 Profit | Show estimated profit per farmer |
| 5 Reward | Draw a random reward percentage (25% or more is a jackpot) |
| 6 Price | Change the water rate, motor rate, or crop income rate |
| 7 Backup | Save the current data to the main file and to the backup file |
| 8 Restore | Load data from the main file or the backup file |
| 9 Exit | Save and quit |

Data is also saved if you close the program with Ctrl+C or Ctrl+D.

## Formulas

```
bill   = water_litres * water_rate + motor_hours * motor_rate
profit = water_litres * crop_income_rate - bill
```

Default rates: water 3, motor 15, crop income 50. Changed rates are saved and reloaded on the next run.

## Project layout

```
farm-water-manager/
├── main.py         menu, prompts, and program entry point
├── models.py       settings, paths, Farmer record, and FarmRegistry
├── logic.py        bill, profit, and reward calculations
├── storage.py      reading and writing data and settings files
├── test_core.py    unit tests
├── README.md
└── statement.md
```

## Data files

Created automatically in `data/`:

- `farm_data.txt` main records
- `farm_backup.txt` backup copy
- `settings.json` saved prices

Each line is `name,field,crop,water,motor_hours`. Older 4-field lines (`name,field,water,motor_hours`) still load, with the crop set to `unknown`. To keep your old data, copy your existing `farm_data.txt` into the `data/` folder before the first run.

## Tests

```
python -m unittest -v
```
