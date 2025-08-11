# GitKit, a Git API tool.
# 2025 Freakybob Team. Licensed under GPL-3.0.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Freakybob Team <freakybobsite@proton.me>
import inquirer
import urllib.request, json 
import tools.orginfo as orginfo
import tools.credits as credits
import tools.reposearch as reposearch
import pyautogui
import os
try:
    pyautogui.press("f11")
    if os.name == 'java':
        print("Gitit doesn't support Mac (Codename: Darwin, Java). Sorry!")
        quit()
    giturlreal = [
        inquirer.Text('giturl', message="You can use any Git instance that is powered by Gitea or Forgejo. What API URL would you like to use? (Codeberg is default)", default="https://codeberg.org/api/v1/")
    ]
    giturl = inquirer.prompt(giturlreal)
    giturl_answer = giturl['giturl']

    print("Welcome to Gitit, a Git API tool by Freakybob Team.")
    print("This tool uses the Codeberg API. Support for other Git APIs may be added later.")
    print("Information may take up a lot of the window. We'd like to ask you to maximize this.")
    print("To unresize, press F11!")
    select = [
        inquirer.List('selection',
                message="What action would you like to perform on the Codeberg API?",
                choices=['Get organzation information', 'Search for a repository', 'See GitKit Credits'],
            ),
    ]
    answers = inquirer.prompt(select)
    if (answers['selection'] == "Get organzation information"):
        orginfo.orgInfo(giturl_answer)
    if (answers['selection'] == "See GitKit Credits"):
        credits.creditUs()
    if (answers['selection'] == "Search for a repository"):
        reposearch.repoSearch(giturl_answer)
except Exception as e:
    print("There was an issue in GitKit and we had to close. Error: " + str(e))