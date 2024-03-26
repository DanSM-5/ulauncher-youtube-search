from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from src.functions import strip_list
from src.items import no_input_item, no_results_item, generate_search_items
from src.youtube_search import YoutubeSearch
# from src.mpv_open import mpv_open


class YoutubeSeachExtension(Extension):
    def __init__(self):
        super(YoutubeSeachExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        # self.subscribe(ItemEnterEvent, ItemClickListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()

        if len(query.strip()) == 0:
            return RenderResultListAction(no_input_item())

        params = strip_list(query.split(' '))            

        search = YoutubeSearch(params)

        if extension.preferences['show_thumbnails'] == 'true' and search.show_thumbnails is None:
            search.show_thumbnails = True

        if not search.has_query():
            return RenderResultListAction(show_used_args(parser))

        results = search.execute()

        if not results:
            return RenderResultListAction(no_results_item())

        return RenderResultListAction(generate_search_items(results, extension.preferences['description_template']))


# class ItemClickListener(EventListener):
#     def on_event(self, event, extension):
#         data = event.get_data()
#         mpv_open(data)


if __name__ == "__main__":
    YoutubeSeachExtension().run()
