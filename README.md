# Atrato Demo

QA Automation project for all UI and Backend testing that we can automate in order to ensure the quality of Atrato servies.

Stack: Python - pytest - Playwright and some extra libraries to get the job done.

## Getting started

### Pre requisites
Install all dependencies for development process
- Navegadores Chrome, MS Edge, Firefox, Chromium
- [Python 3.11](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K)
- [Git 2.42.0](https://git-scm.com/download/win)
- [Github Desktop](https://desktop.github.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

Install the most common chrome extensions to help us in te development process
- [SelectorsHub](https://chrome.google.com/webstore/detail/selectorshub/ndgimibanhlabgdgjcpbbndiehljcpfh)
- [Katalon Recorder (Selenium tests generator)](https://chrome.google.com/webstore/detail/katalon-recorder-selenium/ljdobmomdgdljniojadhoplhkpialdid)
- [ChroPath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo)
- [Ranorex Selocity](https://chrome.google.com/webstore/detail/ranorex-selocity/ocgghcnnjekfpbmafindjmijdpopafoe)

To make it easy for you to get started with AutoMaxi project:

1. Clone the repository.
2. Follow next commands and paste in your terminal.
```
cd atrato_demo

.\my_env\Scripts\activate

pip install -r requirements.txt

playwright install
```

#### Run test scenarios

Example:
API
```
pytest .\src\api\get_users\test_get_users.py --html=report.html --self-contained-html
```

UI
```
python -m pytest .\src\new_account\register_client.py
```
