
# These are the instructions to run this test application.

1. Clone this project from Github repo to your machine.
2. Ensure that Python is installed on your machine and that python environment variable is set correctly in path.
3. Now, activate virtual environment > Goto the project folder and run command 'venv\scripts\activate.bat' in order to activate the virtual environment (for windows machines) and for linux or mac use (source venv/bin/activate)
4. install all the requirements by typing command in terminal "pip3 install -r requirements.txt"
5. with html report (pytest tests\LoginPage --url "https://weathershopper.pythonanywhere.com/" --browser chrome --html=report/report.html)
6. with allure report Run command in terminal (pytest tests\LoginPage --url "https://weathershopper.pythonanywhere.com/" --browser chrome --alluredir=allure-results/)
7. framework currently support three browser configuration namely chrome, firefox and ie xplorer (just replace the chrome with other options)
8. After test execution, please navigate to allure report directory

