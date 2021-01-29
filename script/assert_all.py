import os

GREEN = "\033[32m"
YELLOW = '\033[33m'
RESET = "\033[0m"

sample_number = 1
while(os.path.isfile("./sample_output/expect" + str(sample_number))):
    expect = []
    actual = []

    try:
        with open("./sample_output/expect" + str(sample_number)) as f:
            for expect_line in f:
                expect.append(expect_line.replace("\n",""))

        with open("./sample_output/actual" + str(sample_number)) as f:
            for actual_line in f:
                actual.append(actual_line.replace("\n",""))
    except:
        print(f"{YELLOW}[Error] Please generare expect/actual outputfile before asserting.{RESET}")
        exit(0)

    try:
        print("=======")
        print("sample" + str(sample_number))
        assert(expect == actual)
        print(f"{GREEN}[OK]{RESET}")
    except:
        print(f"{YELLOW}",end="")
        print("assertion failed!!")
        print("--expect--")
        print("\n".join(expect))
        print("++actual++")
        print("\n".join(actual))
        print(f"{RESET}",end="")
    sample_number += 1
