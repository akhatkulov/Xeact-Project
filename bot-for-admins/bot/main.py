from telebot import TeleBot, types
from . import mk_vd

def set_step(step):
    with open("data/odam.step", 'w+') as f:
        f.write(step)

def get_step() -> str:
    try:
        with open("data/odam.step", 'r+') as f:
            step = f.read()
        return step
    except:
        pass
 

admin_id = 789945598
app = TeleBot(token="7091523126:AAGguQTNbELyM47fczvXFRMpxEEeGYd0FlE")

def admin_keys():
    x = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    btn1 = types.KeyboardButton(text="Kino")
    x.add(btn1)
    return x

def mk_db(fname,content_x):
    with open(f"data/{fname}","w+") as f:
         f.write(content_x)

def read_db(fname):
    with open (f"data/{fname}","r+") as f:
        x = f.read()
    return x


@app.message_handler()
def home(msg : types.Message):
    chat_id = msg.chat.id
    text = msg.text
    if text == "/start" and chat_id!=admin_id:
        set_step("default")
        app.send_message(chat_id=chat_id,text="Bot ko'chirilgan: @XeactBot | Xeact.uz")
    elif text == "/start" and chat_id==admin_id:
        set_step("default")
        app.send_message(chat_id=admin_id,text="Salom panelga hush kelibsiz",reply_markup=admin_keys())
    elif text=="Kino" and chat_id==admin_id and text != "/start":
        mk_db("status.txt",msg.text)
        app.send_message(chat_id=admin_id,text="Kino nomini yuboring")
        set_step("kino_1")
    
    if get_step() == "kino_1" and text != "Kino" and text != "/start":
        mk_db("k_name.txt",msg.text)
        app.send_message(chat_id=admin_id,text="Kino uchun rasm linkini yuboring")
        set_step("kino_2")
    elif get_step() == "kino_2" and text != "Kino" and text != "/start":
        mk_db("pic_link.txt",msg.text)
        app.send_message(chat_id=admin_id,text="Kino xaqida ma'lumot yuboring")
        set_step("kino_3")
    elif get_step() == "kino_3" and text != "Kino" and text != "/start":
        mk_db("about.txt",msg.text)
        app.send_message(chat_id=admin_id,text="Yuklab olish kodini bering")
        set_step("end_kino")
    elif get_step()=="end_kino" and text != "Kino" and text != "/start":
        mk_db("down_link.txt",msg.text)
        mk_vd(read_db("k_name.txt"),read_db("about.txt"),read_db("pic_link.txt"),read_db("down_link.txt"))
        x = read_db("k_name.txt"),read_db("about.txt"),read_db("pic_link.txt"),read_db("down_link.txt")
        app.send_message(chat_id=chat_id ,text=f"Qabul qilindi + {x}")
        set_step("default")

mk_vd(name="salom", about="zor kino", pic_link="rasm_linki", down_code="yuklash_linki")


if __name__ == '__main__':
    app.polling()