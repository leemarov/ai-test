#!/bin/env python3

import sys
from transformers import pipeline

context = ""
for line in sys.stdin:
    context += line
nlp = nlp = pipeline("question-answering")
#context = r"""
question = sys.argv[1] 

print("Question: "+question)
result = nlp(question=question, context=context)
print("Answer: "+result['answer'])
#print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
