from lxml import html, etree
import requests
from custom_modules.FileValidator import exists, is_file, is_symLink
from custom_modules.FileReader import return_lines, return_bytes, return_text
from custom_modules.FileOpener import get_file
from custom_classes.FileInterrorgator import fileinterrogator
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms


class Hscraper:
    def __init__(this):
        this.__fileinter = fileinterrogator()

    def set_file_path(this, path):
        try:
            if not exists(path):
                function = cms['warning']
                msg = 'File {} does not exist'.format(path)
                wmsg = function(msg)
                print(wmsg)
                return {'status': False, 'cause': msg}
            else:
                this.__fileinter.set_path(path)
                return {'status': True}
        except TypeError as te:
            function = cms['error']
            msg = 'Argument {} must be a string'.format(str(path))
            emsg = function(msg)
            print(emsg)
            return {'status': False, 'cause': te}

    def get_file_path(this):
        try:
            if this.__fileinter.absolute_path() != None:
                return {
                    'status': True,
                    'path': this.__fileinter.absolute_path()}
            return {
                'status': False,
                'cause': 'File path not available',
                'trace': 'get_file_path method in HtmlScraper file'
            }
        except AttributeError as ae:
            msg = 'The instance variable __fileinter has no property or method called "absolute_path". It seems that it is not initialized.'
            return {
                'status': False, 'cause': msg,
                'trace': 'HtmlScraper file, line 34.'}

    def scrape(this):
        file_path = this.get_file_path()

        if not file_path['status']:
            return {
                'status': file_path['status'],
                'cause': file_path['cause'],
                'trace': file_path['trace']}

        page = html.parse(file_path['path'])

        links = page.xpath('//@href')

        return {'status': True, 'links': links}
