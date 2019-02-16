import praw
import requests
from pathlib import Path
import os

IMAGE_STORAGE_PATH = os.getenv("REDDIT_IMAGE_STORAGE_PATH")
reddit = praw.Reddit('earthporn', user_agent='script')


def download_image(image_info):
    """
    Downloads image given an URL from a previous ingest phase
    :param image_info: Tuple containing image title and image URL
    :return: A stored image in path given
    """
    image_path = Path(f'{IMAGE_STORAGE_PATH}/{image_info[1]}.{image_info[2].split(".")[-1]}')

    if not image_path.is_file():
        with open(image_path, 'wb') as handle:
            response = requests.get(image_info[2], stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)


if __name__ == "__main__":
    for submission in reddit.subreddit('earthporn').hot(limit=10):
        download_image((submission.score, submission.title, submission.url))