import bottle
import os


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )



    return {
        'color': '#000999',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
    # check snakes
    
    # TODO: Do things with data

    return {
        'taunt': 'Super Snake Action Team!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    # check snakes
    boardHeight = int(data['height']) -1
    boardWidth = int(data['width']) -1

    print(boardWidth)
    print(boardHeight)

    ssatSnake = 'Nothing'

    snakes = data['snakes']
    for snake in snakes:
        if snake['id']='2e3e0b1d-4537-4c56-87db-010359369132'
        ssatSnake = snake
        
    print(snake)

    #print(data['snakes'])
    print("and we're Moving south, boys!")
    # TODO: Do things with data

    return {
        'move': 'south',
        'taunt': 'SSAT Moves south'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
