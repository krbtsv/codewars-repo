def alphabet_war(battlefield: str) -> str:
    import re

    if '#' not in battlefield:
        return re.sub(r'[\[\]]', '', battlefield)
    expression = re.compile(r'([a-z#]*)\[([a-z]+)\](?=([a-z#]*))')
    return ''.join(char[1] if (char[0] + char[2]).count('#') < 2 else '' for char in expression.findall(battlefield))
