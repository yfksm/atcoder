import sys
import os
import requests
from bs4 import BeautifulSoup
import config

CONTEST_NAME_CONF = os.path.dirname(__file__) + "/../conf/contest_name"
PROBLEM_NAME_CONF = os.path.dirname(__file__) + "/../conf/problem"
SAMPLE_INPUT_DIR  = os.path.dirname(__file__) + "/../sample_input"
SAMPLE_OUTPUT_DIR = os.path.dirname(__file__) + "/../sample_output"

LOGIN_URL = "https://atcoder.jp/login"
CONTEST_URL = "https://atcoder.jp/contests/"

with open(CONTEST_NAME_CONF) as f:
    contest_name = f.read().splitlines()[0]
    print(contest_name)

with open(PROBLEM_NAME_CONF) as f:
    problem_name = f.read().splitlines()[0]
    print(problem_name)

session = requests.session()

csrf_soup = BeautifulSoup(session.get(LOGIN_URL).text, 'lxml')
csrf_token = csrf_soup.find(attrs={'name': 'csrf_token'}).get('value')

login_info = {
    "csrf_token": csrf_token,
    "username": config.USERNAME,
    "password": config.PASSWORD
}

result = session.post(LOGIN_URL, data=login_info)
result.raise_for_status()
if result.status_code!=200:
    print("Login Failed.")
    exit(0)

load_url = CONTEST_URL + contest_name + "/tasks/" + contest_name + "_" + problem_name
html = session.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

sampleinput_elements = list(filter(lambda element: "Sample Input" in str(element), soup.select("section")))
sampleinputs = list(map(lambda element: element.find("pre").text, sampleinput_elements))

sampleoutput_elements = list(filter(lambda element: "Sample Output" in str(element), soup.select("section")))
sampleoutputs = list(map(lambda element: element.find("pre").text, sampleoutput_elements))

#サンプルケースを書き込み
for i in range(len(sampleinputs)):
    with open(SAMPLE_INPUT_DIR+"/sample"+str(i+1), mode='w') as f:
        f.write(sampleinputs[i])

    with open(SAMPLE_OUTPUT_DIR+"/expect"+str(i+1), mode='w') as f:
        f.write(sampleoutputs[i])
