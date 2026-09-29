# Project Statement

## Title

Farm Water Manager

## Problem

Shared irrigation systems need a simple way to record how much water and motor time each farmer uses, charge them fairly, and see whether their crop income covers those costs. Doing this on paper is slow and error-prone.

## Objectives

1. Record water (litres) and motor hours per farmer and field.
2. Calculate each farmer's bill and the overall total.
3. Estimate profit per farmer from water used and the crop income rate.
4. Keep data safe with saving, backup, and restore.
5. Let the operator adjust prices without editing code.
6. Add a small random reward feature for engagement.

## Scope

**In scope:** a console application, plain-text storage, and configurable rates.

**Out of scope:** a graphical interface, multi-user access, networking, and real payment handling.

## Inputs and outputs

**Inputs:** farmer name, field, crop, water used in litres, motor hours, and price values.

**Outputs:** farmer table, bills, profit figures, reward percentage, and saved data files.

## Rules and assumptions

- A farmer is identified by name and field together. Adding the same pair again increases their totals and updates the crop.
- Names, fields, and crops are stored in lowercase.
- Water and motor hours must be whole, non-negative numbers.
- Bill = water * water rate + motor hours * motor rate.
- Profit = water * crop income rate - bill.
- Rewards are random from 5 to 30 percent, and 25 or more is a jackpot.
- Currency is not fixed; amounts are unit-less numbers.

## Code structure

The program is kept to five Python files: `main.py` (interface), `models.py` (data and settings), `logic.py` (calculations), `storage.py` (files), and `test_core.py` (tests).

## Improvements over the original script

- Split into focused modules instead of one long file.
- Removed the mistakes in the original: Backup overwrote the main file with the same data, Restore ignored old 4-field lines, and the water total was tracked by hand and could drift.
- Invalid input re-prompts instead of dropping back to the menu.
- Damaged data lines are skipped and reported rather than crashing the program.
- Files are written safely through a temporary file.
- Prices are saved between runs, and crop income rate is now adjustable.
- Data is saved on Ctrl+C or Ctrl+D as well as on Exit.
- Unit tests cover parsing, billing, the registry, rewards, and storage.

## Success criteria

- All menu options work without crashing on bad input.
- Bills and profits match the formulas above.
- Data survives a restart and can be restored from backup.
- Unit tests pass.

## Possible future work

- Export reports to CSV or PDF.
- Per-crop pricing.
- Delete and edit farmer records.
- Usage history by date.
