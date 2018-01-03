from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_user(self,update):
        text = update.message.text
        if not text is None:
            if text.lower() == 'rabbit' or text.lower() == 'cat' or text.lower() == 'dog':
                return False
            else:
                return True

    def is_going_to_rabbit(self, update):
        text = update.message.text
        return text.lower() == 'rabbit'

    def is_return_to_rabbit(self, update):
        text = update.message.text
        if text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c' or text.lower() == 'e':
            return False
        else:
            return True
                   
    def is_going_to_cat(self, update):
        text = update.message.text
        return text.lower() == 'cat'

    def is_return_to_cat(self, update):
        text = update.message.text
        if text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c' or text.lower() == 'e':
            return False
        else:
            return True
                   
    def is_going_to_dog(self, update):
        text = update.message.text
        return text.lower() == 'dog'

    def is_return_to_dog(self, update):
        text = update.message.text
        if text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c' or text.lower() == 'e':
            return False
        else:
            return True
                   
    def is_going_to_1(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_2(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_3(self, update):
        text = update.message.text
        return text.lower() == 'c'

    def on_enter_user(self,update):
        update.message.reply_text("Please choose a kind of animal\n(Enter:rabbit,cat,dog)")

    def on_enter_rabbit(self, update):
        update.message.reply_text("You choose rabbit!\nWhich do you like?\nA.道奇兔\nB.垂耳兔\nC.More\n(Please Enter A,B,or C)\nEnter E to return to menu")

    def on_enter_rabbit_1(self, update):
        update.message.reply_text("https://www.google.com.tw/search?hl=zh-TW&dcr=0&biw=1855&bih=851&tbm=isch&sa=1&ei=p19MWvgWg7DQBMCMoJgG&q=%E9%81%93%E5%A5%87%E5%85%94&oq=%E9%81%93%E5%A5%87%E5%85%94&gs_l=psy-ab.3..0l3j0i24k1l7.1307907.1320098.0.1321214.19.18.1.0.0.0.173.1343.13j4.17.0....0...1c.1.64.psy-ab..1.12.927...0i5i30k1j0i13k1.0.reabXQIWq5c")
        update.message.reply_text("Enter\nR:choose other\nM:for more\nE:return to menu")

    def on_enter_rabbit_2(self, update):
        update.message.reply_text("https://www.google.com.tw/search?q=%E5%9E%82%E8%80%B3%E5%85%94&client=ubuntu&hs=CKJ&channel=fs&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjrrKP6grvYAhUM6bwKHbukDqMQ_AUICigB&biw=1855&bih=851")
        update.message.reply_text("Enter\nR:choose other\nM:for more\nE:return to menu")

    def on_enter_rabbit_3(self, update):
        update.message.reply_text("http://blog.xuite.net/blue_sky23/rabbitget")
        update.message.reply_text("Enter\nR:choose other\nE:return to menu")

    def on_exit_rabbit(self, update):
        print('Leaving rabbit')

    def on_enter_cat(self, update):
        update.message.reply_text("You choose cat!\nWhich do you like?\nA.摺耳貓\nB.布偶貓\nC.More\n(Please Enter A,B,or C)\nEnter E to return to menu")

    def on_enter_cat_1(self, update):
        update.message.reply_text("https://www.google.com.tw/search?q=%E6%91%BA%E8%80%B3%E8%B2%93&client=ubuntu&hs=3yI&channel=fs&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwivwZCJ_rrYAhXFk5QKHbUAB64Q_AUICigB&biw=1855&bih=851#imgrc=_")
        update.message.reply_text("Enter\nR:choose other\nM:for more\nE:return to menu")

    def on_enter_cat_2(self, update):
        update.message.reply_text("https://www.google.com.tw/search?q=%E5%B8%83%E5%81%B6%E8%B2%93&client=ubuntu&channel=fs&dcr=0&stick=H4sIAAAAAAAAAONgFuLQz9U3MKwsqlDiBLGMys2TzbXUspOt9JMy83Py0yv1U_JzU4tLMpMTS1JT4hPzMnMTc6ySilJTU4ofMcZyC7z8cU9YKmTSmpPXGP24iNQopMLF5ppXkllSKSTFxSMFd4MGgxQXF5zHAwAUO0ArnwAAAA&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiri-ybgrvYAhUIf7wKHYYyCaQQ_AUICigB")
        update.message.reply_text("Enter\nR:choose other\nM:for more\nE:return to menu")

    def on_enter_cat_3(self, update):
        update.message.reply_text("http://www.buzzhand.com/post_586969.html")
        update.message.reply_text("Enter\nR:choose other\nE:return to menu")

    def on_exit_cat(self, update):
        print('Leaving cat')

    def on_enter_dog(self, update):
        update.message.reply_text("You choose dog!\nWhich do you like?\nA.柯基\nB.博美\nC.More\n(Please Enter A,B,or C)\nEnter E to return to menu")

    def on_enter_dog_1(self, update):
        update.message.reply_text("https://www.google.com.tw/search?q=%E6%9F%AF%E5%9F%BA&client=ubuntu&channel=fs&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiKgbDFgrvYAhUKabwKHQXJDqoQ_AUICigB&biw=1855&bih=851")
        update.message.reply_text("Enter\nR:choose other\nM:for more\nE:return to menu")

    def on_enter_dog_2(self, update):
        update.message.reply_text("https://www.google.com.tw/search?q=%E5%8D%9A%E7%BE%8E%E7%8A%AC&client=ubuntu&channel=fs&dcr=0&stick=H4sIAAAAAAAAAONgFuLUz9U3SCqxzClSAjMNzcrTKrXUspOt9JMy83Py0yv1U_JzU4tLMpMTS1JT4hPzMnMTc6ySilJTU4ofMcZzC7z8cU9YKmzSmpPXGAO4iNQopMbF5ppXkllSKSTDxSuFcIQGgxQ3F4LLAwAwwFhTogAAAA&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjQ6dm9hLvYAhWDoJQKHe-7AuQQ_AUICigB")
        update.message.reply_text("Enter\nR:choose other\nM:for more\nE:return to menu")

    def on_enter_dog_3(self, update):
        update.message.reply_text("")
        update.message.reply_text("Enter\nR:choose other\nE:return to menu")

    def on_exit_state3(self, update):
        print('Leaving state3')

    def is_return(self, update):
        text = update.message.text
        return text.lower() == 'r'

    def is_exit(self, update):
        text = update.message.text
        return text.lower() == 'e'

    def is_more(self, update):
        text = update.message.text
        return text.lower() == 'm'

