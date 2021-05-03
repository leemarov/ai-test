#!/bin/env python3

import sys
from transformers import pipeline

context = ""
#for line in sys.stdin:
#    context += line
#nlp = nlp = pipeline("question-answering")
#context = r"""
gen = pipeline('text-generation', model='gpt2')
question = sys.argv[1] 

print("Root: "+question)
#result = nlp(question=question, context=context)
result = gen(question, do_sample=True, min_length=50)
print(result[0]['generated_text'])
#print("Answer: "+result['generated_text'])
#print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
