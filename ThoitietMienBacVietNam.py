import facebook
import requests


def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['message'])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
app_id = ""
app_secret = ""
# access_token = app_id + "|" + app_secret
access_token = ""
# Look at Bill Gates's profile for this example by using his Facebook id.
user = 'ThoitietMienBacVietNam'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts', limit = "100")

for idPost in range(0,100):
    print("POST : ", idPost)
    try:
        comments = graph.get_connections(posts['data'][idPost]['id'], 'comments', limit = "100")
    except IndexError:
        try:
            comments = graph.get_connections(posts['data'][idPost]['id'], 'comments')
        except IndexError:
            pass
    count = 0
    for i in range(0,len(comments['data'])):
        count = count + 1
        try:
            print(comments['data'][i]['message'])
            with open("ThoitietMienBacVietNam.txt", "a") as commentFile:
                commentFile.write(comments['data'][i]['message'] + "\n\n")
                commentFile.close()
            print(count)
            print(".........................")
        except IndexError:
            pass
        continue
