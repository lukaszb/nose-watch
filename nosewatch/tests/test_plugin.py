import unittest
from mock import Mock
from nosewatch.plugin import WatchPlugin


class TestWatchPlugin(unittest.TestCase):

    def test_finalize(self):
        plugin = WatchPlugin()
        plugin.sys = Mock()
        plugin.sys.argv = ['program', 'arg1', '--with-watch', 'arg3', 'arg4']
        plugin.call = Mock()
        plugin.finalize(Mock())

        watchcmd = 'clear && program arg1 arg3 arg4'
        plugin.call.assert_called_once_with([
            'watchmedo', 'shell-command', '-c', watchcmd,
            '-R', '-p', '*.py', '.'])

