from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenAction import OpenAction

from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from list_choice import List_choice
import sys
import os
import subprocess

class JumpExtension(Extension):

    def __init__(self):
        super(JumpExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        path = event.get_argument()
        print "path is %s " % path
        query_result = List_choice().get_top_five(path)
        items = []
        for i in range(len(query_result)):
            print "get result %d" % i
            print "it is %s" %query_result[i]
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='jump to %s' % query_result[i][0],
                                             description='jump to here and open in file',
                                             on_enter=ExtensionCustomAction(query_result[i][0])))
#        for i in range(5):
#            items.append(ExtensionResultItem(icon='images/icon.png',
#                                             name='Item %s' % i,
#                                             description='Item description %s' % i,
#                                             on_enter=OpenAction(path)))

        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data() or ""
        print "data is %s " % data
        List_choice().write_path(data)
        print "before OpenAction"
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', data))
        #elif os.name == 'nt':
        #    os.startfile(data)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', data))
        print "after OpenAction"
        #return RenderResultListAction([])


if __name__ == '__main__':
    JumpExtension().run()