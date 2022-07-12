#@auto-fold regex /./
import pandas as pd,time,requests as r,os,sys
from python_helpers import python_helper as ph
<<<<<<< HEAD
sys.path.insert(0,ph.root_fp+'ig_content_publisher/publisher')
=======
sys.path.insert(0,ph.root_fp+'ig_content_publisher/automated_ig_pages')
>>>>>>> 224dc30698b4b5a955e4b80a2037ea57d8d3688c
import instagram as ig, img_gur
creds = ig.ig_users.get('forbes_tracker')

def ig_id():
    """Get IG creds"""
<<<<<<< HEAD
    creds = ig.ig_users.get('forbes_tracker')
=======
    creds = ig.ig_users.get('top_10_billionaires')
>>>>>>> 224dc30698b4b5a955e4b80a2037ea57d8d3688c
    token = ig.get_token(creds.get('user_name'))
    ig_id =  ig.get_ig_acc(token.get('id')).get('id')
    return ig_id

def number_format(num):
    if len(str(round(round(abs(num),-2)))) >  3:
        if  len(f"{round(num,-2):,}".replace(',','.')) < 9:
            return f"{round(num,-2):,}".replace(',','.')[:4]+'B'
        elif len(f"{round(num,-2):,}".replace(',','.')) > 8:
            return f"{round(num,-2):,}".replace(',','.')[:5]+'B'
    else:
        return f"{round(num,-2):,}"[:-2]+'M'

def create_content(filename='',content_url=''):
    """Create the folder containing the content if it doesn't already exist
        The dump the pictures into the folder"""
    try:
<<<<<<< HEAD
        os.mkdir(ph.root_fp+'working_files/forbes_tracker')
    except:
        pass
    try:
        with open(ph.root_fp+'working_files/forbes_tracker/'+filename, 'wb+') as f:
=======
        os.mkdir(ph.root_fp+'working_files/top_10_billionaires')
    except:
        pass
    try:
        with open(ph.root_fp+'working_files/top_10_billionaires/'+filename, 'wb+') as f:
>>>>>>> 224dc30698b4b5a955e4b80a2037ea57d8d3688c
            f.write(r.get(content_url).content)
    except:
        pass
    return True

def request(num_rich_ppl):
    """Reuquest data from the API!"""
    headers = {
        'cookie': 'usprivacy=1---; notice_preferences=2:; notice_gdpr_prefs=0,1,2::implied,eu; euconsent-v2=BPPxXTVPPxXTVAvACBENB1CsAP_AAH_AAAAAHtJB5G5UCSFAIGpcYrlEAAACQFgIAaAAAgCAgAAACBgAIAQGAGAAIECAIAAAIBQAIAIAAABACAEABAAAAIABAAGAAAAAAAAAIAAAAAAAAAAAAAAIAAgAAAAAAEQAAAAAgAAAABIAAEAAACAAAAAAAAAAAAAAAAAAAAAAAAED2oFwAC4AKAAqABcADIAHAAPAAgABkADSAIgAigBMACeAFUALoAXwAxABkADQAH4AQgAjgBLgCjAFKALkAYYAywBzwDuAO8AfoBCACIgEWgI4AjoBOwC0AF1gMAAwIB2wFPgLQAXmAxYBlgDRQHtAAAAA.YAAAAAAAAAAA; cmapi_cookie_privacy=permit 1,2,3; cmapi_gtm_bl=',}
    baseURL = "https://www.forbes.com/forbesapi/person/rtb/0/-estWorthPrev/true.json?fields=rank,uri,personName,lastName,gender,source,industries,countryOfCitizenship,birthDate,finalWorth,estWorthPrev,imageExists,squareImage,listUri&limit={}"
    resp = r.get(baseURL.format(num_rich_ppl), headers=headers)
    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception("Query failed to run by returning code of {}, with error {}.".format(resp.status_code, resp.content))

def get_data(num_rich_ppl):
    """Returns top N richest people in the world using forbes API"""
    img_url = "https://specials-images.forbesimg.com/imageserve/{}/700x700.jpg?background=000000&{}"
    resp = request(num_rich_ppl).get('personList').get('personsLists')
    for item in resp:
        try:
            item.update({"industries" : item.get('industries')[0]})
            item.update({"birthDate":str(item.get('birthDate'))[:-3]})
            item.update({"squareImage" : img_url.format(item.get('squareImage').split('imageserve/')[1].split('/')[0],item.get('squareImage').split('?')[1])})
            img_name = str(item.get('rank'))+'_'+item.get('uri')+'.png'
<<<<<<< HEAD
            item.update({"img_path": ph.root_fp+'working_files/forbes_tracker/'+img_name})
=======
            item.update({"img_path": ph.root_fp+'working_files/top_10_billionaires/'+img_name})
>>>>>>> 224dc30698b4b5a955e4b80a2037ea57d8d3688c
            create_content(img_name,item.get('squareImage'))
            for del_item in ['bioSuppress','listUri','wealthList','familyList','lastName']:
                del item[del_item]
        except:
            continue
    return resp

def transform_data(num_rich_ppl):
    """Returns top richest people in a dataframe"""
    df = pd.json_normalize(get_data(num_rich_ppl=num_rich_ppl))
    df['%change'] = round((df.finalWorth/df.estWorthPrev-1)*100,2)
    df['$change'] = df.finalWorth-df.estWorthPrev
    ig_df = pd.DataFrame([["jeff-bezos","@jeffbezos"], ["bill-gates","@thisisbillgates"] , ["mark-zuckerberg","@zuck" ]], columns =['uri','ig_account'])
    df = df.merge(ig_df, how= 'left' ,on ='uri')
    df = df.replace(pd.NA, '')
    df = df[::-1]
    return df

<<<<<<< HEAD
def upload_media(num_rich_ppl=1):
=======
def upload_media(num_rich_ppl=3):
>>>>>>> 224dc30698b4b5a955e4b80a2037ea57d8d3688c
    """Upload all pictures instagram with caption"""
    df = transform_data(num_rich_ppl=num_rich_ppl)
    for index,row in df.iterrows():
        name = row['ig_account'] if row['ig_account']  else row['personName']
        img_url = img_gur.upload_path(row.get('img_path')).get('link')
        ranked = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        pronoun = 'His' if  row['gender']  == 'M' else 'Her'
        change = 'decreased' if  row['%change']  < 0  else 'increased'
        arrows = '👎' if  row['%change']  < 0  else '👍'
        emojis = '💘' if  row['%change']  < 0  else '💚'
        update  = 'Updated @ '+time.strftime("%d/%m/%Y %H:%M") +' GMT'

        caption  = """{0} is currently the {1} richest person in the world, with a total estimated net worth at ${2}.\n\n{3} net worth has {4} by ${5} ({6}{7}%) in the the previous 24hrs {8} \n\n{9}""".format(
        name,ranked(row['rank']),number_format(row['finalWorth']),pronoun,change, number_format(row['$change']),arrows,row['%change'], emojis, update ).replace('& family ','').replace(' 1st ', ' ')

        media_id=ig.post_img_to_ig(ig_id(),img_url,caption)
        tag_comment = "\n. \n. \n. \n. \n. "+' '.join('%23'+ item for item in ig.ig_tags.tags('money',25))
        comment_id =ig.post_ig_media_comment(media_id,tag_comment)
        print(' Uploaded image for '+str(row['rank'])+'_'+name)
        time.sleep(3)
    return True

def follow_and_comment(subject='money', tags=5, top_media=2, follow = 'N'):
    """Comment on post with tags and follow the users"""
    ig.follow_and_comment(creds.get('user_name'), creds.get('password'),ig.ig_tags.tags(subject,tags), ig.ig_tags.comments(1)[0],top_media,follow)

def unfollow_user(users = 10):
    ig.login(creds.get('user_name'), creds.get('password'))
    user_id = ig.user_info_by_urs(creds.get('user_name')).pk
    unfollow_users = dict(ig.user_network(user_id, 'following', users))
    for user in unfollow_users:
        ig.un_follow_user(user, 'unfollow')
        print('Unfollowed user '+ str(user))
<<<<<<< HEAD
    ig.logout()
# upload_media
# ig.delete_media(creds.get('user_name'), creds.get('password'),2)
=======
        time.sleep(30)
    ig.logout()

# ig.delete_media(creds.get('user_name'), creds.get('password'),47)
>>>>>>> 224dc30698b4b5a955e4b80a2037ea57d8d3688c
