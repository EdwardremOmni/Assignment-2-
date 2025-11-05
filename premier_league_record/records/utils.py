from records.models import Match, AugustFixture

def dump_august_matches():
    august_matches = Match.objects.filter(kickoff_time__month=8)

    created, skipped = 0, 0
    for match in august_matches:

        if AugustFixture.objects.filter(code=match.code).exists():
            skipped += 1
            continue

        AugustFixture.objects.create(
            code=match.code,
            kickoff_day=match.kickoff_time.date(),
            kickoff_time=match.kickoff_time.time(),
        )
        created += 1

    return {"created": created, "skipped": skipped}
