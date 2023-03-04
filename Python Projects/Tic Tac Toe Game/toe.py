from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
import random

class MainApp(App):
	def build(self):
		return Builder.load_file("style.kv")

	turn = "X"
	empty = ""
	winner = False
	x_score = 0
	o_score = 0
	tie = 0
	osts = ["music/dio_JbyIlwx.mp3","music/high_dio_feels_high.mp3","music/muda_muda_muda_sound_effect.mp3",
	"music/reaction-za-warudo.mp3","music/rurururu-doppios-ringtone-jojo-all-star-battle.mp3",
	"music/shizaaaaaa_w7zSfcu.mp3","music/the-world-vs-star-platinum-muda-muda-muda-vs-ora-ora-ora_1.mp3",
	"music/wry.mp3","music/za-warudo-over-heaven-sound-effect.mp3","music/za-warudo-toki-wo-tomare_WJVdsYt.mp3"]
	def pressed(self,btn):
		if self.turn == "X":
			btn.text = "X"
			btn.color = "#FF3333"
			btn.disabled = True
			self.turn = "O"
			self.root.ids.score.text = "O's Turn!"
		else:
			btn.text = "O"
			btn.color = "blue"
			btn.disabled = True
			self.turn = "X"
			self.root.ids.score.text = "X's Turn!"
		
		self.check_winner()

	def disable_All_buttons(self):
		bt = "self.root.ids.btn1.disabled = True"
		num = 1
		for b in range(1,10):
			bt = bt.replace(bt[17],str(num))
			exec(bt)
			num += 1
		
	def empty_spaces(self):
		places = 9
		if self.root.ids.btn1.text != self.empty:
			places -= 1
		if self.root.ids.btn2.text != self.empty:
			places -= 1
		if self.root.ids.btn3.text != self.empty:
			places -= 1
		if self.root.ids.btn4.text != self.empty:
			places -= 1
		if self.root.ids.btn5.text != self.empty:
			places -= 1
		if self.root.ids.btn6.text != self.empty:
			places -= 1
		if self.root.ids.btn7.text != self.empty:
			places -= 1
		if self.root.ids.btn8.text != self.empty:
			places -= 1
		if self.root.ids.btn9.text != self.empty:
			places -= 1	
		
		if places == 0:
			return True

	def endgame(self,a=None,b=None,c=None):
		if self.winner == True:
			self.disable_All_buttons()
			a.color = "green"
			b.color = "green"
			c.color = "green"
			if a.text == "X":
				self.x_score += 1
				self.root.ids.score.text = f"{a.text} Wins!"
			elif a.text == "O":
				self.o_score += 1
				self.root.ids.score.text = f"{a.text} Wins!"
		elif self.winner == "Tie":
			self.disable_All_buttons()
			self.root.ids.score.text = "Tie!"

		self.root.ids.game.text = f"X:{self.x_score}   |   O:{self.o_score}"
		random.shuffle(self.osts)
		self.jojo = random.choice(self.osts)
		self.ost = SoundLoader.load(self.jojo)
		self.ost.play()

	def check_winner(self):
		if self.root.ids.btn1.text == self.root.ids.btn2.text == self.root.ids.btn3.text != "":
			self.winner = True
			self.endgame(self.root.ids.btn1,self.root.ids.btn2,self.root.ids.btn3)
		if self.root.ids.btn4.text == self.root.ids.btn5.text == self.root.ids.btn6.text != "":
			self.winner = True
			self.endgame(self.root.ids.btn4,self.root.ids.btn5,self.root.ids.btn6)
		if self.root.ids.btn7.text == self.root.ids.btn8.text == self.root.ids.btn9.text != "":
			self.winner = True
			self.endgame(self.root.ids.btn7,self.root.ids.btn8,self.root.ids.btn9)
		if self.root.ids.btn1.text == self.root.ids.btn4.text == self.root.ids.btn7.text != "":
			self.winner = True
			self.endgame(self.root.ids.btn1,self.root.ids.btn4,self.root.ids.btn7)
		if self.root.ids.btn2.text == self.root.ids.btn5.text == self.root.ids.btn8.text != "":
			self.winner = True
			self.endgame(self.root.ids.btn2,self.root.ids.btn5,self.root.ids.btn8)
		if self.root.ids.btn3.text == self.root.ids.btn6.text == self.root.ids.btn9.text != "":
			self.winner = True
			self.endgame(self.root.ids.btn3,self.root.ids.btn6,self.root.ids.btn9)
		if self.root.ids.btn1.text == self.root.ids.btn5.text == self.root.ids.btn9.text != "":
			self.winner = True
			self.endgame(self.root.ids.btn1,self.root.ids.btn5,self.root.ids.btn9)
		if self.root.ids.btn3.text == self.root.ids.btn5.text == self.root.ids.btn7.text != "":
			self.winner = True
			self.endgame(self.root.ids.btn3,self.root.ids.btn5,self.root.ids.btn7)
		if self.empty_spaces() == True:
			self.winner = "Tie"
			self.endgame()
		



	def restart(self):
		self.turn = "X"
		self.root.ids.score.text = "X Goes First!"
 		
		bt = "self.root.ids.btn1.disabled = False"
		bx = "self.root.ids.btn1.text = self.empty "
		num = 1
		for b in range(1,10):
			bt = bt.replace(bt[17],str(num))
			bx = bx.replace(bx[17],str(num))
			exec(bt)
			exec(bx)
			num += 1
		


if __name__ == "__main__":
	MainApp().run()