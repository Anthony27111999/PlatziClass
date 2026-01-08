from terceros import Check_post, Check_users

def add_post_to_user_classic():
    """
        Match user with post in jsonplaceholder
    """
    users = Check_users()
    posts = Check_post()
    result = {}
    for u in users:
        if u is not None and u.get('name') not in result:
            result[u.get('name')] = []
        for p in posts:
            if p.get('userId') == p.get('id'):
                result[u.get('name')].append(p)
    return result

def user_to_post_compehencion():
    users = Check_users()
    posts = Check_post()

    return {
        user['name']: [
            post
            for post in posts
            if post['userId'] == user['id']
        ]
        for user in users
    }