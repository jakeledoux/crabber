import re

mention = re.compile(
    r'(?:^|\s)(?<!\\)@([\w]{1,32})(?!\w)')
tag = re.compile(
    r'(?:^|\s)(?<!\\)%([\w]{1,16})(?!\w)')
username = re.compile(
    r'^\w+$')
spotify = re.compile(
    r'(https?://open\.spotify\.com/(?:embed/)?(\w+)/(\w+))(?:\S+)?')
youtube = re.compile(
    r'(?:https?://)?(?:www.)?(?:youtube\.com/watch\?(?:[^&]+&)*v=|youtu\.be/)(\S{11})')
giphy = re.compile(
    r'https://(?:media\.)?giphy\.com/\S+[-/](\w{13,21})(?:\S*)')
ext_img = re.compile(
    r'(https://\S+\.(gif|jpe?g|png))(?:\s|$)')
ext_link = re.compile(
    r'(?<!href=[\'"])(https?://\S+)')
ext_md_link = re.compile(
    r'\[([^\]\(\)]+)\]\((http[^\]\(\)]+)\)')
timezone = re.compile(
    r'^-?(1[0-2]|0[0-9]).\d{2}$')