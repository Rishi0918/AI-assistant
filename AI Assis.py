import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes # pip install pyjokes


engine = pyttsx3.init()


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

speak("This is Jarvis Here!")   

def time():
	Time = datetime.datetime.now().strftime("%I 'hours':%M'minutes':%S'seconds' ")
	speak(" the current time is")
	speak(Time)
	




def date():
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	date = int(datetime.datetime.now().day)
	speak("the current date is")
	speak(date)
	speak(month)
	speak(year)


def wishme():
	speak("welcome back sir!")
	
	
	time()
	
	date()
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour<12:
		speak("Good morning sir!")
	elif hour >=12 and hour<18:
		speak("Good Afternoon sir!")
	elif hour >= 18 and hour<24:
		speak("Good evening sir!")
	else:
	    speak("Good night sir! ")	
   
	speak("Jarvis at your service . please tell me how can i assist you?")




def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....😊 ")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing....✌")
		query = r.recognize_google(audio ,language ='en-in')
		print(query)

	except Exception as e:
		print(e)
		speak(" Please ! Say that again....")

		return "None"
	return query

def sendemail(to, content):
	server = smtplib,SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('loginid@gmail.com', 'password')
	server.sendmail('email@gmail.com',to, content)
	server.close()

def screenshot():
	img = pyautogui.screenshot()
	img.save("C:\\Users\\Rishi\\3D Objects\\ss.png")

def cpu():
	usage =str(psutil.cpu_percent())
	speak('CPU is at' + usage)
	battery= psutil.sensors_battery()
	speak("Battery is at")
	speak(battery.percent )

def jokes():
	speak(pyjokes.get_joke())





if __name__=="__main__":
	wishme()
	while  True:
		query = takeCommand().lower()

		if 'what is your name' in query:
			speak("My Name is Jarvis!")


		if 'time' in query:
			time()
		elif 'date' in query:
			date()
		elif 'wikipedia' in query:
			print("Searching....🤔🤔")
			speak("Searching.... ")
			query = query.replace("wikipedia","")
			result = wikipedia.summary(query,sentences=4)
			print(result)
			speak(result)
		elif 'send an email' in query:
			try:
				speak("What should i say?")
				content = takeCommand()
				speak("please mention the reciver's email address")
				to= takeCommand()
				sendEmail(to,content)
				speak("your Email has been sent successfully!")
			except Exception as e:
				print(e)
				speak("Unable to sent the email")
				


		elif 'chrome' in query:
			speak("what should i search?")
			chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
			search = takeCommand().lower()
			wb.get(chromepath).open_new_tab(search) #[you can add  + ".com" after search in the brackets]

		elif 'shut down' in query:
			os.system("shutdown /s /t 1")

		elif 'restart' in query:
			os.system("shutdown /r /t 1")

		elif 'lock' in query:
			os.system("shutdown -l")

		elif 'play songs' in query:
			songs_dir = 'C:\Music'
			songs = os.listdir(songs_dir)
			os.startfile(os.path.join(songs_dir,songs[0]))

		elif 'remember that' in query:
			speak("What should i remember?")
			data = takeCommand()
			speak("you said me to remember that" + data )
			remember = open('data.txt','w')
			remember.write(data)
			remember.close()
		elif 'do you know anything' in query:
			remember= open('data.txt','r')
			speak("you said me to remember that" + remember.read())

		elif 'screenshot' in query:
			screenshot()
			speak("screenshot saved successfully!")

		elif 'cpu' in query:
			cpu()

		elif 'joke' in query:
			jokes()

		elif 'thank you' in query:
			speak( "it was my pleasure helping you... see you again sir!")
			quit()


     









	
