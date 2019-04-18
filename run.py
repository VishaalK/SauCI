import subprocess
import docker
from subprocess import PIPE, CalledProcessError

client = docker.from_env()
client

try:
    subprocess.run(["python3", "test2.py"], check=True, stdout=PIPE, stderr=PIPE)
except CalledProcessError as cpe:
    save = cpe

