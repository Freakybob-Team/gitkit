# GitKit Repository Search, a Git API tool.
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

import urllib.request, json, pyautogui
def repoSearch():
    keyword = input("What would you like to search? ")
    try:
        with urllib.request.urlopen("https://codeberg.org/api/v1/repos/search/search?q=" + keyword) as url:
            data = json.load(url)
            print("Name of repository: " + data["full_name"])
            print("Repo URL: " + data["html_url"])
            pyautogui.press("f11")
    except Exception as e:
        print("There was an issue accessing the API! Error: " + str(e))
        print("Gitit will now exit.")
        pyautogui.press("f11")