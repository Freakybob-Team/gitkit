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

import urllib.request, json 
def orgInfo():
    print("What organzation would you like to see information about?")
    org_name = input()
    try:
        with urllib.request.urlopen("https://codeberg.org/api/v1/orgs/" + org_name) as url:
            data = json.load(url)
            print("--------")
            print("ID: " + str(data["id"]))
            print("Name: " + data["name"])
            if 'data["full_name"]' in locals():
                print("Full Name;" + data["full_name"])
            else:
                print("❌: Full Name wasn't listed")
            if 'data["email"]' in locals():
                print("Email: " + data["email"])
            else:
                print("❌: Email wasn't listed")
            print("Avatar URL: " + data["avatar_url"])
            if 'data["description"]' in locals():
                print("Description: " + data["description"])
            else:
                print("❌: Descripton wasn't listed")
            if 'data["website"]' in locals():
                print("Website: " + data("website"))
            else:
                print("❌: Website wasn't listed")
            if 'data["location"]' in locals():
                print("Location: " + data["location"])
            else:
                print("❌: Location wasn't listed")
            print("Visibility: " + data["visibility"])
            print("Username: " + data["username"] + " - ⚠️  Deprecated")
            print("Gitit will now exit.")
    except Exception as e:
        print("There was an issue accessing the API! Error: " + str(e))
        print("Gitit will now exit.")