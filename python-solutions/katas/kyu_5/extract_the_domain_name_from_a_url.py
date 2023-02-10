def domain_name(url: str) -> str:
    url_spl = url.split('.')
    if url_spl[0][:3] == 'htt':
        if url_spl[0].split("//")[1] == 'www':
            return url_spl[1]
        if 'https' in url_spl[0]:
            url_spl[0] = url_spl[0][8:]
        if 'http' in url_spl[0]:
            url_spl[0] = url_spl[0][7:]
        return url_spl[0]
    if url_spl[0][:3] == 'www':
        return url_spl[1]
    else:
        return url_spl[0]


def domain_name_second_solution(url: str) -> str:
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")
    end = url.find(".")
    return url[0:end]
