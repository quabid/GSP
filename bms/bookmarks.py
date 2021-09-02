#! /usr/bin/python3

import re
from custom_classes.HtmlScraper import Hscraper as Hs
from custom_classes.BookmarkManager import BmLister
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

bml = BmLister()
hs = Hs()

print('\n')

bookmarks = bml.bookmarks_map
function = cms['custom']
start_msg = function('\tBookmarks By Dates\n'.upper(), 244, 230, 109)
print(start_msg)
print(*bookmarks, sep="\n")
print('\n')

res = bml.get_bookmark(input(str("\tEnter which date from above:\t")))

if res['status']:
    hs.set_file_path(res['bookmark'])
    scrape_results = hs.scrape()

    if not scrape_results['status']:
        emsg = cms['error']
        cmsg = cms['custom']

        print('\n\t{}\n\t{}'.format(
            emsg(scrape_results['cause']), cmsg(scrape_results['trace'])))
    else:
        search_term = input(str("\n\tEnter one or more search words:\t"))
        links = scrape_results['links']
        
        function = cms['custom']

        search_msg = function('Searching bookmark: {}\n'.format(
            hs.get_file_path()['path']), 224, 200, 0)

        print(search_msg)

        search_term_pattern = re.compile('[.]*('+search_term+')[.]*')
        found = []

        for i, l in enumerate(links):
            matched = search_term_pattern.search(l)

            if matched != None:
                found.append(l)

        if len(found) > 0:
            function = cms['success']

            success_msg = function('\t\tSearch Term {} Found\n'.format(
                search_term.upper()))

            print(success_msg)

            print(*found, sep='\n')

            print('\n\n')
        else:
            function = cms['error']
            error_msg = function(
                '\t\tSearch Term {} Not Found\n\n'.format(search_term.upper()))
            print(error_msg)

else:
    function = cms['custom']
    wmsg = function(res['cause'].title(), 239, 190, 88)
    print('\n{}\n'.format(wmsg))
