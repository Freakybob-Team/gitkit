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
import urllib.request
import json
import inquirer

def repoSearch():
    try:
        search_q = [
            inquirer.Text('keyword', message="What would you like to search?")
        ]
        keyword_answer = inquirer.prompt(search_q)
        keyword = keyword_answer['keyword']

        results_q = [
            inquirer.Text('count', message="How many results should be shown?", default="5")
        ]
        count_answer = inquirer.prompt(results_q)
        try:
            count = int(count_answer['count'])
            if count < 1:
                count = 1
        except ValueError:
            count = 5 

        try:
            with urllib.request.urlopen(f"https://codeberg.org/api/v1/repos/search?q={keyword}") as url:
                data = json.load(url)
                
                if "data" in data and len(data["data"]) > 0:
                    print(f"\nTop {count} results for '{keyword}':\n")
                    for i, repo in enumerate(data["data"][:count], start=1):
                        print(f"{i}. {repo['full_name']}")
                        print(f"   URL: {repo['html_url']}")
                        if 'description' in repo and repo['description']:
                            print(f"   Description: {repo['description']}")
                        print()
                else:
                    print(f"No repositories found for: {keyword}")
        except Exception as e:
            print("There was an issue accessing the API! Error: " + str(e))
            print("GitKit will now exit.")
    except Exception as e:
        print("There was an issue using the function. Error: " + str(e))
        print("GitKit will now exit.")
