#Anshika Saxena
import wikipedia
import webbrowser
import urllib.request
import os
import pyttsx3
pyttsx3.speak("Hello!! Kindly enter your name")
a=input()
print("Hii",a,"Nice to meet you.Kindly enter your choice")
web=["https://www.google.com/", "https://www.youtube.com/"]
while True:
 p=input()
 if ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("notepad" in p) or ("editor" in p))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("starting notepad")
    os.system("notepad")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("chrome" in p) or ("browser" in p))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start chrome")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and ("python" in p)) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start python")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p)or ("play" in p) or ("launch" in p)) and (("media player" in p)or ("window media" in p))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start wmplayer")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("ie" in p )or ("internet exp") in p ))and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start iexplore")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("paint" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start mspaint")
 elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("word" in p ) or ("microsoft word" in p ) )) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start MSWORD")
 elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("excel" in p ) or ("microsoft excel" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start MSEXCEL")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("powerpoint" in p )or ("ppt" in p ) )) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start POWERPNT")
 elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("gmail" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("chrome  https://mail.google.com/mail")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("control panel" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start control")
 elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("recycle bin" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start recycle bin")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("calculator" in p ) )) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start calculator")
 elif ((("shut" in p) or ("poweroff" in p) or ("turnoff") in p ) and (("pc" in p ) or ("laptop" in p ) or ("computer" in p ) or ("system" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("SHUTDOWN /i")
 elif ((("reboot" in p) or ("restart" in p)) and (("pc" in p ) or ("laptop" in p ) or ("computer" in p ) or ("system" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("SHUTDOWN /r")
 elif ((("start" in p) or ("open" in p) ) and (("explorer" in p ) or ("file expl" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("start explorer")  
 elif ((("start" in p) or ("open" in p) ) and (("youtube" in p ))) and (("don't" not in p) and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("chrome   https://www.youtube.com/")
 elif ((("start" in p) or ("open" in p) ) and (("hotstar" in p ))) and (("don't" not in p) and ("not " not  in p )):
    pyttsx3.speak("wait your program is opening")
    os.system("chrome   https://www.hotstar.com/in")
 elif ("thanks" in p) or ("thank you" in p) or ("thankxx" in p):
    print("Its my Pleasure",a ,"See you soon")
    pyttsx3.speak("Nice to meet you! Have a nice day ahead")
 else:
    pyttsx3.speak("wait for your program to open !!! Have patience")
    print("Here what i found on web about",p,"!!")
    os.system("chrome   //https://www.google.com/")
   
     
        
        
        
