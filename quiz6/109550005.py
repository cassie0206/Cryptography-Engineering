#!/bin/python

import string
import math
import random
import numpy as np

def create_cipher_dict(key):
    cipher_dict = {}
    alphabet_list = list(string.ascii_uppercase)
    #print(len(key))
    for i in range(len(key)):
        cipher_dict[alphabet_list[i]] = key[i]

    return cipher_dict

def decrypt(text, key):
    cipher_dict = create_cipher_dict(key)
    text = list(text)
    newtext = ""
    for elem in text:
        if elem.upper() in cipher_dict:
            newtext += cipher_dict[elem.upper()]
        else:
            newtext += " "
    return newtext

# This function takes input as a path to a long text and creates scoring_params dict which contains the
# number of time each pair of alphabet appears together
# Ex. {'AB':234,'TH':2343,'CD':23 ..}
# Note: Take whitespace into consideration

def create_scoring_params_dict(longtext_path):
    #TODO
    
    with open(longtext_path, 'r', encoding="utf-8") as f:
        line_list = f.readlines()
        dic = {}
        
        for text in line_list:
            text = text.strip()
            text = [alp for alp in text if text not in string.punctuation]
            for i in range(len(text) - 1):
                bistr = text[i].upper() + text[i+1].upper()
                if bistr not in dic:
                    dic[bistr] = 1
                else:
                    dic[bistr] += 1
                   
    #print(dic)        
    return dic

# This function takes input as a text and creates scoring_params dict which contains the
# number of time each pair of alphabet appears together
# Ex. {'AB':234,'TH':2343,'CD':23 ..}
# Note: Take whitespace into consideration

def score_params_on_cipher(text):
    #TODO    
    dic = {}
        
    for i in range(len(text) - 1):
        bistr = text[i].upper() + text[i+1].upper()
        if bistr not in dic:
            dic[bistr] = 1
        else:
            dic[bistr] += 1
            
    return dic

# This function takes the text to be decrypted and a cipher to score the cipher.
# This function returns the log(score) metric

def get_cipher_score(text,cipher,scoring_params):
    #TODO
    
    plain = decrypt(text, cipher)
    ref_dic = scoring_params
    plain_dic = score_params_on_cipher(plain)
    score = 0
    
    for key, val in plain_dic.items():
        if key in ref_dic:
            score += val*math.log(ref_dic[key])
            
    return score


# Generate a proposal cipher by swapping letters at two random location
def generate_cipher(cipher):
    #TODO
    
    #pos1 = random.randrange(0, len(cipher) - 1)
    #pos2 = random.randrange(0, len(cipher) - 1)
    pos1 = random.randint(0, len(cipher) - 1)
    pos2 = random.randint(0, len(cipher) - 1)
    
    
    if pos1 == pos2:
        generate_cipher(cipher)
    else:
        cipher = list(cipher)
        tmp = cipher[pos1]
        cipher[pos1] = cipher[pos2]
        cipher[pos2] =tmp
        
    return "".join(cipher)

# Toss a random coin with probability of head p. If coin comes head return true else false.
def random_coin(p):
    #TODO
    
    pr = random.random()
    if pr > p:
        return False
    else:
        return True
    

# Takes input as a text to decrypt and runs a MCMC algorithm for n_iter. Returns the state having maximum score and also
# the last few states
def MCMC_decrypt(n_iter,cipher_text,scoring_params):
    current_cipher = string.ascii_uppercase # Generate a random cipher to start
    best_state = ''
    score = 0
    for i in range(n_iter):
        proposed_cipher = generate_cipher(current_cipher)
        score_current_cipher = get_cipher_score(cipher_text,current_cipher,scoring_params)
        score_proposed_cipher = get_cipher_score(cipher_text,proposed_cipher,scoring_params)     
        try:
            acceptance_probability = min(1,np.exp(score_proposed_cipher-score_current_cipher))
        except OverflowError:
            acceptance_probability = 1
        if score_current_cipher>score:
            best_state = current_cipher
        if random_coin(acceptance_probability):
            current_cipher = proposed_cipher
        if i%500==0:
            print("iter",i,":",decrypt(cipher_text,current_cipher)[0:99])
    return best_state

def main():
    ## Run the Main Program:
    
    #reference
    scoring_params = create_scoring_params_dict('war_and_peace.txt')

    with open('ciphertext.txt','r') as f:
        cipher_text = f.read()
    #print(cipher_text)

    #print("Text To Decode:", cipher_text)
    #print("\n")
    best_state = MCMC_decrypt(10000,cipher_text,scoring_params)
    #print("\n")
    plain_text = decrypt(cipher_text,best_state)
    #print("Decoded Text:",plain_text)
    #print("\n")
    #print("MCMC KEY FOUND:",best_state)

    with open('plaintext.txt','w+') as f:
        f.write(plain_text)


if __name__ == '__main__':
    main()
