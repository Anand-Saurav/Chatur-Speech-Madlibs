##Chatur Speech Malibs
##
import pyttsx3
chatur_speech=pyttsx3.init()

print("Enjoy the Chatur Speech in your own way")

education_minister=input("Name of Education Minister: ")
college_name=input("Name of the College: ")
animal_name=input("Name of Any Animal: ")
dean_name=input("Name of the Dean of University: ")
stupid_act=input("Name of any act in Hindi: ")
precious_item=input("Name of any precious item (in place of stunn): ")
newline='\n'

madlibs = f"Adarniya sabhapati mahodaya…  {newline}{newline}Atithi vishesh, Shikshan mantri shri shrimati {education_minister}… {newline}Maanyaniya shikshagan aur mere piyaaare sahapathiyon… {newline}{newline}Aaj agar {college_name} aasmaan ki bulandiyon ko chhu raha hai; to uska shreya sirrf ek {animal_name} ko jata hai Shri/Shrimati {dean_name}… Give him a a big hand… He is a great guy really…   {newline}{newline}Peechle buttis saal se inhone nirantar iss college mein {stupid_act} pe  {stupid_act} kiye…  {newline}Umeed hai aagey bee karte rahege..  {newline}Hamain to aashcharya hota hai ki ek {animal_name} apne jeevan kaal mein itni  {stupid_act} kaisi kar sakta hai...  {newline}Inhone kadi tapaasya se apne aapko iss kaabil bunaya hai…   {newline}Waqt ka sahi upyog ghante ka purna istemaal koi inse seeke… seeke inse seeke…   {newline}{newline}Aaj hum sab chaatra yaha hai…  {newline}Kal desh videsh mein faael jayenge… Waadaa hai aapse, jis desh mein honge waha  {stupid_act} karenge.  {newline}{college_name} ka naam roshan karenge… {newline}Dika denge sabko  {stupid_act} Karne ki shamtaa yaha ke chaatro mein hai wo sansaar ke kisi chaatro mein nahiii… No other chaatra No other chaatra…  {newline} {newline}Adarniya mantraji namashkar aapne iss sansthaan ko wo chees di jiski hamein sakht zaroorat thi…  {precious_item}…  {precious_item} hota sabi ke paas hai… sab chupa ke rakte hai… detaa koi nai…  {newline} {newline}Aapne apna  {precious_item} iss  {stupid_act} purush ke haat mein diya hai… ab dekiye yeh kaisa iska upyog karta hai…   {newline} {newline}Iss Uttam samay mai kuch slok yaad aa rahe hain... {newline} {newline}Utamamm dad datdat padam..madhyam padam thuchuk thuchuk  {newline}Khanishtham thudthudiii padam..sursuria pran khatkam..!!!! "
commands=input("Do you want Chatur's Speech in Written(W) or in Voice(V): ")
if (commands == "Written" or commands == 'W'):
    print(madlibs)
else:
   try:
       chatur_speech.say(madlibs)
   except:
        print("Voice Command is not possible right now!!")
   chatur_speech.runAndWait()
