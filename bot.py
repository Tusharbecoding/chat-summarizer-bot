import discord
from discord.ext import commands
import google.genai as genai
import os 
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()