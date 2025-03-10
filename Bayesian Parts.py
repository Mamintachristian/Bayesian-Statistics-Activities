# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 23:30:22 2025

@author: chris
"""
#March 8 Activity


import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

#prior
mu = np.linspace(1.65,1.8, num=50)
test = np.linspace(0,2)
uniform_dist = sts.uniform.pdf(mu)+1
uniform_dist = uniform_dist/uniform_dist.sum()

beta_dist = sts.beta.pdf(mu, 2,5, loc=1.65, scale = 0.2)
beta_dist = beta_dist/beta_dist.sum()
plt.figure()
plt.plot(mu, beta_dist, label = 'Beta Dist')
plt.plot(mu, uniform_dist, label = 'Uniform Dist')
plt.xlabel("Values of $mu$ in meters")
plt.ylabel("Probability Density")
plt.legend()
plt.show(block=False)
#likelihood

def likelihood_func(datum, mu):
    likelihood_out= sts.norm.pdf(datum, mu, scale=0.1)
    return likelihood_out/likelihood_out.sum()

likelihood_out=likelihood_func(1.7, mu)

plt.figure()
plt.plot(mu,likelihood_out)
plt.title("Likelihood of mu's given observation of 1.7m")
plt.ylabel("Probability Density/Likelihood")
plt.xlabel("Value of mu's")
plt.show(block=False)

#posterior
unnormalized_posterior = likelihood_out * uniform_dist
plt.figure()
plt.plot(mu, unnormalized_posterior)
plt.xlabel("mu's in meters")
plt.ylabel("Unnormalized Posterior")
plt.show()

print(unnormalized_posterior.sum())
