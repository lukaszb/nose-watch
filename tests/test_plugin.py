"""
Main plugin tests.

.. note:: Please to not run nosetests with this plugin for testing the plugin
   itself. Also, mock.patch is not much help here as it would try to mock the
   module that would be already imported by nose itself if plugin was installed
   globally (it would take module from sys.modules).
"""
import unittest
from mock import Mock
from nosewatch.plugin import WatchPlugin


class TestWatchPlugin(unittest.TestCase):

    def setUp(self):
        self.plugin = WatchPlugin()
        self.plugin.stdout = Mock()
        self.plugin.argv = ['program', 'arg1', '--with-watch', 'arg3', 'arg4']

    def test_finalize(self):
        self.plugin.call = Mock()
        self.plugin.finalize(Mock())

        watchcmd = 'clear && program arg1 arg3 arg4'
        self.plugin.call.assert_called_once_with([
            'watchmedo', 'shell-command', '-c', watchcmd,
            '-R', '-p', '*.py', '-W', '.'])

    def test_finalize_interrupted(self):
        self.plugin.call = Mock(side_effect=KeyboardInterrupt)
        self.plugin.finalize(Mock())
        self.plugin.stdout.write.assert_called_once_with('\nStopped\n')

