def validate_mapping(score):
    if score > 0.6:
        return "Strong Match"
    elif score > 0.4:
        return "Moderate Match"
    else:
        return "Weak Match"