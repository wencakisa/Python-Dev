import sys
import requests

with open('access_token.txt', 'r') as f:
    ACCESS_TOKEN = str(f.readline())

GET_POSTS_URL = 'https://graph.facebook.com/me/feed?access_token=' + ACCESS_TOKEN
POST_COMMENT_URL = 'https://graph.facebook.com/{}/comments?message={}&access_token=' + ACCESS_TOKEN


def main():
    print('. . . Collecting posts . . .')
    resp = requests.get(GET_POSTS_URL)
    posts_json = resp.json().get('data')

    post_requests = [
        post.get('id')
        for post in posts_json
        if post.get('to') is not None  # If the post is from a friend
        if post.get('comments') is None  # If there are no comments on this post
    ]

    if not post_requests:
        print('No uncommented posts found.')
        return 0

    comment = str(input('Enter a comment to post: '))

    print('. . . Posting comments . . .')

    for post_req_id in post_requests:
        requests.post(POST_COMMENT_URL.format(post_req_id, comment))

    print('Done! Commented on {} posts.'.format(len(post_requests)))

if __name__ == '__main__':
    sys.exit(main())
