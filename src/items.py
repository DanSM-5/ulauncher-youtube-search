from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
# from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from shutil import which


ICON_FILE = 'images/icon.png'


def no_input_item():
    return [
        ExtensionResultItem(
            icon=ICON_FILE,
            name='No input',
            on_enter=DoNothingAction()
        )
    ]


def no_results_item():
    return [
        ExtensionResultItem(
            icon=ICON_FILE,
            name='No results',
            on_enter=DoNothingAction()
        )
    ]


def generate_description(template, search):
    for key in search.keys():
        template = template.replace('{' + key + '}', str(search[key] or '∅'), 1)

    return template


def generate_search_item(search, description_template):
    url = search['url']
    action = RunScriptAction(f"mpv --no-terminal -- {url}") if which('mpv') else OpenUrlAction(url)

    return ExtensionResultItem(
        icon=search['thumbnail'] or ICON_FILE,
        name=search['title'],
        description=generate_description(description_template, search),
        # Original call
        # on_enter=OpenUrlAction(search['url'])
        # Attempt to run using subprocess.Popen
        # on_enter=ExtensionCustomAction({ 'url': search['url'] })
        on_enter=action
    )


def generate_search_items(results, description_template):
    return [
        generate_search_item(search, description_template)
    for search in results]
