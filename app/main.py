import bottle
import os
import math
##tiles: duration, isSnack, isFood, 
def update_board(response):
    i = response["width"]
    j = response["height"]
    
    #print(i)
    #print(j)
    
    board = [[{"duration":0,"isSnack":False,"isFood":False} for x in range(i)] for x in range(j)]
    
    #add foods
    if(len(response["food"])>0):
        for a in range(len(response["food"])):
            b = response["food"][a][0]
            c = response["food"][a][1]
            board[b][c]["isFood"]=True
        
    #print(board)
    #look at snakes
    
    ##for each snake
    #for a in response["snakes"]:
    a = response["snakes"][0]
    slength = len(a["coords"])
    
        #slength = len(a["coords"])
        ##for length of this selected snake

    for b in range(slength):
        #a["coords"][b][0]   
        #print(slength-b)
        #print(slength)
        #print(b)
        x=a["coords"][b][0] 
        y=a["coords"][b][1] 
        ##later, can add the isSnack calculation
        board[x][y]["duration"] = slength-b
            
    #print(board)
    return board

goDown = False
goUp = False
goLeft = False
goRight = False
    #return board
def prediction(board,response,count):
    print("entering prediction")
    ##find out which is our snake
    ourID = '0c8c59f0-1e9f-4453-b480-aededeb3bae8'
    ourSnake = 0
    moveCount = 0
    height = response["height"]
    width = response["width"]
    ##we need an indext to match our snake to
    q = len(response["snakes"])
    for k in range(q):
        
        if response["snakes"][k]["id"] == ourID:
            ourSnake = k
    ##we want to find the first coordinate of our snake
    ourHead = response["snakes"][ourSnake]["coords"][0]
    print("this is ourHead")
    print(ourHead)
    ##now we want to go and find the options
    
    ##x+1 x-1 y+1 y-1
    ##we have to choose which is no bueno
    ##as long as the above calculation does not equal "coords"[1] then you can choose it
    ##if point's duration not >1
        ##select it as a choice, and then make 3 options for it.
    left = [0,0]# = ourHead  
    print(left)
    print("testing this left shit")
    left[0] = ourHead[0]-1
    left[1] = ourHead[1]
    print(left)
    
    ##x and y here are going to be board compatible
    ##if we go into the board, then we should be good
    ##if board[left[0]][left[1]]["duration"]>1 and left[0]is in range(width-1) and left[1] is in range(height-1)
        ##dont' choose
    
    right = [0,0]
    right[0] = ourHead[0] + 1
    right[1] = ourHead[1]   
    
    down = [0,0]
    down[0] = ourHead[0] 
    down[1] = ourHead[1] + 1
    
    up = [0,0]
    up[0] = ourHead[0]
    up[1] = ourHead[1] - 1
    
    #print("ourhead =")
    #print(ourHead)
    
    #print(left)
    #print(right)
    #print(up)
    #print(down)
    #print("left again")
    #print(left)
    

    ##we have our 4 directions
    ##now we do an elimination
    ##which of these is equal to duration>1
    if (board[left[0]][left[1]]["duration"]<2) and (count>0) and (left[0]>0) and (left[1]>0) and (left[0]<width-1) and (left[1]<height-1):
        ##update board with current left coordinate and call again
        if count ==1:
            goLeft = True        
        #board[left[0]][left[1]]["duration"] = slength
        ##we are advancing snake head in the left direction for new call
        tempData = response
        tempData["snakes"][ourSnake]["coords"][0]=left
        tempBoard=board
        board[left[0]][left[1]]["duration"]=3
        count=count-1
        prediction(tempBoard,tempData,count)
    if (board[right[0]][left[1]]["duration"]<2) and(count>0) and(left[0]>0) and (left[1]>0) and(left[0]<width-1) and(left[1]<height-1):
        ##update board and call again
        if count ==1:
            goRight = True
        tempData = response
        tempData["snakes"][ourSnake]["coords"][0]=right
        tempBoard=board
        board[right[0]][right[1]]["duration"]=3
        count=count-1
        prediction(tempBoard,tempData,count)
    if (board[up[0]][up[1]]["duration"]<2) and(count>0) and(left[0]>0) and (left[1]>0) and(left[0]<width-1) and(left[1]<height-1):
        ##update board with current left coordinate and call again
        
        #board[left[0]][left[1]]["duration"] = slength
        ##we are advancing snake head in the left direction for new call
        if count ==1:
            goUp = True
        tempData = response
        tempData["snakes"][ourSnake]["coords"][0]=up
        tempBoard=board
        board[up[0]][up[1]]["duration"]=3
        count=count-1
        prediction(tempBoard,tempData,count)
        
    if (board[down[0]][down[1]]["duration"]<2) and(count>0) and (left[0]>0) and (left[1]>0) and (left[0]<width-1) and (left[1]<height-1):
        ##update board with current left coordinate and call again
        if count ==1:
            goDown = True        
        #board[left[0]][left[1]]["duration"] = slength
        ##we are advancing snake head in the left direction for new call
        tempData = response
        tempData["snakes"][ourSnake]["coords"][0]=down
        tempBoard=board
        board[down[0]][down[1]]["duration"]=3
        count=count-1
        prediction(tempBoard,tempData,count)

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

    board = update_board
    prediction(board,data,2)    

    for food in foods:

        print(movesToFoods[j])
        print(theirMovesToFoods[j])


        if movesToFoods[j] < theirMovesToFoods[j]:

            if ssatSnakeHead[0] != food[0]:
                if ssatSnakeHead[0] > food[0] and (ssatSnakeHead[0]-1 != ssatSnakeBody[0]) and goLeft:

                    return {
                       'move': 'west',
                        'taunt': 'SSAT Moves west'
                    }
                elif (ssatSnakeHead[0]+1 != ssatSnakeBody[0]) and goRight:
                    return {
                        'move': 'east',
                        'taunt': 'SSAT Moves EAST food'
                    }
            elif ssatSnakeHead[1] != food[1]:
                if ssatSnakeHead[1] > food[1]  and (ssatSnakeHead[1]-1 != ssatSnakeBody[1]) and goUp:
                    return {
                       'move': 'north',
                        'taunt': 'SSAT Moves north'
                    }
                elif (ssatSnakeHead[1]+1 != ssatSnakeBody[1]) and goDown:
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
