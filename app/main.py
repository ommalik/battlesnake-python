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
        'color': '#FFCCFF',
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
    # check board dimensions
    boardHeight = int(data['height']) -1
    boardWidth = int(data['width']) -1

    #isolate snakes based on ID, starting with ours

    ssatSnake = 'Nothing'

    snakes = data['snakes']
    print('------------------------- \n')

    for snake in snakes:
        if snake['id'] == '2e3e0b1d-4537-4c56-87db-010359369132':
            print('our snake is here!')
            ssatSnake = snake
            print('/////////////// COORDS /////////////////')
            print(ssatSnake['coords'])

            ssatSnakeHead = ssatSnake['coords'][0]
            ssatSnakeBody = ssatSnake['coords'][1]
            print(ssatSnakeHead)
            
            #reaching 0 x wall
            if ssatSnakeHead[0] == 0:
                #determine where body is 
    
                #determine where food is

                #determine where to move
                return {
                    'move': 'south',
                    'taunt': 'SSAT Moves south w,0'
                    }
            #reaching w x wall
            if ssatSnakeHead[0] == boardWidth:
                
                return {
                    'move': 'south',
                    'taunt': 'SSAT Moves south w,0'
                    }

            if ssatSnakeHead[1] == 0:
                
                return {
                    'move': 'east',
                    'taunt': 'SSAT Moves south 0,0'
                    }
            #reaching w x wall
            if ssatSnakeHead[1] == boardHeight:
                
                return {
                    'move': 'west',
                    'taunt': 'SSAT Moves south 0,Y'
                    }

            
                
            #reaching x wall on boardwidth    
            

        #print snake['id']
        #print('------------------------- \n')

    #print(data['snakes'])
    print("and we're Moving south, boys!")
    # TODO: Do things with data

    return {
        'move': 'north',
        'taunt': 'SSAT Moves EAST NEUTRAL'
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
