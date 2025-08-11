# Gitit, a Git API tool.
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
print("Welcome to Gitit, a Git API tool by Freakybob Team.")
print("This tool uses the Codeberg API. Support for other Git APIs may be added later.")
select = [
  inquirer.List('selection',
                message="What action would you like to perform on the Codeberg API? Or, credits.",
                choices=['Get organzation information', 'Credits'],
            ),
]
answers = inquirer.prompt(select)
if (answers['selection'] == "Get organzation information"):
    print("What organzation would you like to see information about?")
    org_name = input()
    with urllib.request.urlopen("https://codeberg.org/api/v1/orgs/" + org_name) as url:
        data = json.load(url)
        print("Name: " + data["name"])