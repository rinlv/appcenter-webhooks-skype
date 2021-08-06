from flask import Flask, request
from skpy import Skype
import os


ID = os.environ.get('ID_KEY')
PW = os.environ.get('PW_KEY')
GROUP = os.environ.get('GROUP_KEY')


app = Flask(__name__)
sk = Skype(ID, PW)


@app.route('/')
def main():
    return 'AppCenter Webhooks!'


@app.post('/notify')
def notify():
    data = request.json
    channel = sk.chats.chat(GROUP)
    channel.sendMsg(
        '!!!THÔNG BÁO: Ứng dụng ' + data['app_name'] + ' đã có bản cập nhật mới. Bản ' + data[
            'version'] + ', version ' +
        data['short_version'] + ', trên ' + data['release_notes'])
    response = app.response_class(
        response='{"success" : true}',
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
