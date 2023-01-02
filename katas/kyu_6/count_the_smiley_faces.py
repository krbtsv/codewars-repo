def count_smileys(arr: list[str]) -> int:
    valid_smileys = {
        ":)": 0,
        ";)": 0,
        ":D": 0,
        ";D": 0,
        ";-D": 0,
        ";~D": 0,
        ";~)": 0,
        ";-)": 0,
        ":-)": 0,
        ":~)": 0,
        ":~D": 0,
        ":-D": 0,
    }
    for smile in arr:
        if smile in valid_smileys.keys():
            valid_smileys[smile] += 1
    return sum(valid_smileys.values())


def count_smileys_second_solution(arr: list[str]) -> int:
    valid = ":) :D :-) :-D :~) :~D ;) ;D ;-) ;-D ;~) ;~D".split()
    return sum(face in valid for face in arr)


def count_smileys_third_solution(arr: list[str]) -> int:
    smileys = []
    for s in arr:
        if len(s) == 2 and s[0] in [":", ";"] and s[-1] in [")", "D"]:
            smileys.append(s)
        elif len(s) > 2 and s[0] in [":", ";"] and s[1] in ["-", "~"] and s[-1] in [")", "D"]:
            smileys.append(s)
    return len(smileys)
