#   Copyright 2010-2011 Josh Kearney
#   Copyright 2012 Aaron Lee
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Pyhole TinyUrl Plugin"""

import urllib

from pyhole.core import plugin
from pyhole.core import utils


class TinyURL(plugin.Plugin):
    """Provides a short url when a long one is posted"""

    def __init__(self, *args, **kwargs):
        plugin.Plugin.__init__(self, *args, **kwargs)
        self.config = utils.get_config("TinyURL")

    def _shorten(self, message, url):
        if len(url) > self.config.get("length", type="int", default=50):
            tiny_api = ("http://tinyurl.com/api-create.php?url=" +
                        urllib.quote_plus(url))
            message.dispatch(urllib.urlopen(tiny_api).read())

    @plugin.hook_add_keyword("http://")
    def http(self, message, params=None, **kwargs):
        self._shorten(message, "http://" + params)

    @plugin.hook_add_keyword("https://")
    def https(self, message, params=None, **kwargs):
        self._shorten(message, "https://" + params)
