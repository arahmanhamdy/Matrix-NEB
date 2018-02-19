from neb.plugins import Plugin
import base64


class Base64Plugin(Plugin):
    """Encode or decode base64.
    b64 encode <text> : Encode <text> as base64.
    b64 decode <b64> : Decode <b64> and return text.
    """

    name = "b64"

    @staticmethod
    def cmd_encode(event):
        """Encode as base64. 'b64 encode <text>'"""
        # use the body directly so quotes are parsed correctly.
        return base64.b64encode(event["content"]["body"][12:])

    @staticmethod
    def cmd_decode(event):
        """Decode from base64. 'b64 decode <base64>'"""
        # use the body directly so quotes are parsed correctly.
        return base64.b64decode(event["content"]["body"][12:])
