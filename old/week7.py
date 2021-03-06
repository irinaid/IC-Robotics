#!/usr/bin/python

import particles
import particles_addition
import random
import odometry
import sys

particlesList = []
#init 100 random particles 
for i in xrange(100):
  particlesList.append(particles.Particle(random.randint(5,15), random.randint(5,15), 0, 0.01))
    
#sample sonar reading
sonar = 210

for (i, p) in enumerate(particlesList):
    print "Particle", i, ":", "(",p.x,",", p.y,")"
    #l = particles_addition.calculate_likelihood(p.x, p.y, p.theta, sonar)
    l = p.calculate_likelihood(sonar)
    print 'likelihood=', l
    print
