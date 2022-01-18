#!/usr/bin/env python
# coding: utf-8

# Assignment  8
# 
# 1. A crime is committed by one of two suspects, A and B. Initially, there is equal evidence against both of them.
# In further investigation at the crime scene, it is found that the guilty party had a blood type found in 10% of the population. 
# Suspect A does match this blood type, whereas the blood type of Suspect B is unknown.
# 
# (a) Given this new information, what is the probability that A is the guilty party?
# 
# (b) Given this new information, what is the probability that B’s blood type matches that found at the crime scene?
# 
# Ans
# 
# Define events
# 
# A: {A is guilty}
# 
# B: {B is Guilty}
# 
# MA = {A's Blood matches the guilty party}
# 
# MB = {B's Blood matches the guilty party}
# 
# (a) we want to calculate P(A/MA) .Use Byes rule to Calculcate
# 
# P(A/MA) =  P(MA|A)P(A)/P(MA|A)P(A)+P(MA|B)P(B) 
# 
# (1.1/2)/(1.1/2)+(1/10* 1/2) =  10/11
# 
# b  we wan to calculate P(MB/MA). Use Lots to obtain
# 
# P(MB|MA) = P(MB|MA.A)P(A|MA)+P(MB/MB.A)P(B|MA)
# 
# = 1/10*10/11 + 1.1/11 = 2/11
