from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)

print(now_utc.strftime("%Y"))
print(now_utc.strftime("%m"))
print(now_utc.strftime("%d"))