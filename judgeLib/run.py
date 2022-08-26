import subprocess
import psutil

def run(file_dir: str, input: str, timeLimit: float, memoryLimit: int) -> str:
    try:
        # run the program
        process = subprocess.Popen(
            [file_dir], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    except subprocess.CalledProcessError:
        return 'CE'

    # calculate memory usage
    memory_usage = psutil.Process(process.pid).memory_info().rss / 1024 / 1024
    if memory_usage > memoryLimit:
        process.terminate()
        process.wait()
        return 'MLE'

    try:
        output, error = process.communicate(
            input.encode('utf-8', 'ignore'), timeout=timeLimit)
    except subprocess.TimeoutExpired:
        process.terminate()
        process.wait()
        return 'TLE'
    except subprocess.CalledProcessError:
        process.terminate()
        process.wait()
        return 'RE'

    # check if the program is something wrong
    if error:
        process.terminate()
        process.wait()
        return 'CE'

    # close the process
    process.terminate()
    process.wait()
    return output.decode('utf-8')