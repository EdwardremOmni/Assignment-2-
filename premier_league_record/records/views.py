from rest_framework import viewsets
from .models import Match
from .serializers import MatchSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.utils.dateparse import parse_datetime
from datetime import datetime, timezone
from .models import AugustFixture
from .serializers import AugustFixtureSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import dump_august_matches

class AugustFixtureViewSet(viewsets.ModelViewSet):
    queryset = AugustFixture.objects.all()
    serializer_class = AugustFixtureSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

@api_view(["POST"])
def import_fixtures(request):
    url = "https://fantasy.premierleague.com/api/fixtures/"
    response = requests.get(url)
    if response.status_code != 200:
        return Response({"error": "Failed to fetch data"}, status=500)

    fixtures = response.json()
    created, skipped = 0, 0

    for fixture in fixtures:
        code = fixture.get("code")
        if not code:
            continue

        if Match.objects.filter(code=code).exists():
            skipped += 1
            continue

        Match.objects.create(
            code=fixture["code"],
            event=fixture.get("event"),
            finished=fixture.get("finished", False),
            finished_provisional=fixture.get("finished_provisional", False),
            kickoff_time=fixture.get("kickoff_time"),
            minutes=fixture.get("minutes") or 0,
            provisional_start_time=fixture.get("provisional_start_time", False),
            started=fixture.get("started", False),
            team_a=fixture.get("team_a"),
            team_a_score=fixture.get("team_a_score") if fixture.get("team_a_score") is not None else 0,
            team_h=fixture.get("team_h"),
            team_h_score=fixture.get("team_h_score") if fixture.get("team_h_score") is not None else 0,
            stats=fixture.get("stats", []),
            team_h_difficulty=fixture.get("team_h_difficulty", 0),
            team_a_difficulty=fixture.get("team_a_difficulty", 0),
            pulse_id=fixture.get("pulse_id", 0)
        )
        created += 1

    return Response({"created": created, "skipped": skipped})


@api_view(["GET"])
def august_fixtures(request):
    matches = Match.objects.all()
    august_list = []

    for match in matches:
        kickoff = match.kickoff_time
        if kickoff and kickoff.month == 8:  # Month of  August
            august_list.append({
                "code": match.code,
                "kickoff_day": kickoff.strftime("%Y-%m-%d"),
                "kickoff_time": kickoff.strftime("%H:%M:%S"),
            })

    return Response(august_list)


@api_view(["POST"])
def dump_august(request):
    
    result = dump_august_matches()
    return Response(result)