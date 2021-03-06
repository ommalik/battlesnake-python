import bottle
import os
import math
'''##tiles: duration, isSnack, isFood, isOtherSnake
def update_board(response):
    i = response["width"]
    j = response["height"]
    
    #print(i)
    #print(j)
    
    board = [[{"duration":0,"isSnack":False,"isFood":False} for x in range(i)] for x in range(j)]
    
    #add foods
    if(len(response["food"])>0):
        for a in len(response["food"]):
            b = response["food"][a][0]
            c = response["food"][a][1]
            board[b][c]["isFood"]=True
        
    #print(board)
    #look at snakes
    
    ##for each snake
    for a in response["snakes"]:
        slength = len(a["coords"])
        ##for length of this selected snake
        z = 0##iterator
        for b in a["coords"]:
            
            x=b[0]
            y=b[1]
            ##later, can add the isSnack calculation
            board[x][y]["duration"] = slength-z
            z=z+1
            
            
    
    
    #return board
'''
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

    #update_board(data)

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
            
    movesToFoods =[] 
    theirMovesToFoods = []
    
    foods = data['food']
    
    for food in foods:
        xMovesToFood = ssatSnakeHead[0]-food[0]
        yMovesToFood = ssatSnakeHead[1]-food[1]
        movesToFoods.append(abs(xMovesToFood)+abs(yMovesToFood))

    print('For food we have to move ')
    print(movesToFoods)

    for snake in snakes:
        if snake['id'] != '2e3e0b1d-4537-4c56-87db-010359369132':
            

            otherSnakeHead = snake['coords'][0]
            for food in foods:
                txMovesToFood = otherSnakeHead[0]-food[0]
                tyMovesToFood = otherSnakeHead[1]-food[1]
                theirMovesToFoods.append(abs(txMovesToFood)+abs(tyMovesToFood))

            print('For food THEY have to move ')
            print(theirMovesToFoods)
    j = 0    
    
    for food in foods:

        print(movesToFoods[j])
        print(theirMovesToFoods[j])

        
        if movesToFoods[j] < theirMovesToFoods[j]:
            if ssatSnakeHead[0] != food[0]:
                if ssatSnakeHead[0] > food[0]:
                    return {
                       'move': 'west',
                        'taunt': 'SSAT Moves west'
                    }
                else:
                    return {
                        'move': 'east',
                        'taunt': 'SSAT Moves EAST food'
                    }
            elif ssatSnakeHead[1] != food[1]:
                if ssatSnakeHead[1] > food[1]:
                    return {
                       'move': 'north',
                        'taunt': 'SSAT Moves north'
                    }
                else:
                    return {
                        'move': 'south',
                        'taunt': 'SSAT Moves south food'
                    }

        j = j+1
            
    #print(movesToFoods)
    '''
    ssatSnakeHead:
        if (ssatSnakeBody[0]+1 == ssatSnakeHead[0]+1):

        return {
            'move': 'north',
            'taunt': 'SSAT Moves EAST NEUTRAL'
        }
    '''
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
