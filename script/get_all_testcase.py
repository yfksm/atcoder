import sys
import os
import requests
from bs4 import BeautifulSoup

CONTEST_NAME_CONF = os.path.dirname(__file__) + "/../conf/contest_name"
PROBLEM_NAME_CONF = os.path.dirname(__file__) + "/../conf/problem"
SAMPLE_INPUT_DIR  = os.path.dirname(__file__) + "/../sample_input"
SAMPLE_OUTPUT_DIR = os.path.dirname(__file__) + "/../sample_output"

with open(CONTEST_NAME_CONF) as f:
    contest_name = f.read().splitlines()[0]
    print(contest_name)

with open(PROBLEM_NAME_CONF) as f:
    problem_name = f.read().splitlines()[0]
    print(problem_name)

load_url = "https://atcoder.jp/contests/" + contest_name + "/tasks/" + contest_name + "_" + problem_name
html = requests.get(load_url)
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
