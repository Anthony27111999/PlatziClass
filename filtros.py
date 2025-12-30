from comprehencion import Check_users

def get_geo_classic():
    geo = set()
    users = Check_users()
    if users:
        for u in users:
            geo.add(f"""Name: {u.get('name')} -> latitud: {u.get('address').get('geo').get('lat')} longitud: {u.get('address').get('geo').get('lng')}.""")
    return geo

def get_geo_pythonic():
    users =  Check_users()
    return {f"""Name: {g.get('name')} -> latitud: {g.get('address').get('geo').get('lat')} longitud: {g.get('address').get('geo').get('lng')}."""
            for g in users if len(g.get('name')) > 3 }

