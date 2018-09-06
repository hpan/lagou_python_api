from models import comment_user


def get_comment_user_list(aid):
    if not aid:
        return []
    users = comment_user.find({'answerId': aid})
    data_list = []
    for item in users:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list


