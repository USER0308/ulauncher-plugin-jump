from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenAction import OpenAction

class JumpExtension(Extension):

    def __init__(self):
        super(JumpExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        path = event.get_argument()
        items = []
        items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='jump to ',
                                             description='jump to here and open in file',
                                             on_enter=OpenAction(path)))
#        for i in range(5):
#            items.append(ExtensionResultItem(icon='images/icon.png',
#                                             name='Item %s' % i,
#                                             description='Item description %s' % i,
#                                             on_enter=OpenAction(path)))

        return RenderResultListAction(items)

if __name__ == '__main__':
    JumpExtension().run()
