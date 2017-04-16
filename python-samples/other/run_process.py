import subprocess
import time

start = time.time()
process = subprocess.run(['python', '--version'], stderr=subprocess.STDOUT)
end = time.time()

seconds = (end - start) / 1000
exitcode = process.returncode

print()
print(f'Process return {exitcode} ({hex(exitcode)})   execution time: {seconds:.03f} s')
subprocess.call("pause",shell=True)
