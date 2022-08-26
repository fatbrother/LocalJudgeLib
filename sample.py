import judgeLib
import os

def useFile():
    code_path = os.path.dirname(os.path.realpath(__file__))+'/sample.c'
    input_path = os.path.dirname(os.path.realpath(__file__))+'/input.txt'
    answer_path = os.path.dirname(os.path.realpath(__file__))+'/output.txt'
    res, input, output, expected = judgeLib.judge(file_dir=code_path, input_dir=input_path, answer_dir=answer_path, timeLimit=1, memoryLimit=512)
    print('Result:', res)
    print('Input:', input)
    print('Output:', output)
    print('Expected:' ,expected)

def useText():
    with open('code.txt', 'r') as f:
        code_text = f.read()
    input_path = os.path.dirname(os.path.realpath(__file__))+'/input.txt'
    answer_path = os.path.dirname(os.path.realpath(__file__))+'/output.txt'
    res, input, output, expected = judgeLib.judge(code_text=code_text, language='c', input_dir=input_path, answer_dir=answer_path)
    print('Result:', res)
    print('Input:', input)
    print('Output:', output)
    print('Expected:' ,expected)

if __name__ == '__main__':
    useFile()
    useText()