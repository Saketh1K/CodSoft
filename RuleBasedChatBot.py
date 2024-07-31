import random
import re

class chatbot:
    negative_res={'nope','no','sorry','wrong'}
    exit_commands={'exit','thankyou','bye','goodbye'}
    def __init__(self):
        self.supportResponse = {
            'about_product': r'.*\s*product.*',
            'technical_support':r'.*technical.*support.*',
            'about_return':r'.*\s*returnpolicy.*',
            'general_help':r'.*how.*help.*'
        }
    def greet(self):
        self.name=input("Hello! welcome to our customer chatbot,what's your name\n")
        will_help=input(f"hi {self.name},how can i help you")
        if will_help in self.negative_res:
            print("alright thank you!have a great day")
            return
        self.chat()
    def make_exit(self,reply):
        for command in self.exit_commands:
            if command in reply:
                print("thanks for reaching us out")
                return True
            return False
    def chat(self):
        reply=input("tell me your query!").lower()
        while not self.make_exit(reply):
            reply=input(self.match_reply(reply))
    

    def match_reply(self,reply):
        for intent,regex in self.supportResponse.items():
            find_match=re.search(regex,reply)
            if find_match and intent=='about_product':
                return self.about_product()
            elif find_match and intent=='technical_support':
                return self.technical_support()
            elif find_match and intent=='about_return':
                return self.about_return()
            elif find_match and intent=='general_help':
                return self.general_help()
        return self.no_match()
    def about_product(self):
        responses=("our product is good with best reviews\n",
                "you can find our more products in product page\n")
        return random.choice(responses)
    def technical_support(self):
        responses=("you can contact our technical team i can provide their helpline numbers\n","you can see our website to know about that\n")
        return random.choice(responses)
    def about_return(self):
        responses=("we have 30 days policy\n","you can return our product if you are not satisfied with it\n")
        return random.choice(responses)
    def general_help(self):
        responses=("you can see faq section in our website\n","also you can contact our customer support\n")
        return random.choice(responses)
    def no_match(self):
        responses=("sorry! i can not provide information about that \n","i have a limited facility you can try with another query!\n")
        return random.choice(responses)
mybot=chatbot()
mybot.greet()

