#!/bin/env python3

import sys
from transformers import pipeline

question = sys.argv[1] 

generator = pipeline('text-generation', model='huggingtweets/realdonaldtrump')
result = generator(question)
print(result[0]['generated_text'])
