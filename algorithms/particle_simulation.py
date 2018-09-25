from matplotlib import pyplot as plt
from matplotlib import animation

class Particle(object):

    def __init__(self,x,y,ang_speed):
        self.x = x
        self.y = y
        self.ang_speed = ang_speed

class ParticleSimulator(object):

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        

        for i in range(nsteps):
            for p in self.particles:
                # calculate direction
                norm = (p.x**2 + p.y**2)**0.5
                v_x = (-p.y)/norm
                v_y = p.x/norm

                # calculate displacement
                d_x = timestep * p.ang_speed * v_x
                d_y = timestep * p.ang_speed * v_y

                p.x += d_x
                p.y += d_y

def visualize(simulator):

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect = 'equal')
    line, = ax.plot(X,Y, 'ro')

    plt.xlim(-1,1)
    plt.ylim(-1,1)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        simulator.evolve(0.1)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func = init,
                                   blit = False, interval = 10)
    plt.show()

def test_visualize():
    particles = [ Particle(0.3,0.5,+1),
                  Particle(0.0,-0.5, -1),
                  Particle(-0.1,-0.4, +3)]
                  
    simulator = ParticleSimulator(particles)
    visualize(simulator)

if __name__ == '__main__':
    test_visualize()
