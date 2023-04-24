import inquirer
from inquirer.themes import GreenPassion
from blessed import Terminal
import subprocess
import re

term = Terminal()

class Theme(GreenPassion):
  def __init__(self):
    super().__init__()
    self.List.selection_color = term.black_on_bright_green

result = subprocess.run(['nvm', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.split('\n')
lines = list(filter(None, result))

versionRegex = '\d+\.\d+\.\d+'

versions = []
for line in lines:
  version = re.findall(versionRegex, line)[0]
  if '*' in line:
    current = version
  else:
    versions.append(version)

print('Current versions: ' + current)

questions = [
  inquirer.List('version',
                message="Select the version you wish to switch to",
                choices=versions,
            ),
]
v = inquirer.prompt(questions, theme=Theme())

if v is not None:
  result = subprocess.run(['nvm', 'use', v['version']], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

  if result.returncode == 0:
    print('Successfully changed to version ' + v['version'])
  else:
    print(result.stderr)