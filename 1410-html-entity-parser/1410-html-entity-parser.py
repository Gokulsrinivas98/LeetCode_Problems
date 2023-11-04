class Solution:
    def entityParser(self, text: str) -> str:
        return text.replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<').replace('&apos;', "'").replace('&amp;', '&').replace('&frasl;', '/')