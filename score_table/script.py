"""
Example Requests
----------------------
See todays' matches of your subscribed competitions:
https://api.football-data.org/v2/matches

Get all matches of the Champions League:
https://api.football-data.org/v2/competitions/CL/matches

See all upcoming matches for Real Madrid:
https://api.football-data.org/v2/teams/86/matches?status=SCHEDULED

Get all matches where Gigi Buffon was in the squad:
https://api.football-data.org/v2/players/2019/matches?status=FINISHED

Check schedules for Premier League on matchday 11:
https://api.football-data.org/v2/competitions/PL/matches?matchday=11

Get the league table for HOME matches only of Belgiums Jupiler Pro League:
https://api.football-data.org/v2/competitions/BJL/standings?standingType=HOME

See best 10 scorers of Italy's top league (scorers subresource defaults to limit=10):
https://api.football-data.org/v2/competitions/SA/scorers

"""

import json
import requests


URL = 'http://api.football-data.org/v2/'


def print_in_file(resp, file_name='output_file_from_url'):
    json_string = json.dumps(resp, indent=4)
    with open(f'{file_name}.json', 'w') as f:
        f.write(json_string)


def get_info_api(url):
    headers = {'X-Auth-Token': 'c8edaa15323f4a22811f41febf612492'}
    response = requests.request('GET', url, headers=headers).json()
    return response


def competitions(competition_id='2021'):
    url = URL + f'competitions/{competition_id}/standings'
    resp = get_info_api(url)
    table = resp['standings'][0]['table']

    return table


def teams(id='64'):  # liverpool team id = 64

    upcoming_matches = f'{URL}/teams/{id}/matches?status=SCHEDULED'
    all_matches_of_one_team = f'{URL}/teams/{id}/matches/'

    resp = get_info_api(all_matches_of_one_team)
    print_in_file(resp, file_name='all_matches_of_one_team')


def matches():  # liv vs someone
    def one_match(id=264426):
        one_match = f'{URL}/matches/{id}'
        all_matches_of_one_team = f'{URL}/teams/{id}/matches/'

        resp = get_info_api(one_match)
        print_in_file(resp, file_name='one_match')


if __name__ == "__main__":
    pass
