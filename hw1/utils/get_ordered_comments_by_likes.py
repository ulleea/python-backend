def get_ordered_comments_by_likes(comments):
    return sorted(comments, key=lambda comment: comment.like_count, reverse=True)
