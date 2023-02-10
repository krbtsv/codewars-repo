def strip_comments(string, markers):
    string_lst = string.split('\n')
    result_lst = []
    for substring in string_lst:
        result_substring = ''
        for char in substring:
            if char in markers:
                break
            else:
                result_substring += char
        result_lst.append(result_substring.rstrip())
    return '\n'.join(result_lst)
