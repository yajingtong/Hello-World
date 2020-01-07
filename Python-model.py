import matplotlib
matplotlib.use('TkAgg')
import random
import operator
import numpy as np
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import agentframework
import requests
import bs4
import matplotlib.animation as animation
import tkinter

#initialise the pramiters
num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood = 20

#read in environment data
f = open("in.txt")
environment=[]	
for row in f:
    parsed_row = str.split(row,",")
    rowlist = []
    for value in parsed_row:
        rowlist.append(float(value))
    environment.append(rowlist)
f.close()

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs) 
 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1]) 

carry_on=True

# Make the agents.
for i in range(num_of_agents):#use the for-loop to create agents in each iterations
    y = int(td_ys[i].text)#assign x,y coordinates  values to agents
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(x, y, environment, agents, neighbourhood))
    

#the function animation based on  
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    for i in range(num_of_agents): 
        agents[i].eat()
        agents[i].move()
        agents[i].share_with_neighbours()
    
    for i in range(num_of_agents):
        matplotlib.pyplot.xlim(0, 300)
        matplotlib.pyplot.ylim(0, 300)
        matplotlib.pyplot.imshow(environment) 
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
        print(agents[i].x,agents[i].y) 
        
#def gen_function()
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
    


'''
#draw the agents
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.show()
'''

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()

