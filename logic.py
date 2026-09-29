import random

from models import JACKPOT_THRESHOLD, REWARD_MAX, REWARD_MIN


def farmer_bill(farmer, prices):
    return farmer.water * prices.water_rate + farmer.motor_hours * prices.motor_rate


def total_bill(farmers, prices):
    return sum(farmer_bill(farmer, prices) for farmer in farmers)


def farmer_profit(farmer, prices):
    income = farmer.water * prices.crop_income_rate
    return income - farmer_bill(farmer, prices)


def draw_reward(rng=random):
    percent = rng.randint(REWARD_MIN, REWARD_MAX)
    return percent, percent >= JACKPOT_THRESHOLD
