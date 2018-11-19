import threading
import time
from bot import bot


class MyThread(threading.Thread):
	def __init__(self,date,user):
		self.date = date
		self.user = user
	
	def run(self):
		time.sleep(1)
		while(self.date - time.time() > 0): ()
		bot.send_message(self.user,'Время!')


thread = MyThread(date = target_time , user = message.from_user.id)
thread.start()