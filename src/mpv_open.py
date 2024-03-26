# import json
import os
import platform
# import struct
import sys
import subprocess


# Based on ff2mpv backend
def mpv_open(data):
    url = data['url']

    args = ["mpv", "--no-terminal", "--", url]
    kwargs = {}

    device = platform.system()
    # https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging#Closing_the_native_app
    if device == "Windows":
        kwargs["creationflags"] = subprocess.CREATE_BREAKAWAY_FROM_JOB

    # HACK(ww): On macOS, graphical applications inherit their path from `launchd`
    # rather than the default path list in `/etc/paths`. `launchd` doesn't include
    # `/usr/local/bin` in its default list, which means that any installations
    # of MPV and/or youtube-dl under that prefix aren't visible when spawning
    # from, say, Firefox. The real fix is to modify `launchd.conf`, but that's
    # invasive and maybe not what users want in the general case.
    # Hence this nasty hack.
    if device == "Darwin":
        path = os.environ.get("PATH")
        os.environ["PATH"] = f"/usr/local/bin:/opt/homebrew/bin:{path}"

    if device == "Linux":
        kwargs["start_new_session"] = True

    p = subprocess.Popen(args, **kwargs)
    # print("PID:", p.pid)

