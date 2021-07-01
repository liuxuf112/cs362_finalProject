import math


def conv_num(num_str):
    """ Takes a string int, hex, or float, converts it to base 10, then returns it as a int or float. """
    if not type(num_str) is str:
        return None

    point_count = num_str.count('.')
    negative_count = num_str.count('-')
    negative_index = num_str.find('-')

    # Returns None if input is empty, has too many decimals/minuses, or has misplaced minus sign.
    if num_str == "" or point_count > 1 or negative_count > 1 or negative_index > 0:
        return None

    # Returns string as float
    if point_count == 1:
        return generate_float(num_str)

    # Returns string as hexadecimal
    for character in num_str:
        if character not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']:
            return generate_hex(num_str)

    # Returns string as int
    return generate_int(num_str)


def generate_int(int_string):
    """ Converts string int to int and returns it. """
    # If number is negative, strips it out before processing.
    is_negative = False
    if int_string[0] == '-':
        is_negative = True
        int_string = int_string[1:]
        # Edge case when - doesn't have another number with it.
        if int_string == "":
            return None

    # Processes string from right to left, updating integer from least to most significant digit.
    num_int = 0
    for index, value in enumerate(int_string[::-1]):
        num_int = process_character_int(index, value, num_int)
        if num_int is None:
            return None

    # Adds the negative sign back on before returning.
    if is_negative:
        return num_int * -1
    else:
        return num_int


def process_character_int(some_index, some_character, some_int):
    """ Updates given int value if character is valid int. """
    for index, digit in enumerate(range(10)):
        if some_character == str(digit):
            some_int += digit * (10 ** some_index)
            return some_int

    return None


def generate_float(float_string):
    """ Converts string float to float and returns it. """
    # If number is negative, strips it out before processing.
    is_negative = False
    if float_string[0] == '-':
        is_negative = True
        float_string = float_string[1:]
        # Edge case when - doesn't have another number with it.
        if float_string == "":
            return None

    decimal_index = float_string.index('.')
    num_float = 0.0

    # Adds left-hand-side if . is not first.
    if decimal_index != 0:
        left_hand_side = generate_int(float_string[:decimal_index])
        if left_hand_side is None:
            return None  # Edge case when the left-hand-side contains a non-digit character.
        num_float = 1.0 * left_hand_side

    # Adds right-hand-side if . is not last.
    if float_string[-1] != '.':
        for index, character in enumerate(float_string[decimal_index + 1:]):
            num_float = process_character_float(index, character, num_float)
            if num_float is None:
                return None

    # Adds the negative sign back on before returning.
    if is_negative:
        return num_float * -1.0
    else:
        return num_float


def process_character_float(some_index, some_character, some_float):
    """ Updates given float value if character is valid. """
    multiplier = 0.0
    for index, digit in enumerate(range(10)):
        if some_character == str(digit):
            some_float += multiplier * (0.1 / (10.0 ** some_index))
            return some_float
        multiplier += 1.0

    return None


def generate_hex(hex_string):
    """ Converts string hex to hex and returns it. """
    num = 0
    hex_negative = False
    hex_string = hex_string.upper()
    if hex_string.find('0X') == -1:
        return None

    if hex_string.count("X") > 1 or hex_string.count("0X") > 1:
        return None

    if "0X" in hex_string:
        hex_string = hex_string.replace("0X", "")

    if "-" in hex_string:
        hex_negative = True
        hex_string = hex_string.replace("-", "")

    if hex_string == "":
        return None

    hex = [ord(n) - 55 if n in list("ABCDEF") else ord(n) - 48 for n in hex_string]
    num = [hex[-i - 1] * math.pow(16, i) for i in range(len(hex))]
    num = sum(num)
    if hex_negative is True:
        num = num * -1
    return num


def my_datetime(num_sec):
    """ Takes an integer represents seconds elapsed since January 1st 1970. Converts seconds elapsed to a date. Returns
    date as string: MM-DD-YYYY. """
    date_month = 1
    date_year = 1970
    num_days = num_sec / (60 * 60 * 24)
    num_days = 1 + int(num_days)
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while num_days > 365:
        if not is_leap_year(date_year):  # 365 days in non-leap years
            num_days -= 365
            date_year += 1
        elif is_leap_year(date_year) and num_days > 366:  # 366 days in leap year
            num_days -= 366
            date_year += 1
        else:  # Not enough days to fill current year, stop loop
            break

    for i in range(12):  # Cycle through array
        if is_leap_year(date_year) and i == 1:  # February in leap year
            if num_days > 29:
                num_days -= 29
                date_month += 1
        elif num_days > month_lengths[i]:  # All other months
            num_days -= month_lengths[i]
            date_month += 1
        else:  # not enough days to fill another month, stop loop
            break

    return str(date_month).zfill(2) + "-" + str(num_days).zfill(2) + "-" + str(date_year)


def conv_endian(num, endian='big'):
    """ Takes an integer value and whether it should use big or little endian (defaults to big if none provided).
    Converts and returns number to hexadecimal string. Returns None if endian flag is invalid """
    if endian != "little" and endian != "big":
        return None

    # If the number is negative, flags it as negative but treats it as positive for conversion to hex.
    is_negative = False
    if num < 0:
        is_negative = True
        num *= -1

    # Converts number to list of hex characters
    hex_list = []
    while num != 0:
        remainder = num % 16

        # Converts any hex character above 9 to a letter.
        if remainder > 9:
            hex_list.insert(0, chr(ord('A') + remainder - 10))
        else:
            hex_list.insert(0, str(remainder))

        num = num // 16

    # Edge case for any amount of zeros being entered
    if len(hex_list) == 0:
        return "00"

    # If the length of the list is odd, pad an extra zero to keep data paired as two-character bytes.
    if len(hex_list) % 2 != 0:
        hex_list.insert(0, 0)

    # Builds hex string forwards or backwards depending on the endian flag
    hex_string = ""
    if endian == "little":
        hex_string = conv_little_endian(hex_list)
    else:
        hex_string = conv_big_endian(hex_list)

    # Adds a negative sign if original input number was negative.
    if is_negative:
        hex_string = "-" + hex_string

    return hex_string


def conv_little_endian(hex_list):
    """ Converts a list hex characters to the string representation in little endian order and returns it. """
    little_hex_string = ""
    hex_byte = ""
    for character in hex_list:
        # If this character would be the third in a row, inserts a space before adding the byte.
        if len(hex_byte) == 2 and len(little_hex_string) != 0:
            little_hex_string = hex_byte + ' ' + little_hex_string
            hex_byte = ""
        elif len(hex_byte) == 2 and len(little_hex_string) == 0:
            little_hex_string = hex_byte  # The first byte doesn't require a space to be added.
            hex_byte = ""
        hex_byte += str(character)

    # Adds the final byte if this is not the only byte.
    if hex_byte != "" and len(little_hex_string) != 0:
        little_hex_string = hex_byte + ' ' + little_hex_string

    return little_hex_string


def conv_big_endian(hex_list):
    """ Converts a list hex characters to the string representation in big endian order and returns it. """
    big_hex_string = ""
    pair_count = 0
    for character in hex_list:
        # If this character would be the third in a row, inserts a space before adding the character.
        if pair_count == 2:
            big_hex_string += ' '
            pair_count = 0

        big_hex_string += str(character)
        pair_count += 1

    return big_hex_string


def is_leap_year(year):
    """Determines if a year is considered a leap year. Year must be a multiple of 4
     and not a multiple of 100 (unless it is also a multiple of 400)."""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
