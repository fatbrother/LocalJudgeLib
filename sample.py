import judgeLib
import os

def main():
    # find the path of the sample.c
    code_path = os.path.dirname(os.path.realpath(__file__))+'/sample.c'
    input_path = os.path.dirname(os.path.realpath(__file__))+'/input.txt'
    answer_path = os.path.dirname(os.path.realpath(__file__))+'/output.txt'
    res, input, output, expected = judgeLib.judge(file_dir=code_path, input_dir=input_path, answer_dir=answer_path, timeLimit=1, memoryLimit=512)
    print('Result:', res)
    print('Input:', input)
    print('Output:', output)
    print('Expected:' ,expected)

if __name__ == '__main__':
    main()