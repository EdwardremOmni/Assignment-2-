from rest_framework import viewsets
from .models import Match
from .serializers import MatchSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

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
            minutes=fixture.get("minutes", 0),
            provisional_start_time=fixture.get("provisional_start_time", False),
            started=fixture.get("started", False),
            team_a=fixture.get("team_a"),
            team_a_score=fixture.get("team_a_score", 0),
            team_h=fixture.get("team_h"),
            team_h_score=fixture.get("team_h_score", 0),
            stats=fixture.get("stats", []),
            team_h_difficulty=fixture.get("team_h_difficulty", 0),
            team_a_difficulty=fixture.get("team_a_difficulty", 0),
            pulse_id=fixture.get("pulse_id", 0),
        )
        created += 1

    return Response({"created": created, "skipped": skipped})
