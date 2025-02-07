from gtts import gTTS
import vlc
import speech_recognition as sr
import pyttsx3 
import datetime
import os
import webbrowser
from time import sleep
import pyautogui
from pynput.keyboard import Key, Controller
import requests
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia


my_lang = "ar"

def speak(my_text):
    myobj = gTTS(text=my_text,lang=my_lang,slow=False,)

    myobj.save("welcome.mp4")

    p = vlc.MediaPlayer("welcome.mp4")
    p.play()

            
def get_time():
     return datetime.datetime.now().strftime("%H:%M:%S")   

def get_date():
     return datetime.datetime.now().strftime("%A %d/%m/%Y")


def get_weather():
    api_key = "fae4e4336c31fe86cbbcc17161fec8e5"
    city = "Cairo"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()
    Weather=data["weather"][0]["description"]
    Temperature= data["main"]["temp"]
    Humidity=data["main"]["humidity"]
    speak(f" حالة الطقس  {Weather}, و درجة الحرارة الأن {Temperature} و تبلغ درجة الرطوبة {Humidity} في المئة")

def get_dollar_price():
    Api_key = "235fd4efba806bae608a35d794d42e7a" 
    response = requests.get('http://data.fixer.io/api/latest?access_key='+Api_key)
    data = response.json()
    egy_price=round(data["rates"]["EGP"]/data["rates"]["USD"],2)
    speak(f" الدولار عامل {egy_price}  جنيه")

def get_news():
    page = requests.get(f"https://www.youm7.com/Tags/Index?id=46247&tag=%d8%a7%d8%ae%d8%a8%d8%a7%d8%b1-%d8%a7%d9%84%d9%8a%d9%88%d9%85")
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    news = soup.find_all(id = "paging")
    def get_news(news):
        i = 3
        while i <= 42:
            new_title = news.contents[i].find("a",class_ = "bigOneImg")
            n = new_title.find(class_ = "img-responsive")
            the_title_of_news = n.get("title")

            speak(the_title_of_news)
            sleep(10)
            i += 4
    get_news(news[0])

    

def q_chat():
    try:
        location1 = None
        while location1 is None:
            location1 = pyautogui.locateOnScreen('chat.png')
            sleep(1)
            pyautogui.click(location1.left+15,location1.top+10)

    except pyautogui.ImageNotFoundException:
        print("iMAGE NOT FOUND")
def chat_take_copy():
    location1 = None
    while location1 is None:
        try:
            location1 = pyautogui.locateOnScreen('copy.png')
            sleep(1)
            pyautogui.click(location1.left+15,location1.top+15)

        except pyautogui.ImageNotFoundException:
            print("iMAGE NOT FOUND")    

    
  
keyboard = Controller()


def type_arabic(text):
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        sleep(0.1)


r = sr.Recognizer()

def listen():
     
    try:
        with sr.Microphone() as source:
            print("listening...")

            r.adjust_for_ambient_noise(source,duration=1)
                    
            my_audio = r.listen(source)
            command = None        
            command = r.recognize_google(my_audio,language = my_lang)
            print(command)
            if 'اليكسا' in command:
                print(command)
                return command
            else:
                return ""

               
    except:
        if  command is None:
            
            speak('مش فاهمه')

        
 
        
            
        

def serch_wrods_in_string(words_list,srch_str):
    for word in words_list:
        if word in srch_str:
            return True


def response():
     
    state = True
    while state:
        my_voice = listen()
        if not my_voice is None:
            print(my_voice)
            
            if serch_wrods_in_string(['انهي','إنهاء','انهاء'],my_voice) :
                state = False
            elif 'اليكسا' == my_voice:  
                speak('أومورني')

            elif serch_wrods_in_string(['أخبار','اخبار','الاخبار'],my_voice) : 
                get_news()       

            elif serch_wrods_in_string(['ترمنال','الترمينال','ترمينال'],my_voice):
                pyautogui.hotkey('ctrl','alt','t')

            elif serch_wrods_in_string(['طقس','الطقس'],my_voice):    
                get_weather()

            elif serch_wrods_in_string(['دولار','الدولار'],my_voice):
                get_dollar_price()    


            elif serch_wrods_in_string(['وقت','الساعه','الساعة'],my_voice):
                speak("الساعة الان هي "+get_time())

            elif serch_wrods_in_string(['التاريخ','تاريخ'],my_voice) :
                speak("التاريخ اليوم هو "+get_date())

            elif serch_wrods_in_string(['عامله ايه','كيف خالك'],my_voice):
                speak("الحمد لله") 

            elif serch_wrods_in_string(['الفيسبوك','فيسبوك','فيس'],my_voice):
                webbrowser.open('https://www.facebook.com/profile.php?id=100014735089383')


            elif serch_wrods_in_string(['هب','هاب','جيت'],my_voice) :
                webbrowser.open('https://github.com/ahmedfathy21')    

            elif serch_wrods_in_string(['ان','لينكد','لينكدان'],my_voice) :
                webbrowser.open('https://www.linkedin.com/in/ahmed-fathy0/')   

            elif 'تويتر' in my_voice :
                webbrowser.open('https://x.com/MESSI1987_2024')

            elif serch_wrods_in_string(['انستغرام','الانستغرام','انستا'],my_voice) :
                webbrowser.open('https://www.instagram.com/kakashi_thereal/')

            elif serch_wrods_in_string(['ابحثي','سرشي','جوجل'],my_voice) :   
                t = my_voice.replace('اليكسا','')
                t = t.replace('سرشي','')
                t = t.replace('جوجل','')

                pywhatkit.search(t)
            
            elif serch_wrods_in_string(['اليوتيوب','يوتيوب','شغلي'],my_voice) :
                y = my_voice.replace('اليكسا','')
                y = y.replace('شغلي','')
                y = y.replace('يوتيوب','')

                pywhatkit.playonyt(y)
                sleep(5)
                pyautogui.click(1000,300)

            elif serch_wrods_in_string(['اسألي','سؤال'],my_voice) :
                q = my_voice.replace('اليكسا','')
                q = q.replace('سؤال','')

                speak('جاري البحث ')
                webbrowser.open('https://chatgpt.com/')
                #os.system('xdg-open https://chatgpt.com/')
                sleep(5)
                type_arabic(q)
                sleep(3)
                q_chat()
                #sleep(20)
                chat_take_copy()
                os.system("touch temp.txt")
                sleep(2)
                os.system("open temp.txt")
                sleep(2)
                pyautogui.hotkey('ctrl','v')
                pyautogui.hotkey('ctrl','s')
                sleep(2)
    
                with open('temp.txt','r') as f:
                    for line in f.readlines():
                        print(line)
                        speak(line)
                        
                os.system('rm temp.txt')

            elif serch_wrods_in_string(['عن','كلميني','ملخص'],my_voice) :
                my_voice = my_voice.replace('كلميني','')
                my_voice = my_voice.replace('عن','')
                my_voice = my_voice.replace('اليكسا','') 
                info = wikipedia.summary(my_voice, sentences=1)
                speak(info)


                

            elif serch_wrods_in_string(['النوم','ينام','انام'],my_voice) :
                speak('نوما هنئا مستر عبدو')
                webbrowser.open('https://www.youtube.com/watch?v=MyLQegDd-DU')
                sleep(3)
                pyautogui.press('enter')
                break
            


    #speak('مع السلامه')


          
response()