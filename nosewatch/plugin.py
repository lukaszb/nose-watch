import sys
from nose.plugins import Plugin
from subprocess import Popen


class WatchPlugin(Plugin):
    """
    Plugin that use watchdog for continuous tests run.
    """
    name = 'watch'
    is_watching = False
    argv = []
    stdout = None

    def __init__(self, *args, **kwargs):
        self.argv = sys.argv
        self.stdout = sys.stdout
        super(WatchPlugin, self).__init__(*args, **kwargs)

    def call(self, args):
        Popen(args).wait()

    def finalize(self, result):
        argv = list(self.argv)
        try:
            argv.remove('--with-watch')
        except ValueError:
            pass
        watchcmd = 'clear && ' + ' '.join(argv)
        call_args = ['watchmedo', 'shell-command', '-c',
            watchcmd, '-R', '-p', '*.py', '-W', '.']
        try:
            self.call(call_args)
        except KeyboardInterrupt:
            self.stdout.write('\nStopped\n')
