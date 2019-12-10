import matplotlib
import numpy as np
import tkinter
import requests
import bs4
matplotlib.use('TkAgg')
import random
import operator
import matplotlib.pyplot
import newagentframework as agentframework
import matplotlib.animation as animation


r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


#reads in environmental data
f = open("in.txt")
environment=[]	
for row in f:
    parsed_row = str.split(row,",")
    rowlist = []
    for value in parsed_row:
        rowlist.append(float(value))
    environment.append(rowlist)
#'print(environment)


#initialising paramitters
num_of_agents = 100
num_of_iterations = 10
agents = []
neighbourhood = 20

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i, agents, environment,x,y))


   
#print(agents)
print(agents[0])
print(agents[1])
print(agents[num_of_agents - 1])
'''
# Move the agents.
for j in range(num_of_iterations):
    alreadyshared = []
      
    for i in range(num_of_agents):
        agents[i].move()
#agents eat
    for i in range(num_of_agents):
   
        agents[i].eat()
#agents share with neighbours(neighbourhood)
    for i in range(num_of_agents):
       
        ashared = agents[i].share_with_neighbours(neighbourhood, alreadyshared)
        alreadyshared.append(ashared)
print(agents[0])
print(agents[1])
print(agents[num_of_agents - 1])
'''
#create a plot
fig = matplotlib.pyplot.figure(figsize=(100, 100))
ax = fig.add_axes([0, 0, 1, 1])


def update(frame_number):
    
    fig.clear()   
    
    for i in range(num_of_iterations):
        alreadyshared = []
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhood
#agents share with neighbours(neighbourhood)
    for i in range(num_of_agents):
        ashared = agents[i].share_with_neighbours(neighbourhood, alreadyshared)
        alreadyshared.append(ashared) 
        
    matplotlib.pyplot.show(environment)
   
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
    #matplotlib.pyplot.show()
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
matplotlib.pyplot.draw()
    


#draw a scatterplot 
'''        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.draw()
'''
ani = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations,interval=2, repeat=False)
#matplotlib.pyplot.show(environment)








#save as animation

'''
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
a = agentframework.Agent(environment)
print(a.y, a.x)
a.move()
print(a.y, a.x)


# Calculate distance between each agent
def calcutalte_distance(self, environment):
    for agent in self.agents:
        dist = self.distance_between(agent)
        if dist <= environment:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave


distances=[]
for self in agents:
    distance=[]
    for a in agents:
        distance.append(distance_between(self,a))
        distances.append(distance)
print("sharing" + str(dist) + " " + str(ave))


      
print(distances)
'''    


