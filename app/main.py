# from flask import Flask, request
# from fbmq import Page
#
# app = Flask(__name__)

# page = fbmq.Page('EAABuZCmQx9iYBAFlmZCnLaQmbKjJrifZATYitHuW1XZAhcCifV8HWKgfz2jLMLeJZAZCbG5wr3mLM0F7EnnwuZCYnaaS8iaYPeGHnj3tUtenfKjRXyzhmiQR8ZAlIzXehYm2d6D4dvIPzZBdihs9W1gu2DV732KAQDii1TLvMO5zo6QZDZD')
#
# @app.route('/webhook', methods=['POST'])
# def webhook():
#   page.handle_webhook(request.get_data(as_text=True))
#   return "ok"
#
# @app.route('/')
# def index():
#     return "ok"
#
# @page.handle_message
# def message_handler(event):
#   """:type event: fbmq.Event"""
#   sender_id = event.sender_id
#   message = event.message_text
#
#   page.send(sender_id, "thank you! your message is '%s'" % message)
#
# @page.after_send
# def after_send(payload, response):
#   """:type payload: fbmq.Payload"""
#   print("complete")

# if __name__ == '__main__':
#     app.run()

from flask import Flask

from pymessenger.bot import Bot



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.debug=True
    app.run()
