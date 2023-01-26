def validate_usr(username: str) -> bool:
    import re
    if len(username.split()) > 1 or len(username) < 4 or len(username) > 16:
        return False
    res = re.findall('[a-z0-9_]', username)
    return True if username == ''.join(res) else False


def validate_usr_second_solution(username: str) -> bool:
    import re
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))
