#### Python Script

_A script that searches my exported chrome bookmarks and returns one or more lines of URLs._


---
- Development Platform
    - Ubuntu 20.04.2 LTS
- IDE
    - Visual Studio Code v1.59.1
- Python3
    - v3.8.10
- External Dependencies
    - sty
    - lxml
---
### _Working out code in a virtual environment_
- *Install virtualenv*
    - sudo apt install virtualenv -y
- *Initialize project directory*
    - virtualenv -p /path/to/python Or "$(which python3)" project-name
- *Change into the project directory*
- *Activate the environment*
    - source bin/activate
- *Install environment dependencies*
    - pip3 install sty lxml
- *To deactivate the environment*
    - deactivate
### _Script Usage_
- *Install external libraries*
    - pip3 install sty lxml
- *Add script location to PATH*
    - I added if statement to ~/.profile
- *Refresh environment*
    - source ~/.profile