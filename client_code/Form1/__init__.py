from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.label_direktor.text = anvil.server.call('get_direktor', self.gefaengnisse_drop_down.selected_value) 
    self.label_freie_zellen.text = anvil.server.call('get_freieZellen', self.gefaengnisse_drop_down.selected_value)
    zellen = list()
    
    zellen = anvil.server.call('get_zellen', self.gefaengnisse_drop_down.selected_value)
    haeftlinge = anvil.server.call('get_haeftlinge', self.gefaengnisse_drop_down.selected_value)
    laenge = 0
    liste = list()
    for i in zellen:
      laenge += 1
    print (laenge)
    for i in range(laenge):
      liste.append({'zellennummer': f'{str(zellen[i])}', 'anzahl_häftlinge': f'{str(haeftlinge[i])}'})

    print(liste)
    self.repeating_zellen.items = liste  
                                   
    

  def gefaengnisse_drop_down_change(self, **event_args):
    self.label_direktor.text = anvil.server.call('get_direktor', self.gefaengnisse_drop_down.selected_value)
    self.label_freie_zellen.text = anvil.server.call('get_freieZellen', self.gefaengnisse_drop_down.selected_value)
    zellen = list()
    zellen = anvil.server.call('get_zellen', self.gefaengnisse_drop_down.selected_value)
    haeftlinge = anvil.server.call('get_haeftlinge', self.gefaengnisse_drop_down.selected_value)
    laenge = 0
    liste = list()
    for i in zellen:
      laenge += 1
    print (laenge)
    for i in range(laenge):
      liste.append({'zellennummer': f'{str(zellen[i])}', 'anzahl_häftlinge': f'{str(haeftlinge[i])}'})

    print(liste)
    self.repeating_zellen.items = liste  

 



  
 
