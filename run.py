import subprocess
from subprocess import PIPE, CalledProcessError

try:
    subprocess.run(["python3", "test2.py"], check=True, stdout=PIPE, stderr=PIPE)
except CalledProcessError as cpe:
    save = cpe

