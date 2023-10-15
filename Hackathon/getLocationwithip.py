import geocoder

g = geocoder.ip('202.40.188.218')
print(g.latlng)
# import gpsd

# gpsd.connect()
# packet = gpsd.get_current()
# print(packet.position())
