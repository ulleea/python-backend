def select_top_users_by_rate(users, top_size):
    return sorted(users, key=lambda user: user.rate, reverse=True)[:top_size]
