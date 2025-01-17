from configparser import ConfigParser
from shutil import copy
from os import path,makedirs,remove
import time

class Config(ConfigParser):
  """loads the config file automatically and ensures it's in valid shape"""
  path = "config/"
  file = "config/config.ini"
  template = "config/config.factory.ini"

  def __init__(self):
    """
    Custom init for merelybot configparser
    will always return a valid config object, even if the filesystem is broken
    """
    ConfigParser.__init__(self)
    self.load()
  
  def load(self):
    if path.isfile(self.path):
      remove(self.path)
    if not path.exists(self.path):
      print(f"WARNING: ./{self.path} missing - creating folder and generating bare-minimum defaults, you should consider downloading and including ./{self.template}")
      makedirs(self.path)
    if not path.exists(self.file):
      if path.exists(self.template):
        print(f"WARNING: ./{self.file} missing - reverting to template config")
        copy(self.template, self.file)
      else:
        print(f"WARNING: ./{self.template} missing - resorting to bare-minimum defaults")
    ConfigParser.read(self, self.file, encoding='utf-8')

    # Ensure required sections exist and provide sane defaults
    if 'main' not in self.sections():
      self.add_section('main')
    if 'prefix_short' not in self['main']:
      self['main']['prefix_short'] = 'm/'
    if 'prefix_long' not in self['main']:
      self['main']['prefix_long'] = ''
    if 'botname' not in self['main']:
      self['main']['botname'] = 'merely framework bot'
    if 'themecolor' not in self['main']:
      self['main']['themecolor'] = '0x0'
    if 'voteurl' not in self['main']:
      self['main']['voteurl'] = ''
    if 'beta' not in self['main']:
      self['main']['beta'] = 'False'
    if 'ver' not in self['main']:
      self['main']['ver'] = ''
    if 'creator' not in self['main']:
      self['main']['creator'] = ''
    if 'intents' not in self.sections():
      self.add_section('intents')
    if 'guilds' not in self['intents']:
      self['intents']['guilds'] = 'False'
    if 'members' not in self['intents']:
      self['intents']['members'] = 'False'
    if 'bans' not in self['intents']:
      self['intents']['bans'] = 'False'
    if 'emojis' not in self['intents']:
      self['intents']['emojis'] = 'False'
    if 'integrations' not in self['intents']:
      self['intents']['integrations'] = 'False'
    if 'webhooks' not in self['intents']:
      self['intents']['webhooks'] = 'False'
    if 'invites' not in self['intents']:
      self['intents']['invites'] = 'False'
    if 'voice_states' not in self['intents']:
      self['intents']['voice_states'] = 'False'
    if 'presences' not in self['intents']:
      self['intents']['presences'] = 'False'
    if 'messages' not in self['intents']:
      self['intents']['messages'] = 'False'
    if 'guild_messages' not in self['intents']:
      self['intents']['guild_messages'] = 'False'
    if 'dm_messages' not in self['intents']:
      self['intents']['dm_messages'] = 'False'
    if 'reactions' not in self['intents']:
      self['intents']['reactions'] = 'False'
    if 'guild_reactions' not in self['intents']:
      self['intents']['guild_reactions'] = 'False'
    if 'dm_reactions' not in self['intents']:
      self['intents']['dm_reactions'] = 'False'
    if 'typing' not in self['intents']:
      self['intents']['typing'] = 'False'
    if 'guild_typing' not in self['intents']:
      self['intents']['guild_typing'] = 'False'
    if 'dm_typing' not in self['intents']:
      self['intents']['dm_typing'] = 'False'
    if 'extensions' not in self.sections():
      self.add_section('extensions')
    if 'allow_reloading' not in self['extensions']:
      self['extensions']['allow_reloading'] = 'True'
    if 'language' not in self.sections():
      self.add_section('language')
    if 'default' not in self['language']:
      self['language']['default'] = 'en'
    if 'prefix' not in self['language']:
      self['language']['prefix'] = 'en'
    if 'contribute_url' not in self['language']:
      self['language']['contribute_url'] = ''
    self.save()

  def save(self):
    if not path.exists(self.path+'config_history/'+time.strftime("%m-%y")):
      makedirs(self.path+'config_history/'+time.strftime("%m-%y"))
    if path.isfile(self.file):
      copy(self.file, self.path+'config_history/'+time.strftime("%m-%y")+'/config-'+time.strftime("%H:%M.%S-%d-%m-%y")+'.ini')
    with open(self.file, 'w', encoding='utf-8') as f:
      ConfigParser.write(self, f)
  
  def reload(self):
    for section in self.sections():
      self.remove_section(section)
    self.load()