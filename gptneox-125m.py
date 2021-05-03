#!/bin/env python3

import sys
import time
from transformers import pipeline

timer = time.time()
context = ""
#for line in sys.stdin:
#    context += line
#nlp = nlp = pipeline("question-answering")
#context = r"""
gen = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
question = sys.argv[1] 
mlen = 100
if(len(sys.argv)>2):
    mlen = int(sys.argv[2])

print("Generated root: "+question)
#result = nlp(question=question, context=context)
result = gen(question, max_length=mlen)
#print(len(result))
print("---GENERATED TEXT--- \n"+result[0]['generated_text'])
#print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
print("\nGeneration Time: "+str(time.time()-timer))
#print(time.time()-timer)
