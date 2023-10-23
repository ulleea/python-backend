def filter_comments_by_author(comments, author):
    filtered=[]
    for comment in comments:
        if comment.author_id == author.id:
            filtered.append(comment.text)
    return filtered