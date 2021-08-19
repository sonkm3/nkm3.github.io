import re
import urllib

from markdown import Extension
from markdown.postprocessors import Postprocessor


class EmbedGithubExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('embed-github', EmbedGithubPostprocesser(self), '>raw_html')


class EmbedGithubPostprocesser(Postprocessor):
    _pattern = re.compile(r"\[(http(s)?(://github\.com\/[\w:;/.?%#&=+-]+)):embed\-github\]")

    def run(self, html):
        return re.sub(self._pattern, self._replace_embed, html) 

    def _replace_embed(self, match):
        # https://github.com/yusanshi/embed-like-gist
        return """<script src="/javascripts/embed.js?target={0}&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on"></script>"""\
            .format(urllib.parse.quote(match.group(1), safe=''),)


def makeExtension(*args, **kwargs):
    return EmbedGithubExtension(*args, **kwargs)
