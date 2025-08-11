# GitKit Organzation Information, a Git API tool.
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

import urllib.request, json, pyautogui, inquirer

def orgInfo(giturl_answer):
    org_name = [
        inquirer.Text('orgname', message="What organization would you like to see information about?")
    ]
    org_answer = inquirer.prompt(org_name)
    org_name = org_answer['orgname']
    try:
        with urllib.request.urlopen(giturl_answer + "orgs/" + org_name) as url:
            data = json.load(url)
            print("--------")
            print("ID: " + str(data.get("id", "N/A")))
            print("Name: " + data.get("name", "N/A"))
            print("Full Name: " + data.get("full_name", "❌: Full Name wasn't listed"))
            print("Email: " + data.get("email", "❌: Email wasn't listed"))
            print("Avatar URL: " + data.get("avatar_url", "N/A"))
            print("Description: " + data.get("description", "❌: Description wasn't listed"))
            print("Website: " + data.get("website", "❌: Website wasn't listed"))
            print("Location: " + data.get("location", "❌: Location wasn't listed"))
            print("Visibility: " + data.get("visibility", "N/A"))
            print("Username: " + data.get("username", "N/A") + " - ⚠️ Deprecated")
            print("Gitit will now exit.")
            pyautogui.press("f11")
    except Exception as e:
        print("There was an issue accessing the API! Error: " + str(e))
        print("Gitit will now exit.")
        pyautogui.press("f11")