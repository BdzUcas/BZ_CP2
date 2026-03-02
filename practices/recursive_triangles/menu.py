from helper import *
from drawing import *
#make list of colors and depth dictionary
colors = ['aquamarine','azure','beige','bisque','black','blanched almond','blue','blue violet','brown','chocolate','coral','chartreuse','cornsilk','cyan','crimson','dark blue','dark cyan','dark golden rod','dark gray','dark grey','dark green','dark khaki','dark magenta','dark olive green','dark orange','dark orchid','dark red','dark salmon','dark violet','dim gray','dim grey','forest green','fuchsia','firebrick','gold','gray','grey','indigo','honeydew','HotPink','ivory','khaki','lavender','lawngreen','magenta','maroon','navy','orange','orchid','peru','pink','plum','purple','red','salmon','sienna','snow','tan','thistle','tomato','turquoise','violet','wheat','white','yellow']
depth_max = {'1':8,'2':5}
#menu function
def menu():
    #welcome user to the program
    print('Welcome to the fractal shape generator!')
    #loop forever
    while True:
        #ask user which fractal to draw
        print('Which fractal do you want to draw?\n1. Serpinski Triangle\n2.Koch Snowflake')
        fractal = choice_input(['1','2'])
        #ask user for recursion depth
        print(f'What depth of recursion do you want? (1 - {depth_max[fractal]})')
        depth = int_input(max = depth_max[fractal],min = 1)
        #ask user for fractal color
        print('What color do you want the shape to be? (red, cyan, beige, etc.)')
        color = choice_input(colors)
        #ask user for background color
        print('What color do you want the background to be?')
        back = choice_input(colors)
        #setup screen
        screen_setup(back)
        #draw fractal
        print('drawing fractal...')
        match fractal:
            case '1':
                size = 1200
                #calculate height using pythagorean theorum
                height = math.sqrt(size ** 2 - (size / 2) ** 2)
                #set startx and starty
                startx = 0
                starty = 0 - height / 2
                #draw largest triangle
                main_triangle(startx,starty,size,color)
                #draw fractal triangles
                triangle(startx,starty,size/2,2,depth,color)
            case '2':
                koch_triangle(0,-250,120,'right',480,1,depth,color)
        #ask user if they want to exit
        print('done! Press enter to continue, or type "exit" to exit the program.')
        done = input('> ').lower()
        if done == 'exit':
            return
menu()