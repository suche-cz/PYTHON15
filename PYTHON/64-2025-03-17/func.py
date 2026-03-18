from string import ascii_lowercase, digits


def is_username_valid(username: str):
    """
    valid if len <= 20 and len >= 3
    a nesmí obsahovat speciální znaky kromě -_ a-z 0-9
    """

    length = len(username)

    if length > 20 or length < 3:
        return False
    
    allowed_chars = set(ascii_lowercase + digits + '-_')
    username_chars = set(username)
    return allowed_chars.issuperset(username_chars)
