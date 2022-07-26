from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from datetime import datetime
import telegram
import praw
import telepot
import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes
import pandas as pd

TOKEN = "5504082893:AAE8pwBiV5asOc1432F4RPma5TWABhJPhHg"
updater = Updater("5504082893:AAE8pwBiV5asOc1432F4RPma5TWABhJPhHg", use_context = True)
bot = telegram.Bot(token = "5504082893:AAE8pwBiV5asOc1432F4RPma5TWABhJPhHg")
helper_count=0
start_count=0
meme_count=0
vmeme_count=0
joke_count=0
policy_count=0
post_count=0
search_count=0
help_count=0
user_list={}
user_df=pd.read_csv('users.csv', encoding = "ISO-8859-1")
ad="To buy advertisement on our services contact @the_modern_prometheus \n\n Note : Your advertisement musta adhere to our /policy"

policy = """Your advertisement must adhere to the following :-

✔ Your ad must not contain any sexual explicit information.

✔ Your advertisment must not be scammy in nature.

✔ You can have at most 1 image/GIF/video file as an ad on our services.

✔ The owner in responsible for any misunderstandings aroused due to the ad and bot is not accountable in any scenario.

"""


def update_block_user():
    d={'152007083':'Cuz you are a piece of sh*t','818576063':'abbey chal na spammer ke 14','1120142014':'bbey chal na spammer ke 14',
       '1875914636':'abbey chal na spammer ke 14'}
    return d

blocked_user=update_block_user()

active_sessions={}

def generate_link():
    global active_sessions
    while True:
        comb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-', '_', '+', '=', ':', '?', '*','1','2','3','4','5','6','7','8','9','0']
        s1 = random.randint(0,len(comb)-1)
        s2 = random.randint(0,len(comb)-1)
        s3 = random.randint(0,len(comb)-1)
        s4 = random.randint(0,len(comb)-1)
        s5 = random.randint(0,len(comb)-1)
        s6 = random.randint(0,len(comb)-1)
        string = comb[s1] + comb [s2] + comb[s3] + comb [s4] + comb[s5] + comb [s6]
        if string  not in active_sessions:
            break
    return string

def assign_link(user_id):
    global active_sessions
    link = generate_link()
    active_sessions[link]=[]
    return link


def start(update: Update, context: CallbackContext):
    global start_count
    global blocked_user
    global ad
    global user_list
    global user_df
    
    z=random.randint(1,2)
    user = update.message.from_user
    
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])
        
        if user_id not in list(user_df.userID):
            user_df.loc[len(user_df.index)] = [user_id, update.message.chat_id, first_name]
        else:
            user_df=user_df
            
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]\
                                
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        start_count+=1
        
        update.message.reply_text(
            "So finally you found me, I can help you browse over reddit from telegram itself using my user friendly interface. \nHit /help to know all my commands")

        update.message.reply_text(ad)
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0
        z=1
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad1.jpg", 'rb'), caption=ad_msg1+ad_msg12+ad_msg13, parse_mode='html')
            ad_status='ad shown'
            #ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            #ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        print(str(now) +", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(start_count) + ", Command: '/start" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")

def policy_msg(update: Update, context: CallbackContext):
    
    global policy
    global policy_count
    global blocked_user
    global user_list
    global user_df
    
    z=random.randint(1,2)
    user = update.message.from_user
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        update.message.reply_text(policy)
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])

        if user_id not in list(user_df.userID):
            user_df.loc[len(user_df.index)] = [user_id, update.message.chat_id, first_name]
        else:
            user_df=user_df
        
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        policy_count+=1
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0
        z=1
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad1.jpg", 'rb'), caption=ad_msg1+ad_msg12+ad_msg13, parse_mode='html')
            ad_status='ad shown'
            #ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            #ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        
        print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(policy_count) + ", Command: '/policy" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")

def post_get(sub, cat):
    reddit=praw.Reddit(client_id='m4ome4-BWHCTubwpoMXs_A',
                   client_secret='2Md4F_mp6r4-6O5SZMYoeR3x5Y0vDA',
                   user_agent='meme-collector')

    #s=reddit.subreddits.search_by_name('programmer')

    subreddit = reddit.subreddit(sub)
    
    if cat=='hot':
        posts = subreddit.hot(limit=50)
    elif cat=='top':
        posts = subreddit.top(limit=50)
    elif cat=='rising':
        posts = subreddit.rising(limit=50)
    elif cat=='new':
        posts = subreddit.new(limit=50)
        
    final=[]
    post_urls=[]
    titles=[]
    texts=[]
    pl=[]

    
    for post in posts:
        
        if ('.gif' not in str(post.url.encode('utf-8'))) and ('.jpg' not in str(post.url.encode('utf-8'))) and ('.png' not in str(post.url.encode('utf-8'))) and ('.jpeg' not in str(post.url.encode('utf-8'))) and ('v.redd.it' not in str(post.url.encode('utf-8'))) and ('i.redd.it' not in str(post.url.encode('utf-8'))):
            texts.append(post.selftext)
        else:
            post_urls.append(post.url.encode('utf-8'))
        titles.append(post.title)
        pl.append("https://www.reddit.com" + post.permalink)

    if post_urls!=[]:
        for index, url in enumerate(post_urls):
            final.append(url)
    else:
        final=final
        
    final2=[]
    if final!=[]:
        for i in final:
            i=str(i)
            f=''
            l=list(i)
            l.remove(l[0])
            l.remove(l[0])
            l.remove(l[len(l)-1])
            for i in l:
                f+=i
            if "v.redd.it" in f and ".gif" not in f:
                f=f+"/DASH_360.mp4"
            else:
                f=f
            final2.append(f)
    else:
        final2=final2
        

    all_the_posts=[]
    if final2!=[]:
        for z2 in range(len(final2)):
            all_the_posts.append(final2[z2]+'////'+titles[z2]+'////'+pl[z2])
    else:
        for z2 in range(len(texts)):
            all_the_posts.append(texts[z2]+'////'+titles[z2]+'////'+pl[z2])
        
    return all_the_posts

def get_text(context):
    k = context.args
    y = ""
    try:
        if k==0:
            y=""
        else:
            for i in k:
                y=y+" "+i
            z=y.strip()
            y=z
        return y
    except Exception as e:
        print(str(e))
        return ""
        
#print(post_get('funnyvideos', 'top'))

def helper(update: Update, context: CallbackContext):
    global user_df
    global help_count
    global blocked_user
    global user_list
    z=random.randint(1,2)
    user = update.message.from_user
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])

        if user_id not in list(user_df.userID):
            user_df.loc[len(user_df.index)] = [user_id, update.message.chat_id, first_name]
        else:
            user_df=user_df
        
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        help_count+=1
        update.message.reply_text("You can browse through various subreddits of reddit using this bot \nFirstly search the subreddit with the command \n                         <code>/search</code> <i> {subreddit's name} </i> \n\nThen select the subreddit from the result dropdown and you are done!!", parse_mode='html')
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0
        z=1
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad1.jpg", 'rb'), caption=ad_msg1+ad_msg12+ad_msg13, parse_mode='html')
            ad_status='ad shown'
            #ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            #ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(help_count) + ", Command: '/help" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")


def searcher(update: Update, context: CallbackContext):
    global user_df
    global search_count
    global blocked_user
    global user_list
    
    user = update.message.from_user
    user_id=user['id']
    link=assign_link(user_id)
    
    y=get_text(context)

    reddit=praw.Reddit(client_id='m4ome4-BWHCTubwpoMXs_A',
                   client_secret='2Md4F_mp6r4-6O5SZMYoeR3x5Y0vDA',
                   user_agent='meme-collector')

    res=reddit.subreddits.search_by_name(y)
    names=[]
    
    for i in res:
        names.append(i.display_name)

    keyboard=[]
    for i in names:
        keyboard.append([InlineKeyboardButton(text=i, callback_data="sub////"+i+'////'+link)])
        
    reply_markup=InlineKeyboardMarkup(keyboard)
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])
        
        if user_id not in list(user_df.userID):
            user_df.loc[len(user_df.index)] = [user_id, update.message.chat_id, first_name]
        else:
            user_df=user_df
            
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]\
                                
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        
        update.message.reply_text("Subreddits according to your search are listed below", reply_markup=reply_markup)
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0
        z=1
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad1.jpg", 'rb'), caption=ad_msg1+ad_msg12+ad_msg13, parse_mode='html')
            ad_status='ad shown'
            #ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            #ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(search_count) + ", Command: '/search" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")


def queryHandler(update: Update, context: CallbackContext):
    global active_sessions
    global post_count
    global user_df
    global user_list
    
    query=update.callback_query
    data=query.data
    user = update.callback_query.from_user
    first_name=str(user['first_name'])
    last_name=str(user['last_name'])
    user_name=str(user['username'])
    user_id=str(user['id'])
        
    if user_id not in list(user_df.userID):
        user_df.loc[len(user_df.index)] = [user_id, update.message.chat_id, first_name]
    else:
        user_df=user_df
            
    if user_id not in user_list:
        user_list[user_id]=0
    else:
        user_list[user_id]=user_list[user_id]\
                                
    is_bot=str(user['is_bot'])
    language_code=str(user['language_code'])
    now = datetime.now()
    
    if 'sub' in data:
        l=data.split('////')
        link=l[2]
        active_sessions[link].append(l[1])
        active_sessions[link].append('hot')
        active_sessions[link].append(0)
        info=active_sessions[link]
        sub=info[0]
        cat=info[1]
        z=info[2]
        posts=post_get(sub, cat)
        
        active_sessions[link].append(posts)
        post=posts[z]
        post_data=post.split('////')
        #print(posts)
        if '.jpg' in post_data[0] or '.png' in post_data[0] or '.jpeg' in post_data[0]:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            try:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=post_data[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                
                bot.send_photo(chat_id=query.message.chat_id, photo=post_data[0], caption=post_data[1], reply_markup=reply_markup)
            except:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=posts[z+1].split('////')[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                active_sessions[link][2]+=1
                if '.jpg' in posts[z+1].split('////')[0] or '.png' in posts[z+1].split('////')[0] or '.jpeg' in posts[z+1].split('////')[0]: 
                    
                    bot.send_photo(chat_id=query.message.chat_id, photo=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                elif '.mp4' in posts[z+1].split('////')[0] or '.gif' in posts[z+1].split('////')[0]:
                    
                    bot.send_document(chat_id=query.message.chat_id, document=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                else:
                    
                    bot.send_message(chat_id=query.message.chat_id, text=post_data[1]+'\n\n'+post_data[0], reply_markup=reply_markup)
                    
        elif '.mp4' in post_data[0] or '.gif' in post_data[0]:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            try:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=post_data[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                
                bot.send_document(chat_id=query.message.chat_id, document=post_data[0], caption=post_data[1], reply_markup=reply_markup)
            except:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=posts[z+1].split('////')[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                active_sessions[link][2]+=1
                if '.jpg' in posts[z+1].split('////')[0] or '.png' in posts[z+1].split('////')[0] or '.jpeg' in posts[z+1].split('////')[0]: 
                    
                    bot.send_photo(chat_id=query.message.chat_id, photo=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                elif '.mp4' in posts[z+1].split('////')[0] or '.gif' in posts[z+1].split('////')[0]:
                    
                    bot.send_document(chat_id=query.message.chat_id, document=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                else:
                    
                    bot.send_message(chat_id=query.message.chat_id, text=post_data[1]+'\n\n'+post_data[0], reply_markup=reply_markup)
        else:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            try:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=post_data[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                
                bot.send_message(chat_id=query.message.chat_id, text=post_data[1]+'\n\n'+post_data[0], reply_markup=reply_markup)
            except:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=posts[z+1].split('////')[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                active_sessions[link][2]+=1
                if '.jpg' in posts[z+1].split('////')[0] or '.png' in posts[z+1].split('////')[0] or '.jpeg' in posts[z+1].split('////')[0]: 
                    
                    bot.send_photo(chat_id=query.message.chat_id, photo=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                elif '.mp4' in posts[z+1].split('////')[0] or '.gif' in posts[z+1].split('////')[0]:
                    
                    bot.send_document(chat_id=query.message.chat_id, document=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                else:
                    
                    bot.send_message(chat_id=query.message.chat_id, text=post_data[1]+'\n\n'+post_data[0], reply_markup=reply_markup)

                    
        if active_sessions[link][2] < 48:
            active_sessions[link][2]+=1
            post_count+=1
            user_list[user_id]+=1
            if user_id in user_list:
                fre=user_list[user_id]
            else:
                fre=0
            z=1
            if fre>=4 and z==1:
                user_list[user_id]=0
                #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad1.jpg", 'rb'), caption=ad_msg1+ad_msg12+ad_msg13, parse_mode='html')
                ad_status='ad shown'
                #ad_msg1_count+=1
            elif fre>=4 and z==2:
                user_list[user_id]=0
                #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
                ad_status='ad shown'
                #ad_msg2_count+=1
            else:
                user_list[user_id]=user_list[user_id]
                ad_status='not now'
            print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(post_count) + ", Command: '/sub" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")
        else:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            bot.send_message(chat_id=user_id, text='Limit reached!! Go out and touch some grass')

    elif 'nxt_post' in data:
        link=data.split('////')[1]
        info=active_sessions[link]
        sub=info[0]
        cat=info[1]
        posts=info[3]
        z=info[2]
        post=posts[z]
        post_data=post.split('////')
        keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
               InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
               InlineKeyboardButton(text='Source', url=post_data[2])]]
    
        reply_markup=InlineKeyboardMarkup(keyboard)
        if '.jpg' in post_data[0] or '.png' in post_data[0] or '.jpeg' in post_data[0]:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            try:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=post_data[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                
                bot.send_photo(chat_id=user_id, photo=post_data[0], caption=post_data[1], reply_markup=reply_markup)
            except:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=posts[z+1].split('////')[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                active_sessions[link][2]+=1
                if '.jpg' in posts[z+1].split('////')[0] or '.png' in posts[z+1].split('////')[0] or '.jpeg' in posts[z+1].split('////')[0]: 
                    
                    bot.send_photo(chat_id=query.message.chat_id, photo=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                elif '.mp4' in posts[z+1].split('////')[0] or '.gif' in posts[z+1].split('////')[0]:
                    
                    bot.send_document(chat_id=query.message.chat_id, document=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                else:
                    
                    bot.send_message(chat_id=query.message.chat_id, text=post_data[1]+'\n\n'+post_data[0], reply_markup=reply_markup)
        elif '.mp4' in post_data[0] or '.gif' in post_data[0]:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            try:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=post_data[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                
                bot.send_document(chat_id=query.message.chat_id, document=post_data[0], caption=post_data[1], reply_markup=reply_markup)
            except:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=posts[z+1].split('////')[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                active_sessions[link][2]+=1
                if '.jpg' in posts[z+1].split('////')[0] or '.png' in posts[z+1].split('////')[0] or '.jpeg' in posts[z+1].split('////')[0]:
                    
                    bot.send_photo(chat_id=query.message.chat_id, photo=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                elif '.mp4' in posts[z+1].split('////')[0] or '.gif' in posts[z+1].split('////')[0]:
                    
                    bot.send_document(chat_id=query.message.chat_id, document=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                else:
                    
                    bot.send_message(chat_id=query.message.chat_id, text=post_data[1]+'\n\n'+post_data[0], reply_markup=reply_markup)
        else:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            try:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=post_data[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                bot.send_message(chat_id=query.message.chat_id, text=post_data[1]+'\n\n'+post_data[0], reply_markup=reply_markup)
            except:
                keyboard=[[InlineKeyboardButton(text='Next', callback_data='nxt_post////'+link),
                   InlineKeyboardButton(text='Sort by category', callback_data='cat////'+link),
                   InlineKeyboardButton(text='Source', url=posts[z+1].split('////')[2])]]
    
                reply_markup=InlineKeyboardMarkup(keyboard)
                active_sessions[link][2]+=1
                if '.jpg' in posts[z+1].split('////')[0] or '.png' in posts[z+1].split('////')[0] or '.jpeg' in posts[z+1].split('////')[0]:
                    
                    bot.send_photo(chat_id=query.message.chat_id, photo=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                elif '.mp4' in posts[z+1].split('////')[0] or '.gif' in posts[z+1].split('////')[0]:
                    
                    bot.send_document(chat_id=query.message.chat_id, document=posts[z+1].split('////')[0], caption=posts[z+1].split('////')[1], reply_markup=reply_markup)
                else:
                    
                    bot.send_message(chat_id=query.message.chat_id, text=post_data[1]+'\n\n'+post_data[0], reply_markup=reply_markup)

        if active_sessions[link][2] < 48:
            active_sessions[link][2]+=1
            post_count+=1
            user_list[user_id]+=1
            if user_id in user_list:
                fre=user_list[user_id]
            else:
                fre=0
            z=1
            if fre>=4 and z==1:
                user_list[user_id]=0
                #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad1.jpg", 'rb'), caption=ad_msg1+ad_msg12+ad_msg13, parse_mode='html')
                ad_status='ad shown'
                #ad_msg1_count+=1
            elif fre>=4 and z==2:
                user_list[user_id]=0
                #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
                ad_status='ad shown'
                #ad_msg2_count+=1
            else:
                user_list[user_id]=user_list[user_id]
                ad_status='not now'
            print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(post_count) + ", Command: '/nxt" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")

        else:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            bot.send_message(chat_id=user_id, text='Limit reached!! Go out and touch some grass')

    elif 'cat' in data and 'category' not in data:
        link=data.split('////')[1]
        keyboard=[[InlineKeyboardButton(text='Hot', callback_data='category////hot////'+link)],
                  [InlineKeyboardButton(text='Top', callback_data='category////top////'+link)],
                  [InlineKeyboardButton(text='New', callback_data='category////new////'+link)],
                  [InlineKeyboardButton(text='Rising', callback_data='category////rising////'+link)]]
        
        reply_markup=InlineKeyboardMarkup(keyboard)
        try:
            query.edit_message_text(text='Select any one the categories from below', reply_markup=reply_markup)
        except:
            bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            bot.send_message(chat_id=user_id, text='Select any one the categories from below', reply_markup=reply_markup)
            

    elif 'category' in data:
        link=data.split('////')[2]
        new_cat=data.split('////')[1]
        active_sessions[link][1]=new_cat
        info=active_sessions[link]
        sub=info[0]
        cat=info[1]
        posts=post_get(sub, cat)
        active_sessions[link][3]=posts
        
        keyboard=[[InlineKeyboardButton(text='Continue', callback_data='nxt_post////'+link)],
                  [InlineKeyboardButton(text='Change category', callback_data='cat////'+link)]]
        reply_markup=InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Category updated successfully. View posts with <b>"+new_cat+"</b> click on Continue", parse_mode='html', reply_markup=reply_markup)
        


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('policy', policy_msg))
updater.dispatcher.add_handler(CommandHandler('help', helper))
updater.dispatcher.add_handler(CommandHandler('search', searcher, pass_user_data=True))
updater.dispatcher.add_handler(CallbackQueryHandler(queryHandler))
updater.start_polling()

