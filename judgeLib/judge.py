from judgeLib.compile import compile
from judgeLib.file import readFile, writeFile
from judgeLib.run import run
import os


# this func return the result of judging and IO and expect of the program
def judge(file_dir: str = None, code_text: str = None, language: str = None, input_dir: str = None, answer_dir: str = None, timeLimit: float = 1.0, memoryLimit: int = 512) -> tuple[str, str | None, str | None, str | None]:
    res = ''
    fd = file_dir
    ct = code_text
    lang = language
    id = input_dir
    ad = answer_dir
    tl = timeLimit
    ml = memoryLimit

    need_delete = False
    if fd is None:
        if lang is None:
            res = 'language is needed'
        if ct is None:
            res = 'code text is needed'
        if res == '':
            fd = 'temp.' + lang
            writeFile(fd, ct)
            need_delete = True

    # compile
    if res == '':
        compileSuccess = compile(fd)
        if not compileSuccess:
            res = 'CE'

    if res == '':
        # read input and answer
        input = readFile(id)
        answer = readFile(ad)
        if input == 'Error: file not found':
            res = 'input not found'
        if answer == 'Error: file not found':
            res = 'answer not found'

    # run
    if res == '':
        print(fd)
        exe_dir = fd.split('.')[0] + '.exe'
        print('exe_dir:', exe_dir)
        if os.path.exists(exe_dir):
            output = run(exe_dir, input, tl, ml)
        else:
            print('False')
            output = 'CE'

        if output == 'TLE':
            res = 'TLE'
            output = ''
        if output == 'MLE':
            res = 'MLE'
            output = ''
        if output == 'RE':
            res = 'RE'
            output = ''
        if output == 'CE':
            res = 'CE'
            output = ''

    txt_dir = './temp.txt'
    if res == '':
        # wash the output
        writeFile(txt_dir, output)
        output = readFile(txt_dir)

        if output == answer:
            res = 'AC'
        else:
            res = 'WA'

    # clean up the file
    if os.path.exists(exe_dir):
        os.remove(exe_dir)
    if os.path.exists(fd) and need_delete:
        os.remove(fd)
    if os.path.exists(txt_dir):
        os.remove(txt_dir)

    return res, input, output, answer
