#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando as bibliotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Importando o dataset

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


# In[3]:


# Implementando o modelo UCB

import math

N = 10000 # Quantidade de usuários
d = 10 # Quantidade de anúncios
ads_selected = []
numbers_of_selections = [0] * d # Cria uma lista com 10 zeros
sum_of_rewards = [0] * d # Cria uma lista com 10 zeros
total_rewards = 0
for n in range(0, N):
  ad = 0
  max_upper_bound = 0
  for i in range(0, d):
    if (numbers_of_selections[i] > 0):
      average_reward = sum_of_rewards[i] / numbers_of_selections[i]
      delta_i = math.sqrt((3/2) * (math.log(n + 1) / numbers_of_selections[i]))
      upper_bound = average_reward + delta_i
    else:
      upper_bound = 1e400
    if (upper_bound > max_upper_bound):
        max_upper_bound = upper_bound
        ad = i
  ads_selected.append(ad)
  numbers_of_selections[ad] = numbers_of_selections[ad] + 1
  reward = dataset.values[n, ad]
  sum_of_rewards[ad] = sum_of_rewards[ad] + reward
  total_rewards = total_rewards + reward


# In[4]:


# Visualizando os Resultados

plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

