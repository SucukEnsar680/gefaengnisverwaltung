import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute('SELECT Name, GID FROM Gefaengnis'))
  return res

@anvil.server.callable
def get_direktor(gefaengnis):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f'SELECT Direktor FROM Gefaengnis WHERE GID = {gefaengnis}'))
  return res[0]
  
@anvil.server.callable
def get_freieZellen(gefaengnis):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f'SELECT Anzahl_freie_Zellen FROM Gefaengnis WHERE GID = {gefaengnis}'))
  return res[0]

@anvil.server.callable
def get_zellen(gefaengnis):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f'SELECT ZID FROM Zelle WHERE GID = {gefaengnis}'))
  return res

@anvil.server.callable
def get_haeftlinge(gefaengnis):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f'SELECT Anzahl_Haeftlinge FROM Zelle WHERE GID = {gefaengnis}'))
  return res