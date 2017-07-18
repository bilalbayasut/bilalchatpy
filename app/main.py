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

@app.route('/webhook', methods=['POST'])
def webhook():
  if request.method == "GET":
        if (request.GET.get('hub.verify_token') == 'bilalchatbot'):
            return HttpResponse(request.GET.get('hub.challenge'))
        return HttpResponse('Error, wrong validation token')

  if request.method == "POST":
        body = request.body
        print("BODY", body)
        messaging_events = json.loads(body.decode("utf-8"))
        print("JSON BODY", body)
        sender_id = messaging_events["entry"][0]["messaging"][0]["sender"]["id"]
        message = messaging_events["entry"][0]["messaging"][0]["message"]["text"]
        respond_FB(sender_id, message)
        return HttpResponse('Received.')

if __name__ == '__main__':
    app.debug=True
    app.run()
