css = '''
<style>
body {
    background-color: #1e1e1e;
    color: #fff;
    font-family: Arial, sans-serif;
}

.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}

.chat-message.user {
    background-color: #2b313e;
}

.chat-message.bot {
    background-color: #475063;
}

.chat-message .avatar {
    width: 50px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #3b3b3b;
    border-radius: 50%;
    margin-right: 1rem;
    font-size: 1.5rem;
    color: #fff;
}

.chat-message .message {
    width: calc(100% - 70px);
    padding: 0 1rem;
    color: #fff;
    font-size: 1rem;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        🤖
    </div>
    <div class="message">{{MSG}}</div>
</div>

'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        🙋
    </div>
    <div class="message">{{MSG}}</div>
</div>

'''
