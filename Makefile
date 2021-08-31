INPUT_FILE_PATH = ./custom_input.txt
OUTPUT_FILE_PATH = ./custom_output.txt
TEMPLATE_FILE_PATH = ./template/template.cpp
PROBLEM_FILE_PATH = ./conf/problem
SCRIPT_DIR_PATH = ./script
SAMPLE_INPUT_DIR_PATH = ./sample_input
SAMPLE_OUTPUT_DIR_PATH = ./sample_output
LIB_DIR = ./lib
LIB = *
CC = g++ --std=c++14
ARG = <${INPUT_FILE_PATH}> ${OUTPUT_FILE_PATH}
PROGRAM = main

case = 1

default: ${PROGRAM} run assert

${PROGRAM}: ${PROGRAM}.cpp
	${CC} ${PROGRAM}.cpp -o ${PROGRAM}

run:
	${SCRIPT_DIR_PATH}/exec.sh 2> /dev/null

crun:${PROGRAM}
	./${PROGRAM} ${ARG}

assert:
	python3 ${SCRIPT_DIR_PATH}/assert_all.py

clear:
	cat /dev/null > ${INPUT_FILE_PATH}
	cat /dev/null > ${OUTPUT_FILE_PATH}
	cp -f ${TEMPLATE_FILE_PATH} ./${PROGRAM}.cpp

libuse:
	echo "\n\n/** added libraries by make command **/\n" >> ${PROGRAM}.cpp
	cat ${LIB_DIR}/${LIB}.cpp >> ./${PROGRAM}.cpp

a:
	echo a > ${PROBLEM_FILE_PATH}
	rm -rf ${SAMPLE_INPUT_DIR_PATH}/* ${SAMPLE_OUTPUT_DIR_PATH}/*
	python3 ${SCRIPT_DIR_PATH}/get_all_testcase.py

b:
	echo b > ${PROBLEM_FILE_PATH}
	rm -rf ${SAMPLE_INPUT_DIR_PATH}/* ${SAMPLE_OUTPUT_DIR_PATH}/*
	python3 ${SCRIPT_DIR_PATH}/get_all_testcase.py

c:
	echo c > ${PROBLEM_FILE_PATH}
	rm -rf ${SAMPLE_INPUT_DIR_PATH}/* ${SAMPLE_OUTPUT_DIR_PATH}/*
	python3 ${SCRIPT_DIR_PATH}/get_all_testcase.py

d:
	echo d > ${PROBLEM_FILE_PATH}
	rm -rf ${SAMPLE_INPUT_DIR_PATH}/* ${SAMPLE_OUTPUT_DIR_PATH}/*
	python3 ${SCRIPT_DIR_PATH}/get_all_testcase.py

e:
	echo e > ${PROBLEM_FILE_PATH}
	rm -rf ${SAMPLE_INPUT_DIR_PATH}/* ${SAMPLE_OUTPUT_DIR_PATH}/*
	python3 ${SCRIPT_DIR_PATH}/get_all_testcase.py

f:
	echo f > ${PROBLEM_FILE_PATH}
	rm -rf ${SAMPLE_INPUT_DIR_PATH}/* ${SAMPLE_OUTPUT_DIR_PATH}/*
	python3 ${SCRIPT_DIR_PATH}/get_all_testcase.py