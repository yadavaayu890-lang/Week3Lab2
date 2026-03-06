def can_enrol(distance_km, age, right_to_stay, pay_international_fees):
    if distance_km < 4 and age < 18 and right_to_stay:
        return True
    elif age < 18 and pay_international_fees:
        return True
    else:
        return False