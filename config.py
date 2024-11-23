TOKEN_BOT = ''
ADMINS = []















################################################################################## Тут происходит взятие сохранённых сообщений из msg.txt
with open('./msg.txt', 'r', encoding='utf-8') as f:
    messages = f.readlines()
    msgs = {str(i+1):message.strip() for i, message in enumerate(messages)}
