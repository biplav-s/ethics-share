#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 20:57:58 2019

"""

import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
#%%


#for insurance
bias=pd.read_csv('../bias/insurance_dataset_scaled_clipped.csv')
bias["bias_rating"][bias["bias_rating"]=="none"]=0

abusive=pd.read_csv('../abuse/hate-speech-results/[scaled] [hate-speech-output] insurance_dataset.csv')
complexity=pd.read_csv('../complex/insurance_dataset_complexities.csv')
result = pd.merge(bias, abusive, on=['row'])
result = pd.merge(result, complexity, on=['row'])
result["privacy_rating"]='M'
result["bias_rating_discrete"]='0'
result["abusive_language_discrete"]='0'
result["dialog_complexity_discrete"]='0'

result["bias_rating"]=result["bias_rating"].astype(float)
result["score"]=result["score"].astype(float)
result["dialog_complexity"]=result["dialog_complexity"].astype(float)

result["abusive_language_discrete"][result["score"] < 0.33]='L'
result["abusive_language_discrete"][(result["score"] >= 0.33) & (result["score"] <= 0.67)]='M'
result["abusive_language_discrete"][result["score"] > 0.67]='H'

result["dialog_complexity_discrete"][result["dialog_complexity"] < 0.33]='L'
result["dialog_complexity_discrete"][(result["dialog_complexity"] >= 0.33) & (result["dialog_complexity"] <= 0.67)]='M'
result["dialog_complexity_discrete"][result["dialog_complexity"] > 0.67]='H'

result["bias_rating_discrete"][result["bias_rating"] < 0.33]='L'
result["bias_rating_discrete"][(result["bias_rating"] >= 0.33) & (result["bias_rating"] <= 0.67)]='M'
result["bias_rating_discrete"][result["bias_rating"] > 0.67]='H'

print(bias.shape)
print(abusive.shape)
print(result.shape)
result=result[["row","dialog_ID_x","speaker_x","utterance_x","bias_rating","score","dialog_complexity","privacy_rating","abusive_language_discrete","dialog_complexity_discrete","bias_rating_discrete"]]
result.columns = ["row_id","dialog_ID","speaker","utterance","bias_rating","abusive_language_rating","dialog_complexity_rating","privacy_rating","abusive_language_discrete","dialog_complexity_discrete","bias_rating_discrete"]
result.to_csv("./output/combined_discrete_insurance.csv")
#%%

#for ubuntu
bias=pd.read_csv('../bias/ubuntu_dataset_scaled_clipped.csv')
bias["bias_rating"][bias["bias_rating"]=="none"]=0
abusive=pd.read_csv('../abuse/hate-speech-results/[scaled] [hate-speech-output] ubuntu_dataset.csv')
complexity=pd.read_csv('../complex/ubuntu_dataset_complexities.csv')
result = pd.merge(bias, abusive, on=['row'])
result = pd.merge(result, complexity, on=['row'])
result["privacy_rating"]='0'
result["bias_rating_discrete"]='0'
result["abusive_language_discrete"]='0'
result["dialog_complexity_discrete"]='0'

result["biaprivacy_ratings_rating"]=result["bias_rating"].astype(float)
result["bias_rating"]=result["bias_rating"].astype(float)
result["score"]=result["score"].astype(float)
result["dialog_complexity"]=result["dialog_complexity"].astype(float)

result["abusive_language_discrete"][result["score"] < 0.33]='L'
result["abusive_language_discrete"][(result["score"] >= 0.33) & (result["score"] <= 0.67)]='M'
result["abusive_language_discrete"][result["score"] > 0.67]='H'

result["dialog_complexity_discrete"][result["dialog_complexity"] < 0.33]='L'
result["dialog_complexity_discrete"][(result["dialog_complexity"] >= 0.33) & (result["dialog_complexity"] <= 0.67)]='M'
result["dialog_complexity_discrete"][result["dialog_complexity"] > 0.67]='H'

result["bias_rating_discrete"][result["bias_rating"] < 0.33]='L'
result["bias_rating_discrete"][(result["bias_rating"] >= 0.33) & (result["bias_rating"] <= 0.67)]='M'
result["bias_rating_discrete"][result["bias_rating"] > 0.67]='H'

print(bias.shape)
print(abusive.shape)
print(result.shape)
result=result[["row","dialog_ID_x","speaker_x","utterance_x","bias_rating","score","dialog_complexity","privacy_rating","abusive_language_discrete","dialog_complexity_discrete","bias_rating_discrete"]]
result.columns = ["row_id","dialog_ID","speaker","utterance","bias_rating","abusive_language_rating","dialog_complexity_rating","privacy_rating","abusive_language_discrete","dialog_complexity_discrete","bias_rating_discrete"]
result.to_csv("./output/combined_discrete_ubuntu.csv")
#%%

#for restaurant
bias=pd.read_csv('../bias/DSTC_dataset_scaled_clipped.csv')
bias["bias_rating"][bias["bias_rating"]=="none"]=0
abusive=pd.read_csv('../abuse/hate-speech-results/[scaled] [hate-speech-output] DSTC_dataset.csv')
complexity=pd.read_csv('../complex/DSTC_dataset_complexities.csv')
result = pd.merge(bias, abusive, on=['row'])
result = pd.merge(result, complexity, on=['row'])
result["privacy_rating"]='M'
result["bias_rating_discrete"]='0'
result["abusive_language_discrete"]='0'
result["dialog_complexity_discrete"]='0'

result["bias_rating"]=result["bias_rating"].astype(float)
result["score"]=result["score"].astype(float)
result["dialog_complexity"]=result["dialog_complexity"].astype(float)

result["abusive_language_discrete"][result["score"] < 0.33]='L'
result["abusive_language_discrete"][(result["score"] >= 0.33) & (result["score"] <= 0.67)]='M'
result["abusive_language_discrete"][result["score"] > 0.67]='H'

result["dialog_complexity_discrete"][result["dialog_complexity"] < 0.33]='L'
result["dialog_complexity_discrete"][(result["dialog_complexity"] >= 0.33) & (result["dialog_complexity"] <= 0.67)]='M'
result["dialog_complexity_discrete"][result["dialog_complexity"] > 0.67]='H'

result["bias_rating_discrete"][result["bias_rating"] < 0.33]='L'
result["bias_rating_discrete"][(result["bias_rating"] >= 0.33) & (result["bias_rating"] <= 0.67)]='M'
result["bias_rating_discrete"][result["bias_rating"] > 0.67]='H'

print(bias.shape)
print(abusive.shape)
print(result.shape)
result=result[["row","dialog_ID_x","speaker_x","utterance_x","bias_rating","score","dialog_complexity","privacy_rating","abusive_language_discrete","dialog_complexity_discrete","bias_rating_discrete"]]
result.columns = ["row_id","dialog_ID","speaker","utterance","bias_rating","abusive_language_rating","dialog_complexity_rating","privacy_rating","abusive_language_discrete","dialog_complexity_discrete","bias_rating_discrete"]
result.to_csv("./output/combined_discrete_restaurant.csv")
#%%

#for HRbot
bias=pd.read_csv('../bias/HRbot_dataset_scaled_clipped.csv')
bias["bias_rating"][bias["bias_rating"]=="none"]=0
abusive=pd.read_csv('../abuse/hate-speech-results/[scaled] [hate-speech-output] HRbot_dataset.csv')
complexity=pd.read_csv('../complex/HRbot_dataset_complexities.csv')
result = pd.merge(bias, abusive, on=['row'])
result = pd.merge(result, complexity, on=['row'])
result["privacy_rating"]='0'
result["bias_rating_discrete"]='0'
result["abusive_language_discrete"]='0'
result["dialog_complexity_discrete"]='0'

result["privacy_rating"]=result["privacy_rating"].astype(float)
result["bias_rating"]=result["bias_rating"].astype(float)
result["score"]=result["score"].astype(float)
result["dialog_complexity"]=result["dialog_complexity"].astype(float)

result["abusive_language_discrete"][result["score"] < 0.33]='L'
result["abusive_language_discrete"][(result["score"] >= 0.33) & (result["score"] <= 0.67)]='M'
result["abusive_language_discrete"][result["score"] > 0.67]='H'

result["dialog_complexity_discrete"][result["dialog_complexity"] < 0.33]='L'
result["dialog_complexity_discrete"][(result["dialog_complexity"] >= 0.33) & (result["dialog_complexity"] <= 0.67)]='M'
result["dialog_complexity_discrete"][result["dialog_complexity"] > 0.67]='H'

result["bias_rating_discrete"][result["bias_rating"] < 0.33]='L'
result["bias_rating_discrete"][(result["bias_rating"] >= 0.33) & (result["bias_rating"] <= 0.67)]='M'
result["bias_rating_discrete"][result["bias_rating"] > 0.67]='H'

print(bias.shape)
print(abusive.shape)
print(result.shape)
result=result[["row","dialog_ID_x","speaker_x","utterance_x","bias_rating","score","dialog_complexity","privacy_rating","abusive_language_discrete","dialog_complexity_discrete","bias_rating_discrete"]]
result.columns = ["row_id","dialog_ID","speaker","utterance","bias_rating","abusive_language_rating","dialog_complexity_rating","privacy_rating","abusive_language_discrete","dialog_complexity_discrete","bias_rating_discrete"]
result.to_csv("./output/combined_discrete_HRbot.csv")
#%%


#rating for profile 1 (CC, AL, B, IL)
imp_cc=1
imp_al=2
imp_b=3
imp_il=4

#rating for profile 2 (B, CC, AL, IL)
#imp_b=1
#imp_cc=2
#imp_al=3
#imp_il=4

#rating for profile 3 (IL, AL, B, CC)
#imp_il=1
#imp_al=2
#imp_b=3
#imp_cc=4

#rating for profile 4 (AL, CC, B, IL)
#imp_al=1
#imp_cc=2
#imp_b=3
#imp_il=4


final_c_l=0
final_c_m=0
final_c_h=0

for index, row in result.iterrows():
    c_l=0
    c_m=0
    c_h=0
    if row["bias_rating_discrete"]=='L':
        c_l=c_l+(4-imp_b)
    if row["bias_rating_discrete"]=='M':
        c_m=c_m+(4-imp_b)
    if row["bias_rating_discrete"]=='H':
        c_h=c_h+(4-imp_b)
    if row["abusive_language_discrete"]=='L':
        c_l=c_l+(4-imp_al)
    if row["abusive_language_discrete"]=='M':
        c_m=c_m+(4-imp_al)
    if row["abusive_language_discrete"]=='H':
        c_h=c_h+(4-imp_al)
    if row["dialog_complexity_discrete"]=='L':
        c_l=c_l+(4-imp_cc)
    if row["dialog_complexity_discrete"]=='M':
        c_m=c_m+(4-imp_cc)
    if row["dialog_complexity_discrete"]=='H':
        c_h=c_h+(4-imp_cc)
    if row["privacy_rating"]=='L':
        c_l=c_l+(4-imp_il)
    if row["privacy_rating"]=='M':
        c_m=c_m+(4-imp_il)
    if row["privacy_rating"]=='H':
        c_h=c_h+(4-imp_il)
    var = {c_l:"L",c_m:"M",c_h:"H"}
    agg= var.get(max(var))
    if agg=="L":
        final_c_l=final_c_l+1
    if agg=="M":
        final_c_m=final_c_m+1
    if agg=="H":
        final_c_h=final_c_h+1
print(final_c_l)
print(final_c_m)
print(final_c_h)
#result["bias_rating"]=result["bias_rating"].astype(float)
#rating1=((result["dialog_complexity_rating"]).mean()*(4-imp_cc))+((result["abusive_language_rating"]).mean()*(4-imp_al))+((result["bias_rating"]).mean()*(4-imp_b))+((result["privacy_rating"]).mean()*(4-imp_il))
#dialog_rating=((result["dialog_complexity_rating"])*(4-imp_cc))+((result["abusive_language_rating"])*(4-imp_al))+((result["bias_rating"])*(4-imp_b))+((result["privacy_rating"])*(4-imp_il))
#rating2=dialog_rating.mean()
#print(rating2)

#%%
c_l=8
c_m=8
c_h=2
var = {c_l:"L",c_m:"M",c_h:"H"}
agg= var.get(max(var))
print(agg)

#%%
#rating for profile 2 (B, CC, AL, IL)
imp_b=1
imp_cc=2
imp_al=3
imp_il=4
#rating1=((result["dialog_complexity_rating"]).mean()*(4-imp_cc))+((result["abusive_language_rating"]).mean()*(4-imp_al))+((result["bias_rating"]).mean()*(4-imp_b))+((result["privacy_rating"]).mean()*(4-imp_il))
dialog_rating=((result["dialog_complexity_rating"])*(4-imp_cc))+((result["abusive_language_rating"])*(4-imp_al))+((result["bias_rating"])*(4-imp_b))+((result["privacy_rating"])*(4-imp_il))

rating2=dialog_rating.mean()
print (str(rating2))

#%%
#rating for profile 3 (IL, AL, B, CC)
imp_il=1
imp_al=2
imp_b=3
imp_cc=4
#rating1=((result["dialog_complexity_rating"]).mean()*(4-imp_cc))+((result["abusive_language_rating"]).mean()*(4-imp_al))+((result["bias_rating"]).mean()*(4-imp_b))+((result["privacy_rating"]).mean()*(4-imp_il))
dialog_rating=((result["dialog_complexity_rating"])*(4-imp_cc))+((result["abusive_language_rating"])*(4-imp_al))+((result["bias_rating"])*(4-imp_b))+((result["privacy_rating"])*(4-imp_il))


rating2=dialog_rating.mean()
print (str(rating2))
