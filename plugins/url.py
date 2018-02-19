from neb.plugins import Plugin

import urllib.parse


class UrlPlugin(Plugin):
    """URL encode or decode text.
    url encode <text>
    url decode <text>
    """

    name = "url"

    @staticmethod
    def cmd_encode(event, url):
        """URL encode text. 'url encode <text>'"""
        # use the body directly so quotes are parsed correctly.
        return urllib.parse.quote(url)

    @staticmethod
    def cmd_decode(event, url):
        """URL decode text. 'url decode <url encoded text>'"""
        # use the body directly so quotes are parsed correctly.
        return urllib.parse.unquote(url)
