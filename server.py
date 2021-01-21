from flask import Flask, json, request

api = Flask(__name__)

@api.route('/success', methods=['GET'])
def return_success():
  if request.headers.get('Content-Type'):
    if request.headers['Content-Type'] == 'application/json':
      return json.dumps({'success': True})
    else:
      return json.dumps({'success': False})
  else:
    return json.dumps({'error': 'no headers provided'})

if __name__ == '__main__':
    api.run()