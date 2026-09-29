from logic import draw_reward, farmer_bill, farmer_profit, total_bill
from models import BACKUP_FILE, DATA_FILE, SETTINGS_FILE, FarmRegistry
from storage import load_farmers, load_prices, save_farmers, save_prices

MENU = """
1 Add   
2 View   
3 Bill   
4 Profit
5 Reward   
6 Price   
7 Backup   
8 Restore   
9 Exit"""

PRICE_FIELDS = {"1": "water_rate", "2": "motor_rate", "3": "crop_income_rate"}


def ask_text(label):
    while True:
        value = input(f"{label}: ").strip().lower()
        if value:
            return value
        print("This field cannot be empty")


def ask_number(label):
    while True:
        value = input(f"{label}: ").strip()
        if value.isdigit():
            return int(value)
        print("Enter a whole number")


def ask_choice(label, valid):
    value = input(f"{label}: ").strip()
    if value in valid:
        return value
    print("Wrong choice")
    return None


class FarmApp:
    def __init__(self):
        farmers, skipped = load_farmers(DATA_FILE)
        self.registry = FarmRegistry(farmers)
        self.prices = load_prices(SETTINGS_FILE)
        self.running = True
        if skipped:
            print(f"Skipped {skipped} unreadable line(s) in {DATA_FILE.name}")

    def save(self):
        save_farmers(DATA_FILE, self.registry.farmers)

    def has_farmers(self):
        if len(self.registry) == 0:
            print("No farmers")
            return False
        return True

    def add(self):
        name = ask_text("Name")
        field = ask_text("Field")
        crop = ask_text("Crop")
        water = ask_number("Water (L)")
        hours = ask_number("Motor hours")
        print(self.registry.add_or_update(name, field, crop, water, hours))

    def view(self):
        if not self.has_farmers():
            return
        print(f"{'#':<4}{'Name':<16}{'Field':<12}{'Crop':<12}{'Water (L)':>10}{'Motor (h)':>11}")
        for index, farmer in enumerate(self.registry.farmers, 1):
            print(
                f"{index:<4}{farmer.name:<16}{farmer.field:<12}{farmer.crop:<12}"
                f"{farmer.water:>10}{farmer.motor_hours:>11}"
            )
        print("Total water:", self.registry.total_water, "L")

    def bill(self):
        if not self.has_farmers():
            return
        for farmer in self.registry.farmers:
            print(f"{farmer.name} = {farmer_bill(farmer, self.prices)}")
        print("Total:", total_bill(self.registry.farmers, self.prices))

    def profit(self):
        if not self.has_farmers():
            return
        for farmer in self.registry.farmers:
            print(f"{farmer.name} ({farmer.crop}) profit = {farmer_profit(farmer, self.prices)}")

    def reward(self):
        if not self.has_farmers():
            return
        percent, jackpot = draw_reward()
        print("Reward:", percent, "%")
        if jackpot:
            print("Jackpot!")

    def change_price(self):
        choice = ask_choice("1 Water  2 Motor  3 Crop income", PRICE_FIELDS)
        if choice is None:
            return
        value = ask_number("New price")
        setattr(self.prices, PRICE_FIELDS[choice], value)
        save_prices(SETTINGS_FILE, self.prices)
        print("Price updated")

    def backup(self):
        self.save()
        save_farmers(BACKUP_FILE, self.registry.farmers)
        print("Backup done")

    def restore(self):
        choice = ask_choice("1 Main  2 Backup", {"1", "2"})
        if choice is None:
            return
        path = DATA_FILE if choice == "1" else BACKUP_FILE
        if not path.exists():
            print("File not found")
            return
        farmers, skipped = load_farmers(path)
        self.registry.replace(farmers)
        print(f"Restored {len(farmers)} farmer(s)")
        if skipped:
            print(f"Skipped {skipped} unreadable line(s)")

    def exit(self):
        self.save()
        print("Saved")
        self.running = False

    def run(self):
        handlers = {
            "1": self.add,
            "2": self.view,
            "3": self.bill,
            "4": self.profit,
            "5": self.reward,
            "6": self.change_price,
            "7": self.backup,
            "8": self.restore,
            "9": self.exit,
        }
        try:
            while self.running:
                print(MENU)
                handler = handlers.get(input("Choice: ").strip())
                if handler:
                    handler()
                else:
                    print("Wrong choice")
        except (KeyboardInterrupt, EOFError):
            print()
            self.save()
            print("Saved")


if __name__ == "__main__":
    FarmApp().run()
