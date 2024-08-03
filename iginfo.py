#!bin/python
import os,sys,requests,time

os.system("clear")
logo="""
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗███╗   ██╗███████╗ ██████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝██╔═══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║██║██╔██╗ ██║█████╗  ██║   ██║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║ ╚████║███████║   ██║   ██║  ██║██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝
>>>>>>>>>>>>>>>>>>>>>>>>[•Version-1.0.1•]<<<<<<<<<<<<<<<<<<<<<<<<<<
      • Tool info : Instagram user profile public info info •
-------------------------------------------------------------------
\33[32;1m                           <[Termux]>
\33[0m"""
print(logo)


user=input("Enter Username: ")
head={'x-ig-app-id':'936619743392459'}
url=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'

def rprnt(s):
    for alien in s + '\n':
        sys.stdout.write(alien)
        sys.stdout.flush()
        time.sleep(0.1)




rprnt("\33[32;1mGathering info, please wait....\33[0m\n")

req=requests.get(url,headers=head).json()['data']['user']
i=req['id']
p=req['profile_pic_url']
fo=req['edge_followed_by']['count']
fw=req['edge_follow']['count']
b=req['biography']
m=req['edge_owner_to_timeline_media']['count']
fid=req['fbid']
ib=req['is_business_account']
dt = requests.get(f"https://o7aa.pythonanywhere.com/?id={i}").json()['date']



rprnt("-"*48)
print("\n")
print(f"info\t\t")
print(f"Numeric id " + i)
print(f"Followers ",fo)
print(f"Following " , fw)
print(f"Bio " , b)
print(f"Posts " , m)
print(f"Fb numeric id " , fid)
print(f"Is Business Account " , ib)
print(f"Joining Year " , dt)
print(f"Profile pic " , p)
print(f"profile emails " + e)



