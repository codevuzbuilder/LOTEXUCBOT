async def get_user(user_id):
    return {"id": user_id, "banned": False}

def is_admin(user_id):
    try:
        import config
        return user_id in getattr(config, 'ADMIN_LIST', [])
    except:
        return False
