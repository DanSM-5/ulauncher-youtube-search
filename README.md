# Youtube Search

This is a Ulauncher extension to search on Youtube.

## About this fork

This fork works same as original from [NastuzziSamy](https://github.com/NastuzziSamy/ulauncher-youtube-search) but it will prefer opening videos in MPV rather than in the browser.

If you haven't installed `mpv` or it is not available in the PATH, the behavior will fallback to open the video in the browser.

## Table of Contents

- [Youtube Search](#youtube-search)
  - [About this fork](#about-this-fork)
  - [Table of Contents](#table-of-contents)
  - [Screenshot](#screenshot)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Ulauncher's GUI](#ulaunchers-gui)
    - [Manually from source](#manually-from-source)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [License](#license)

## Screenshot

![Screenshot](images/screenshot.png)

## Installation

### Requirements

No external modules are required.

### Ulauncher's GUI

1. Open Ulauncher's settings and the "Extensions" tab
2. Click "Add extension" button
3. Paste this URL: `https://github.com/NastuzziSamy/ulauncher-youtube-search`
4. Click "Add" button – the extension will be installed

### Manually from source

The extensions' directory is located at: `$HOME/.local/share/ulauncher/extensions`

Go to that location, and while being inside, just `git clone` this repository.

## Configuration

In Ulauncher's settings, you can custom some settings:
- Keyword
  - default: `yt`

- Template: define how description must be generated based on video information
  - default: `{duration} • {views} • {channel} • {date}`
  - template keys:
    - duration: video duration
    - date: publication date
    - views: views counter
    - channel: channel publisher
    - url: youtube video url
    - id: youtube video id

- Show thumbnails: show thumbnails as icon
  - default: `true`
  - info: search may be slower with thumbnails

## Usage

To search on youtube, use the keyword (default is `yt`), then type/paste and wait for the extension to load.

You will see the 10 top searches. Just click/press ENTER on one to see it on your default browser.

## License

[MIT License](LICENSE)
