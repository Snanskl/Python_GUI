from random import randint
import customtkinter 

#I have used CTk for the widgets, which is known to be more easier and more modern to use than the default tkinter widgets

#set the appearance mode to dark
customtkinter.set_appearance_mode("dark")

#set the default color theme to green
customtkinter.set_default_color_theme("green")

#make a root to be more modern with customtkinter
root = customtkinter.CTk()

#title of the program
root.title("Japanese flashcard by Minou")
root.geometry("1000x410")

#create a list that contain of tuples of japanese words and their english translation
#list are mutable, so we can add more words to the list
#tuples are immutable, so we can't change the words in the list
words = [
    (("こんにちは"), ("Konnichiwa"), ("Hello")),
    (("さようなら"), ("Sayōnara"), ("Goodbye")),
    (("ありがとうございます"), ("Arigatōgozaimasu"), ("Thank you very much")),
    (("すみません"), ("Sumimasen"), ("Excuse me/I'm sorry")),
    (("はい"), ("Hai"), ("Yes")),
    (("いいえ"), ("Iie"), ("No")),
    (("おはようございます"), ("Ohayōgozaimasu"), ("Good morning")),
    (("こんばんは"), ("Konbanwa"), ("Good evening")),
    (("おやすみなさい"), ("Oyasuminasai"), ("Good night")),
    (("お名前は？"), ("O-namae wa?"), ("What's your name?")),
    (("私の名前は...です"), ("Watashi no namae wa...desu"), ("My name is...")),
    (("どうぞよろしく"), ("Dōzo yoroshiku"), ("Please to meet you/Nice to meet you")),
    (("いただきます"), ("Itadakimasu"), ("I humbly receive (before eating)")),
    (("ごちそうさまでした"), ("Gochisōsama deshita"), ("That was a feast (after eating)")),
    (("お願いします"), ("Onegaishimasu"), ("Please")),
    (("トイレはどこですか？"), ("Toire wa doko desu ka?"), ("Where is the toilet?")),
    (("日本"), ("Nihon"), ("Japan")),
    (("日本語"), ("Nihongo"), ("Japanese (language)")),
    (("英語"), ("Eigo"), ("English (language)")),
    (("数"), ("Sū"), ("Number")),
    (("食べる"), ("Taberu"), ("Eat")),
    (("飲む"), ("Nomu"), ("Drink")),
    (("大丈夫"), ("Daijōbu"), ("All right/OK")),
    (("分かります"), ("Wakarimasu"), ("I understand")),
    (("分かりません"), ("Wakarimasen"), ("I don't understand")),
    (("日本人"), ("Nihonjin"), ("Japanese (person)")),
    (("外国人"), ("Gaikokujin"), ("Foreigner")),
    (("学生"), ("Gakusei"), ("Student")),
    (("先生"), ("Sensei"), ("Teacher")),
    (("会社員"), ("Kaishain"), ("Company employee")),
    (("家"), ("Ie"), ("House/Home")),
    (("学校"), ("Gakkō"), ("School")),
    (("病院"), ("Byōin"), ("Hospital")),
    (("銀行"), ("Ginkō"), ("Bank")),
    (("電車"), ("Densha"), ("Train")),
    (("飛行機"), ("Hikōki"), ("Airplane")),
    (("車"), ("Kuruma"), ("Car")),
    (("自転車"), ("Jitensha"), ("Bicycle")),
    (("電話"), ("Denwa"), ("Phone")),
    (("携帯電話"), ("Keitaidenwa"), ("Mobile phone")),
    (("時計"), ("Tokei"), ("Clock/Watch")),
    (("お金"), ("Okane"), ("Money")),
    (("財布"), ("Saifu"), ("Wallet")),
    (("鞄"), ("Kaban"), ("Bag")),
    (("本"), ("Hon"), ("Book")),
    (("新聞"), ("Shinbun"), ("Newspaper")),
    (("雑誌"), ("Zasshi"), ("Magazine")),
    (("手紙"), ("Tegami"), ("Letter")),
    (("印鑑"), ("Inkan"), ("Seal/Stamp")),
    (("切符"), ("Kippu"), ("Ticket")),
    (("パスポート"), ("Pasupōto"), ("Passport")),
    (("鍵"), ("Kagi"), ("Key")),
    (("傘"), ("Kasa"), ("Umbrella")),
    (("帽子"), ("Bōshi"), ("Hat")),
    (("メガネ"), ("Megane"), ("Glasses")),
    (("テレビ"), ("Terebi"), ("Television")),
    (("ラジオ"), ("Rajio"), ("Radio")),
    (("CD"), ("Shīdī"), ("CD")),
    (("テープ"), ("Tēpu"), ("Tape")),
    (("カメラ"), ("Kamera"), ("Camera")),
    (("コンピュータ"), ("Konpyūta"), ("Computer")),
    (("バス"), ("Basu"), ("Bus")),
    (("地下鉄"), ("Chikatetsu"), ("Subway")),
    (("タクシー"), ("Takushī"), ("Taxi")),
    (("食堂"), ("Shokudō"), ("Dining hall/Cafeteria")),
    (("レストラン"), ("Resutoran"), ("Restaurant")),
    (("喫茶店"), ("Kissaten"), ("Coffee shop")),
    (("パン屋"), ("Pan'ya"), ("Bakery")),
    (("スーパー"), ("Sūpā"), ("Supermarket")),
    (("コンビニ"), ("Konbini"), ("Convenience store")),
    (("郵便局"), ("Yūbinkyoku"), ("Post office")),
    (("銀行"), ("Ginkō"), ("Bank")),
    (("病院"), ("Byōin"), ("Hospital")),
    (("薬局"), ("Yakkyoku"), ("Pharmacy")),
    (("図書館"), ("Toshokan"), ("Library")),
    (("公園"), ("Kōen"), ("Park")),
    (("動物園"), ("Dōbutsuen"), ("Zoo")),
    (("美術館"), ("Bijutsukan"), ("Art museum")),
    (("映画館"), ("Eigakan"), ("Movie theater")),
    (("劇場"), ("Gekijō"), ("Theater")),
    (("スポーツセンター"), ("Supōtsusentā"), ("Sports center")),
    (("教会"), ("Kyōkai"), ("Church")),
    (("神社"), ("Jinja"), ("Shinto shrine")),
    (("寺"), ("Tera"), ("Temple")),
    (("海"), ("Umi"), ("Sea")),
    (("山"), ("Yama"), ("Mountain")),
    (("川"), ("Kawa"), ("River")),
    (("湖"), ("Mizuumi"), ("Lake")),
    (("田んぼ"), ("Tanbo"), ("Rice paddy")),
    (("森"), ("Mori"), ("Forest")),
    (("花"), ("Hana"), ("Flower")),
    (("木"), ("Ki"), ("Tree")),
    (("芝生"), ("Shibafu"), ("Lawn/Grass")),
    (("空"), ("Sora"), ("Sky")),
    (("星"), ("Hoshi"), ("Star")),
    (("月"), ("Tsuki"), ("Moon")),
    (("太陽"), ("Taiyō"), ("Sun")),
    (("雲"), ("Kumo"), ("Cloud")),
    (("雨"), ("Ame"), ("Rain")),
    (("雪"), ("Yuki"), ("Snow")),
    (("風"), ("Kaze"), ("Wind")),
    (("暑い"), ("Atsui"), ("Hot")),
    (("寒い"), ("Samui"), ("Cold")),
    (("涼しい"), ("Suzushii"), ("Cool")),
    (("暖かい"), ("Atatakai"), ("Warm")),
    (("冷たい"), ("Tsumetai"), ("Cold to the touch")),
    (("晴れ"), ("Hare"), ("Clear weather")),
    (("曇り"), ("Kumori"), ("Cloudy")),
    (("台風"), ("Taifū"), ("Typhoon")),
    (("地震"), ("Jishin"), ("Earthquake")),
    (("津波"), ("Tsunami"), ("Tsunami")),
    (("火事"), ("Kaji"), ("Fire")),
    (("事故"), ("Jiko"), ("Accident")),
    (("病気"), ("Byōki"), ("Illness/Sickness")),
    (("怪我"), ("Kega"), ("Injury")),
    (("薬"), ("Kusuri"), ("Medicine")),
    (("医者"), ("Isha"), ("Doctor")),
    (("看護婦"), ("Kangofu"), ("Nurse")),
    (("薬剤師"), ("Yakuzaishi"), ("Pharmacist")),
    (("歯医者"), ("Haisha"), ("Dentist")),
    (("風邪"), ("Kaze"), ("Cold (illness)")),
    (("咳"), ("Seki"), ("Cough")),
    (("頭痛"), ("Zutsū"), ("Headache")),
    (("腹痛"), ("Fukutsū"), ("Stomachache")),
    (("歯痛"), ("Ha itami"), ("Toothache")),
    (("目薬"), ("Megusuri"), ("Eye drops"))
]


#get a count of the number of words in the list
count = len(words)

def next():
    global hinter, hint_count, random_woord #making the variables global so that they can be accessed from the hint function
    answer_label.configure(text="") #clear the answer label when click next
    my_entry.delete(0, "end") #clear the entry field when click next
    hint_label.configure(text="") #clear the hint label when click next
    hinter = "" #reset on every new word when click next
    hint_count = 0 #reset on every new word when click next
    
    random_woord = randint(0, count - 1) #minus 1 because the index starts at 0
    japanese_words.configure(text=words[random_woord][0]) #display the japanese word randomly from 0 to the count of the words
    english_pronounce_words.configure(text=words[random_woord][1]) #display the english word according to the japanese word
    
def answerss():
    if my_entry.get().capitalize() == words[random_woord][2]:#2 is the tuple in the list where the answer in eng translate
        answer_label.configure(text=f"Correct! {words[random_woord][0]} is {words[random_woord[2]]}!", text_color = "green") #if the answer is correct, then display "Correct!" in green
    else:
        answer_label.configure(text=f"Incorrect! {words[random_woord][0]} is {words[random_woord][2]}!", text_color = "red") #if the answer is incorrect, then display "Incorrect!" in red
        
#for keeping track of the number of hints given
hinter = ""
hint_count = 0 

def hint():
    global hint_count
    global hinter
    
    if hint_count < len(words[random_woord][2]): #if the hint count is less than the length of the english translation of the word
        hinter = hinter + words[random_woord][2][hint_count] #add the hint to the hint variable
        hint_label.configure(text=f"The hint is {hinter}") #display the hint
        hint_count += 1 #increment the hint count
        
        if hint_count == len(words[random_woord][2]):
            hint_label.configure(text=f"No more hints available! The answer is {words[random_woord][2]}")


#initializing the variables and do the setup for each widgets
japanese_words = customtkinter.CTkLabel(root, text="", font=("Arial", 30)) #setup the words
japanese_words.pack(pady=20) # pack it up

english_pronounce_words = customtkinter.CTkLabel(root, text="", font=("Arial", 20)) #setup the english words
english_pronounce_words.pack(pady=10) #pack it up

answer_label =  customtkinter.CTkLabel(root, text="", font=("Arial", 20)) #setup the answer words
answer_label.pack(pady=20) #pack it up
    
my_entry =  customtkinter.CTkEntry(root, font=("Arial", 20))#set up the entry field
my_entry.pack(pady=20)#pack it up

hint_label = customtkinter.CTkLabel(root, text="", font=("Arial", 20))
hint_label.pack(pady=20)

#create buttons
#command is used to link the button to a function

button_frame =  customtkinter.CTkFrame(root)
button_frame.pack(pady=20)

answer_button = customtkinter.CTkButton(button_frame, text="Answer", command=answerss)
answer_button.grid(row=0, column=0, padx=20)

next_button = customtkinter.CTkButton(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1)

hint_button = customtkinter.CTkButton(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)

#run next function when the next button is clicked
next()

#mainloop is used to keep the window running
root.mainloop() 