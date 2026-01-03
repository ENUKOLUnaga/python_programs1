class Messenger:
    def use_keyboard(self):
        print("use keyboard")
    def message_sent(self):
        print("message sent")
    def message_received(self):
        print("message received")

class Whatsapp(Messenger):
    def message_sent(self):
        print("send message in Whatsapp")
    def message_received(self):
        print("receive message in Whatsapp")
    def send_live_location(self):
        print("send live location in Whatsapp")

class Facebook(Messenger):
    def message_sent(self):
        print("send message in Facebook")
    def message_received(self):
        print("receive message in Facebook")
    def use_builtin_apps(self):
        print("use builtin apps")
class Instagram(Messenger):
    def message_sent(self):
        print("send message in Instagram")
    def message_received(self):
        print("receive message in Instagram")
    def use_filter(self):
        print("use filter")

def use_message(ref):
    ref.use_keyboard()
    ref.message_sent()
    ref.message_received()
    if type(ref)==Whatsapp:
        ref.send_live_location()
    if type(ref)==Facebook:
        ref.use_builtin_apps()
    if type(ref)==Instagram:
        ref.use_filter()

wa=Whatsapp()
fb=Facebook()
im=Instagram()

use_message(wa)
use_message(fb)
use_message(im)