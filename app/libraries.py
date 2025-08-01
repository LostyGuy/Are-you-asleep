import os
import sys
import time as t
import tkinter as tk
from tkinter import messagebox
from multiprocessing import Process
import logging as log
import shutil

# Creating Virtual Environment: python -m venv .venv
# Activating Virtual Environment: .venv\Scripts\activate

# Get requirements: pip freeze > requirements.txt
# Installing Dependencies: pip install -r requirements.txt