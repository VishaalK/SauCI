# import docker
from yaml import load, dump

document = """
  a: 1
  b:
    c: 3
    d: 4
"""

def produce_docker_file(sauciYmlConfig):
   return "sup"

loaded = load(document)
print(loaded)