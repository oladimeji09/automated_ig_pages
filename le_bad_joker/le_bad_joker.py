#@auto-fold regex /./
import requests as r, pyjokes as pyjk, random, time,sys
from python_helpers import python_helper as ph
sys.path.insert(0,ph.root_fp+'ig_content_publisher/publisher')
import instagram as ig, txt_to_img as tt,json
creds = ig.ig_users.get('le_bad_joker')

def ig_id():
    token = ig.get_token(creds.get('user_name'))
    ig_id =  ig.get_ig_acc(token.get('id')).get('id')
    return ig_id

def get_joke():
    """Get random jokes"""
    headers = {'Accept': 'application/json'}
    urls= ["https://icanhazdadjoke.com","https://api.chucknorris.io/jokes/random","https://icanhazdadjoke.com"]
    resp = r.get(random.choice(urls), headers=headers).json()
    joke = resp.get('joke') or resp.get('value')
    return joke

def store_joke():
    """Check if the joke is already used then store joke to the csv file"""
    joke = random.choice([get_joke() ,pyjk.get_joke(category= 'all'),pyjk.get_joke(category= 'all')])
    with open(ph.root_fp+'automated_ig_pages/le_bad_joker/saved_jokes.txt',"r+") as file:
        contents = file.read()
        if joke not in contents:
            file.write('\n'+joke) ## NOTE: add while loop here
    return joke

def share_joke(tags= 25, subject ='comedy'):
    """Share joke to instagram"""
    joke = store_joke()
    img_url = tt.upload_img(joke,'joke',font_size=55,colour='black')
    caption = ig.ig_tags.comments()[0]
    media_id= ig.post_img_to_ig(ig_id(),img_url,caption)
    tag_comment = "\n. \n. \n. \n. \n. "+' '.join('%23'+ item for item in ig.ig_tags.tags(subject,tags)) ##add quotating for all pos.
    comment_id =ig.post_ig_media_comment(media_id,tag_comment)
    return True

def follow_and_comment(subject='comedy', tags=2, top_media=1, follow = 'Y'):
    """Comment on post with tags and follow the users"""
    ig.follow_and_comment(creds.get('user_name'), creds.get('password'),ig.ig_tags.tags(subject,tags), ig.ig_tags.comments(1)[0],top_media,
                            comment_fp = ph.root_fp+'/automated_ig_pages/le_bad_joker/deleted_comment.json',follow=follow)
<<<<<<< HEAD

# follow_and_comment(subject='comedy', tags=2, top_media=1, follow = 'Y')
=======
                            
>>>>>>> 224dc30698b4b5a955e4b80a2037ea57d8d3688c
# def unfollow_user(users = 1):
#     ig.login(creds.get('user_name'), creds.get('password'))
#     user_id = ig.user_info_by_urs(creds.get('user_name')).pk
#     unfollow_users = dict(ig.user_network(user_id, 'following', users))
#     for user in unfollow_users:
#         ig.un_follow_user(user, 'unfollow')
#         print('Unfollowed user '+ str(user))
#         time.sleep(30)
#     ig.logout()

# follow_and_comment()
