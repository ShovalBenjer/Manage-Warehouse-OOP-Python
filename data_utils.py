def validate_phone_number(phone_number):
    if phone_number is None:
        return None

    if len(phone_number) != 11:
        return None

    if phone_number[0:2] != "05":
        return None

    if phone_number[2] != "-":
        return None

    if not phone_number[3:].isdigit():
        return None

    return phone_number


def validate_gender(gender):
    if gender is None:
        return None

    if gender.upper() not in ['M', 'F']:
        return None

    return gender
