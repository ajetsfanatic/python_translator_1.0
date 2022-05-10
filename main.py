#imported only 3 libraries for listening, translating and speaking
import googletrans
import speech_recognition
import pyttsx3



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[31].id) #I created this with spanish in mind, so change the number in voices[] to any of the
# following  =[8,15,29,31] for a spanish accent. the range of accents goes from 0-47, for ukrainian use [27]. Not all langauges
#are supported via speech unfortunately, so they may only show up as text
engine.setProperty("rate", 190) #this number is how fast the voice speaks, standard rate is 200 so feel free to play with this


#Below are the list on languages available, w/ the 2-letter designation to the left of the language of choice
#to substitute languages in lines 34 & 35, just add the 2-letter designation in between the '' i.e 'uk' for Ukrainian
#-------------------------------------------------------------------------------------------------------------------------
#'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque',
# 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
# 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech',
# 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish',
# 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati',
# 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong',
# 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese',
# 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz',
# 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy',
# 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)',
# 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese',
# 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
# 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish',
# 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish',
# 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish',
# 'yo': 'yoruba', 'zu': 'zulu'}
audio_input = speech_recognition.Recognizer()
translator = googletrans.Translator()
input_language = 'en'
output_language = 'es'

#
try:
    with speech_recognition.Microphone() as source:
        print('Bro, please speak clearly...')
        voice = audio_input.listen(source)
        text = audio_input.recognize_google(voice, language=input_language)
        print()
        print(text)
except:
    pass

#down below is where the translated speech gets displayed on screen and converted to speech
translated_speech = translator.translate(text, dest=output_language)
print(translated_speech.text)
pyttsx3.speak(translated_speech.text)
