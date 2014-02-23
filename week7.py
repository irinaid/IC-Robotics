import particles
import particles_addition
import random
import odometry

particlesList = []
#init 100 random particles 
for i in xrange(5):
  particlesList.append(particles.Particle(random.randint(1,10), random.randint(1,10), 0, 0.01))
    
#sample sonar reading
sonar = 200

print "Sonar :", sonar
for (i, p) in enumerate(particlesList):
    print "Particle", i, ":"
    print particles_addition.calculate_likelihood(p.x, p.y, p.theta, sonar)
    print "x:", p.x, "y:", p.y
    print
