import argparse
import random


dark_souls_1_bosses_list = [
    "Asylum Demon",
    "Bell Gargoyle",
    "Capra Demon",
    "Ceaseless Discharge",
    "Centipede Demon",
    "Chaos Witch Quelaag",
    "Crossbreed Priscilla",
    "Dark Sun Gwyndolin",
    "Demon Firesage",
    "Four Kings",
    "Gaping Dragon",
    "Great Grey Wolf Sif",
    "Gwyn Lord of Cinder",
    "Iron Golem",
    "Moonlight Butterfly",
    "Nito",
    "Ornstein and Smough",
    "Pinwheel",
    "Seath the Scaleless",
    "Stray Demon",
    "Taurus Demon",
    "The Bed of Chaos",
]


dark_souls_2_bosses_list = [
    "The Last Giant",
    "The Pursuer",
    "Executioner's Chariot",
    "Looking Glass Knight",
    "The Skeleton Lords",
    "Flexile Sentry",
    "Lost Sinner",
    "Belfry Gargoyles",
    "Ruin Sentinel",
    "Royal Rat Vanguard",
    "Royal Rat Authority",
    "Scorpioness Najka",
    "The Duke's Dear Freja",
    "Mytha, the Baneful Queen",
    "The Rotten",
    "Old Dragonslayer",
    "Covetous Demon",
    "Smelter Demon",
    "Old Iron King",
    "Guardian Dragon",
    "Demon of Song",
    "Velstadt, the Royal Aegis",
    "Vendrick",
    "Darklurker",
    "Dragonrider",
    "Twin Dragonrider",
    "Prowling Magus and Congregation",
    "Giant Lord",
    "Ancient Dragon",
    "Throne Watcher and Throne Defender",
    "Nashandra",
    "Aldia, Scholar of the First Sin",
    "Elana, Squalid Queen",
    "Sinh, the Slumbering Dragon",
    "Graverobber, Varg, and Cerah",
    "Smelter Demon",
    "Fume Knight",
    "Sir Alonne",
    "Burnt Ivory King",
    "Aava, the King's Pet",
    "Lud and Zallen, the King's Pets",
]


dark_souls_3_bosses_list = [
    "Iudex Gundyr",
    "Vordt of the Boreal Valley",
    "Crystal Sage",
    "Deacons of the Deep",
    "Abyss Watchers",
    "High Lord Wolnir",
    "Pontiff Sulyvahn",
    "Aldrich, Devourer of Gods",
    "Yhorm the Giant",
    "Dancer of the Boreal Valley",
    "Dragonslayer Armour",
    "Lorian, Elder Prince and Lothric, Younger Prince",
    "Soul of Cinder",
    "Sister Friede",
    "Demon Prince",
    "Halflight, Spear of the Church",
    "Slave Knight Gael",
    "Curse-rotted Greatwood",
    "Old Demon King",
    "Oceiros, the Consumed King",
    "Champion Gundyr",
    "Ancient Wyvern",
    "The Nameless King",
    "Champion's Gravetender and Gravetender Greatwolf",
    "Darkeater Midir",
]


# Get dark souls help.
def show_dark_souls_summary():
    ds_1_count = len(dark_souls_1_bosses_list)
    ds_2_count = len(dark_souls_2_bosses_list)
    ds_3_count = len(dark_souls_3_bosses_list)
    ds_total_count = ds_1_count + ds_2_count + ds_3_count
    print("Dark Souls Boss Summary")
    print(f"\tDark Souls 1 Bosses stored: {ds_1_count}")
    print(f"\tDark Souls 2 Bosses stored: {ds_2_count}")
    print(f"\tDark Souls 3 Bosses stored: {ds_3_count}")
    print(f"\tTotal Dark Souls Bosses stored: {ds_total_count}")


# Get dark souls boss.
def print_dark_souls_boss(quantity, dark_souls):
    # Get dark souls list.
    bosses_list = []
    if dark_souls in ["all", "1"]:
        bosses_list += dark_souls_1_bosses_list
    if dark_souls in ["all", "2"]:
        bosses_list += dark_souls_2_bosses_list
    if dark_souls in ["all", "3"]:
        bosses_list += dark_souls_3_bosses_list

    # Get dark souls bosses.
    random.shuffle(bosses_list)
    
    # If quantity is -1, set to bosses list size.
    if quantity == -1:
        quantity = len(bosses_list)

    # Iterate from 0 to quantity to show dark souls bosses.
    for boss in bosses_list[:quantity]:
        print(boss)


# Main functionality.
if __name__ == '__main__':
    # Parse arguments.
    parser = argparse.ArgumentParser(description="Get dark souls boss name")
    parser.add_argument("-q", "--quantity", default=1, type=int,
                        help="The number of returned bosses, -1 to show all")
    parser.add_argument("-ds", "--dark_souls", default='all', choices=["all", "1", "2", "3"],
                        help="Dark souls games where boss is selected randomly")
    parser.add_argument("-s", "--summary", action='store_true',
                        help="Show dark souls bosses summary")
    args = parser.parse_args()


    # If summary, just show summary 
    if args.summary:
        show_dark_souls_summary()
    # Else, show dark souls boss.
    else:
        print_dark_souls_boss(args.quantity, args.dark_souls)
