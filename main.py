import os
import time

import vk_api
from dotenv import load_dotenv

load_dotenv()

VK_API_TOKEN = os.getenv('TOKEN')
VK_GROUP_ID = os.getenv('GROUP_ID')
REPEAT_TIME = int(os.getenv('REPEAT_SECONDS'))


def run2():
    vk_session = vk_api.VkApi(token=VK_API_TOKEN)
    vk = vk_session.get_api()

    while True:
        file_in = open('ban.txt', 'r')
        ban_ls = [l.rstrip() for l in file_in]
        file_in.close()

        for ban_str in ban_ls:
            search_response = vk.wall.search(owner_id=f'-{VK_GROUP_ID}', query=ban_str)
            count = search_response['count']
            print(f'count={count}')
            if count == 0:
                continue
            ids_to_del = list(map(lambda item: item['id'], search_response['items']))
            print(ids_to_del)
            for del_id in ids_to_del:
                print(f'DELETE! id={del_id}')
                vk.wall.delete(owner_id=f'-{VK_GROUP_ID}', post_id=del_id)

        time.sleep(REPEAT_TIME)


def run1():
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()

    last_checked_id = 0
    while True:
        time.sleep(REPEAT_TIME)
        print(f'last_checked_id={last_checked_id}')
        get_response = vk.wall.get(owner_id=f'-{VK_GROUP_ID}', offset=0)
        count = get_response['count']
        print(f'count={count}')
        if count == 0:
            continue
        actual_id = get_response['items'][0]['id']
        print(f'actual_id={actual_id}')
        if actual_id <= last_checked_id:
            continue
        items = list(map(lambda item: (item['id'], item['text']), get_response['items']))
        for it in items:
            print(f'check id={it[0]} text={it[1]}')
            if it[0] > last_checked_id:
                if it[1] == 'banString':
                    print(f'DELETE! id={it[0]}')
            else:
                break
        last_checked_id = actual_id
        print(items)


if __name__ == '__main__':
    run2()

# https://oauth.vk.com/authorize?client_id=51848136&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall,groups,offline&response_type=token&v=5.199
