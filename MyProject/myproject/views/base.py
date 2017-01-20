from jinja2 import Environment,FileSystemLoader
from MyProject.myproject.shema import Data_Base

environment=Environment(loader=FileSystemLoader('routes'))

dataBase=Data_Base()