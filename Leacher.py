#in the name of god | coded by sardarcyberym | yarnovin | github.com/sardarcybery
import instaloader
from time import sleep
from colorama import fore
app = instaloader.instaloader()
class leacher:
    def __init__(self,username:str,password:str,target:str) -> none:
        self.username = username
        self.passsord = password
        self.target = target
    def followersleecher(self):
        try:
            app.login(self.username,self.passsord)
            print(fore.lightgreen_ex + "login . . .")
            followerlist = []
            profile = instaloader.profile.from_username(app.context,self.target)
            sleeptime,antiban,count = 0,0,0
            filefollowers = open("followers.txt", "a+")
            for followers in profile.get_followers():
                print(followers.username)
                followerlist.append(followers.username)  
                filefollowers.write(f'{followerlist[count]}\n')
                count += 1
                sleeptime += 1
                antiban += 1
                if sleeptime == 100:
                    sleep(30)
                    sleeptime = 0
                if antiban == 8000:
                    print(fore.lightred_ex + "sleep 3600 second(1 hours) , do not exit the app")
                    sleep(3600)
                    antiban = 0
            filefollowers.close()
        except exception as ex:
            print(str(ex))
#in the name of god | Coded By SardarCyberym | Yarnovin | GitHub.com/SardarCybery
import instaloader
from time import sleep
from colorama import Fore
app = instaloader.Instaloader()
class Leacher:
    def __init__(self,Username:str,Password:str,Target:str) -> None:
        self.Username = Username
        self.Passsord = Password
        self.Target = Target
    def FollowersLeecher(self):
        try:
            app.login(self.Username,self.Passsord)
            print(Fore.LIGHTGREEN_EX + "Login . . .")
            FollowerList = []
            Profile = instaloader.Profile.from_username(app.context,self.Target)
            SleepTime,AntiBan,count = 0,0,0
            FileFollowers = open("Followers.txt", "a+")
            for Followers in Profile.get_followers():
                print(Followers.username)
                FollowerList.append(Followers.username)  
                FileFollowers.write(f'{FollowerList[count]}\n')
                count += 1
                SleepTime += 1
                AntiBan += 1
                if SleepTime == 100:
                    sleep(30)
                    SleepTime = 0
                if AntiBan == 8000:
                    print(Fore.LIGHTRED_EX + "Sleep 3600 Second(1 Hours) , Do not exit the App")
                    sleep(3600)
                    AntiBan = 0
            FileFollowers.close()
        except Exception as ex:
            print(str(ex))
GitHub.com/SardarCybery#in the name of god | Coded By SardarCyberym | Yarnovin | GitHub.com/SardarCybery
import instaloader
from time import sleep
from colorama import Fore
app = instaloader.Instaloader()
class Leacher:
    def __init__(self,Username:str,Password:str,Target:str) -> None:
        self.Username = Username
        self.Passsord = Password
        self.Target = Target
    def FollowersLeecher(self):
        try:
            app.login(self.Username,self.Passsord)
            print(Fore.LIGHTGREEN_EX + "Login . . .")
            FollowerList = []
            Profile = instaloader.Profile.from_username(app.context,self.Target)
            SleepTime,AntiBan,count = 0,0,0
            FileFollowers = open("Followers.txt", "a+")
            for Followers in Profile.get_followers():
                print(Followers.username)
                FollowerList.append(Followers.username)  
                FileFollowers.write(f'{FollowerList[count]}\n')
                count += 1
                SleepTime += 1
                AntiBan += 1
                if SleepTime == 100:
                    sleep(30)
                    SleepTime = 0
                if AntiBan == 8000:
                    print(Fore.LIGHTRED_EX + "Sleep 3600 Second(1 Hours) , Do not exit the App")
                    sleep(3600)
                    AntiBan = 0
            FileFollowers.close()
        except Exception as ex:
            print(str(ex))
self.Username#in the name of god | Coded By SardarCyberym | Yarnovin | GitHub.com/SardarCybery
import instaloader
from time import sleep
from colorama import Fore
app = instaloader.Instaloader()
class Leacher:
    def __init__(self,Username:str,Password:str,Target:str) -> None:
        self.Username = Username
        self.Passsord = Password
        self.Target = Target
    def FollowersLeecher(self):
        try:
            app.login(self.Username,self.Passsord)
            print(Fore.LIGHTGREEN_EX + "Login . . .")
            FollowerList = []
            Profile = instaloader.Profile.from_username(app.context,self.Target)
            SleepTime,AntiBan,count = 0,0,0
            FileFollowers = open("Followers.txt", "a+")
            for Followers in Profile.get_followers():
                print(Followers.username)
                FollowerList.append(Followers.username)  
                FileFollowers.write(f'{FollowerList[count]}\n')
                count += 1
                SleepTime += 1
                AntiBan += 1
                if SleepTime == 100:
                    sleep(30)
                    SleepTime = 0
                if AntiBan == 8000:
                    print(Fore.LIGHTRED_EX + "Sleep 3600 Second(1 Hours) , Do not exit the App")
                    sleep(3600)
                    AntiBan = 0
            FileFollowers.close()
        except Exception as ex:
            print(str(ex))
