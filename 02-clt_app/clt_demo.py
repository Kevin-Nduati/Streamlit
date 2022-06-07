import streamlit as st
import numpy as np
"""
We will generate a distribution that we want to sample from with replacement. 
We will choose the binomial type
We can read the following code as simulating 1000 coin flips
And printing out the mean number of heads from those 1000 coin flips
"""

binom_dist = np.random.binomial(1, 0.5, 100)
st.write("The mean is", np.mean(binom_dist))

""""
Given what we all know about the central limit theorem,
wewould expect that if we sampled from binom_dist enough times,
the mean of those samples would be approximately the
normal distribution 


The next foray into writing content to the streamlit app
is through graphs. *st.pyplot()* is a function that lets us
use all the power of the popular mtplotlib library and push our
matplotlib graph to streamlit. Once we create a figure in matplotlib
, we can explicitly tell streamlit to write to our app
with that function


This app simulates 1000 coin flips and stores those values
in a list we call binomial_dist. We then sample 100 with replacement
fromthat list, take the mean, and store that mean in list_of_means
After we do this, the result should show a bell-shaped distribution
"""

import matplotlib.pyplot as plt
list_of_means = []
for i in range(0,1000):
    list_of_means.append(np.random.choice(binom_dist, 100,
    replace=True).mean())

fig, axs = plt.subplots()
axs = plt.hist(list_of_means)
st.pyplot(fig)

"""
We assumed coins flipped had a 50/50 chance of being heads/tails
Let us let the user deide the percentage chance of heads is,
and then using that as an input to our binomial distribution"""
st.title('Illustrating the Central Limit Theorem with Streamlit')
st.subheader('An app by Kevin Kamau')
perc_heads = st.number_input(
    label = 'Chance of Coins Landing on Heads',
    min_value = 0.0,
    max_value = 1.0,
    value = 0.5
)
title = st.text_input(label="Graph Input")
binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []
for i in range(0,1000):
    list_of_means.append(np.random.choice(binom_dist, 100,
    replace=True).mean())

fig, axs = plt.subplots()
axs = plt.hist(list_of_means)
plt.title(title)
st.pyplot(fig)

