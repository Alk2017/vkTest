import os
import time

import vk_api
from dotenv import load_dotenv

load_dotenv()

VK_API_TOKEN = os.getenv('TOKEN')
VK_GROUP_ID = os.getenv('GROUP_ID')
REPEAT_TIME = int(os.getenv('REPEAT_SECONDS'))


def run():
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


if __name__ == '__main__':
    run()
