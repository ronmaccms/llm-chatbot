css = '''
<style>
body {
    background-color: #1e1e1e;
    color: #fff;
    font-family: Arial, sans-serif;
    font-size: 14px;  /* Adjusted font size */
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
    font-size: 0.875rem;  /* Slightly smaller font size */
}

/* Ensure the sidebar is always visible and allow the user to minimize it */
[data-testid="stSidebar"] {
    min-width: 20rem;
    max-width: 20rem;
}

/* Move everything up in the sidebar */
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
}

.sidebar-logo {
    width: 100%;
    max-width: 200px;
    margin: 0 auto;
    display: block;
}

.sidebar-center {
    text-align: center;
}

.process-button {
    display: flex;
    justify-content: center;
    margin-top: 1rem;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        -
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        +
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

sidebar_text = '''
<div align="center">
    <img src="https://raw.githubusercontent.com/ronmaccms/llm-chatbot/main/src/img/Innovation-Tournaments.jpg" alt="Innovation Tournament Logo" class="sidebar-logo">
    <h3 class="sidebar-center">About LegisBot</h3>
</div>
'''