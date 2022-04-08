import requests
import re




def auth_moodle(data: dict) -> requests.Session():
    login, password, url_domain = data.values()
    s = requests.Session()
    r_1 = s.get(url=url_domain)
    pattern_auth = '<input type="hidden" name="logintoken" value="\w{32}">'
    token = re.findall(pattern_auth, r_1.text)
    token = re.findall("\w{32}", token[0])[0]
    payload = {'anchor': '', 'logintoken': token, 'username': login, 'password': password, 'rememberusername': 1}
    r_2 = s.post(url=url_domain + "/login/index.php", data=payload)
    for i in r_2.text.splitlines():
        if "<title>" in i:
            # print(i[15:-8:])
            break
    counter = 0
    for i in r_2.text.splitlines():
        if "loginerrors" in i or (0 < counter <= 3):
            counter += 1
            # print(i)
    return s


def extract_token_from_content(content):
    result = re.findall(str('>(.{32})<.*[\n\r].*Moodle\s+mobile\s+web\s+service'), str(content))
    # pattern = re.compile()
    # result = re.match(pattern, content)
    return result


def get_token_from_credentials(username, password):
    app_data = {
        "login": username,
        "password": password,
        "url": "https://moodle2.cs.huji.ac.il/nu21/login/index.php?cse=1&slevel=4"
    }
    session = auth_moodle(data=app_data)
    token_page_content = session.get(url="https://moodle2.cs.huji.ac.il/nu21/user/managetoken.php")

    token_matches_list = extract_token_from_content(str(token_page_content.text))
    if len(token_matches_list) > 0:
        return token_matches_list[0]
    raise SystemError(f"Failed to extract token for {username}")


# if __name__ == '__main__':
    # print(str(token_page_content.content))
