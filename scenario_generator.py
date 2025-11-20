import random

def generate_random_scenario_name():
    prefixes = (
        "VT",
        "Aimerz+",
        "Avasive",
        "cAt",
        "wobin",
        "Smooth Your",
    )
    scenario_types = (
        "Air",
        "6 Sphere Hipfire Voltaic",
        "voxTS",
        "1w4ts reload",
        "ww5t reload",
        "Pasu",
        "Bounceshot",
        "Smoothbot",
        "Controlsphere",
        "Polarized Hell",
        "Ground Plaza Sparky V3",
        "skyTS",
        "psalmTS",
    )

    modifiers = (
        "30% Smaller",
        "30% Larger",
        "Static",
        "Easy",
        "Hard",
        "Fixed",
        "Perfected",
        "Goated",
        "Good Version",
        "OW",
        "Novice",
        "Intermediate",
        "Advanced",
        "no UFO no Skybots",
        "Small and Slow",
        "Precision Focus",
        "Reactive Focus",
    )

    scenario_name = f"{random.choice(prefixes)} {random.choice(scenario_types)}"

    for _ in range(random.randint(1, 5)):
        scenario_name += f" {random.choice(modifiers)}"

    return scenario_name

if __name__ == "__main__":
    for _ in range(5):
        print(generate_random_scenario_name())
