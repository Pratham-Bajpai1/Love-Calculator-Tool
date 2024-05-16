import random

def calculate_love_percentage(name1, name2):
    """Calculate a love percentage based on names and randomness."""
    combined_names = name1.strip().lower() + name2.strip().lower()
    random.seed(combined_names)  # Seed based on combined names for consistent results
    base_percentage = random.randint(40, 80)  
    percentage = base_percentage + random.randint(0, 20) - random.randint(0, 20)
    return percentage, get_message(percentage)

def get_message(percentage):
    """Return a personalized message based on the love percentage."""
    if percentage > 90:
        return "A match made in heaven!"
    elif percentage > 75:
        return "A great match! You two are meant for each other."
    elif percentage > 50:
        return "A good match! There's potential here."
    elif percentage > 30:
        return "An okay match. Maybe give it some time?"
    else:
        return "It might be tough, but love can conquer all!"
