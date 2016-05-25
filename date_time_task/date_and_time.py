# import time
# from datetime import datetime, timedelta, timezone
# import pytz
# import iso8601 as iso

# mydate = datetime(2015, 10, 3, 10, 23, 45)
# print(mydate)
# print(mydate.timestamp())
# print(mydate.strftime('%Y %m %S %A'))

# d1 = datetime.now()
# delta = timedelta(hours=3, seconds=50, days=4)
# result = d1 + delta
# print(result.isoformat())

# np = '2012-11-13T13:53:32'
# d1 = datetime.strptime(np, '%Y-%m-%dT%H:%M:%S')
# print(d1.second)

# zone_sofia = pytz.timezone('Europe/Sofia')
# print(zone_sofia)
# zone_berlin = pytz.timezone('Europe/Berlin')
# print(zone_berlin)

# d1 = datetime.now(tz=zone_sofia)
# d2 = datetime.now(tz=zone_berlin)

# d1_utc = pytz.UTC.normalize(d1)
# d2_utc = pytz.UTC.normalize(d2)

# print(d1.isoformat())
# print(d2.isoformat())
# print(zone_sofia.normalize(d2).isoformat())
