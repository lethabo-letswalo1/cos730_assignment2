import random
import streamlit as st

class Reviewer:
    def __init__(self, name):
        self.name = name

    def submit_score(self):
        score = random.randint(40, 100)
        print(f"{self.name} submits score {score}")
        return score