from django.shortcuts import render
from django.views import generic
from .script import competitions, team_matches, team_detail, match_day_point
import wikipedia


def HomeView(request):
    table, top_scorer = competitions()
    context = {
        'table': table,
        'scorers': top_scorer
    }
    return render(request, 'stat-board/league.html', context)


class LeagueView(generic.View):
    def get(self, *args, **kwargs):
        table, top_scorer = competitions(kwargs['league_id'])
        match_day_record = dict()
        context = {
            'table': table,
            'scorers': top_scorer,
            'matchday': match_day_record,
        }

        print(match_day_record)

        return render(self.request, 'stat-board/league.html', context)


class TeamView(generic.View):
    def get(self, *args, **kwargs):
        upcoming, finished = team_matches(kwargs['team_id'])
        team = team_detail(kwargs['team_id'])
        squad = team['squad']
        wiki = wikipedia.summary(team['name'])
        context = {
            'upcoming': upcoming,
            'finished': finished,
            'squad': squad,
            'team': team,
            'wiki': wiki

        }
        return render(self.request, 'stat-board/team.html', context)


# kwargs['league_id'], i['team']['id']
