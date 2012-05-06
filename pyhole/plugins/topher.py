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

"""Pyhole Topher Plugin"""

from pyhole import plugin
from pyhole import utils


class Topher(plugin.Plugin):
    """I'm a beliber"""

    def __init__(self, irc):
        self.irc = irc
        self.name = self.__class__.__name__
        self.config = utils.get_config("Topher")

    def say_hi(self, source, target):
        greeting = self.config.get("greeting")
        if not greeting:
            return

        if source == self.irc.nick:
            self.irc.connection.privmsg(target, greeting)

    @plugin.hook_add_action("join")
    def join(self, params=None, **kwargs):
        target = kwargs.get("target")
        source = params
        if not source or not target:
            return
        self.say_hi(source, target)

    @plugin.hook_add_command("hi")
    def hi(self, params=None, **kwargs):
        greeting = self.config.get("greeting")
        if not greeting:
            return

        self.irc.reply(greeting)
