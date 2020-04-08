from naoqi import ALProxy


class Media(object):
    def __init__(self,host='localhost',port=9559, user='Test_ASR', asr_callback=None):
        self.user = user
        self.asr_callback = asr_callback
        self.tts = ALProxy("ALTextToSpeech", host, port)
        # self.tts.setParameter("speed", 200)
        # self.tts.setLanguage("English")
        self.asr = ALProxy("ALSpeechRecognition", host, port)
        # self.asr.setLanguage("English")


    # TODO
    def start_asr(self, words=None):
        self.asr.subscribe(self.user)
        if words:
            self.asr.setVocabulary(words, False)
    
    def stop_asr(self):
        self.asr.unsubscribe(self.user)


    def say(self, text):
        self.stop_asr()
        self.tts.stopAll()
        self.tts.say(text)
    
    def stop_say(self):
        self.tts.stopAll()