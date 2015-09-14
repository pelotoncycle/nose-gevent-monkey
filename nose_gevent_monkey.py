import logging

from nose.plugins.base import Plugin

logger = logging.getLogger(__name__)
# TODO: Add/configure handler for logger. Use default nose plugin handler.


class GeventMonkey(Plugin):
    """
    Plugin to monkey patch modules for use with gevent.
    """

    def options(self, parser, env):
        """
        Add options to command line.
        """
        super(GeventMonkey, self).options(parser, env)

        parser.add_option('--gevent-monkey-patch-all', action='store_true',
                          default=env.get('NOSE_GEVENT_MONKEY_PATCH_ALL'),
                          dest='gevent_monkey_patch_all',
                          help='Monkey patches the default modules patched by '
                               '`gevent.monkey.patch_all()`. Specific modules '
                               'can be overridden with the '
                               '`--gevent-monkey-patch` and '
                               '`--gevent-monkey-no-patch` options.  '
                               '[NOSE_GEVENT_MONKEY_PATCH_ALL]')
        parser.add_option('--gevent-monkey-patch', action='store',
                          default=env.get('NOSE_GEVENT_MONKEY_PATCH'),
                          dest='gevent_monkey_patch', metavar='MODULES',
                          help='Comma separated list of modules to patch.'
                               'Modules not supported by gevent.monkey are '
                               'ignored.  [NOSE_GEVENT_MONKEY_PATCH]')
        parser.add_option('--gevent-monkey-no-patch', action='store',
                          default=env.get('NOSE_GEVENT_MONKEY_NO_PATCH'),
                          dest='gevent_monkey_no_patch', metavar='MODULES',
                          help='Comma separated list of modules not to patch. '
                               'Modules not supported by gevent.monkey are '
                               'ignored.  [NOSE_GEVENT_MONKEY_NO_PATCH]')

    def configure(self, options, conf):
        """
        Configure plugin.
        """
        super(GeventMonkey, self).configure(options, conf)

        if not self.enabled:
            return

        try:
            import gevent.monkey
        except ImportError:
            logger.error(
                'Gevent monkey patching not available: '
                'Unable to import gevent.monkey module.'
            )
            self.enabled = False
            return

        try:
            from inspect import getargspec
            spec = getargspec(gevent.monkey.patch_all)
            patch_all_defaults = dict(zip(spec.args, spec.defaults))
        except:
            logger.exception(
                'Unable to get arguments for `gevent.monkey.patch_all()`.'
            )
            return

        if options.gevent_monkey_patch_all:
            modules = patch_all_defaults.copy()
        else:
            modules = {key: False for key in patch_all_defaults}

        if options.gevent_monkey_patch:
            for module in options.gevent_monkey_patch.split(','):
                if module in modules:
                    modules[module] = True

        if options.gevent_monkey_no_patch:
            for module in options.gevent_monkey_no_patch.split(','):
                if module in modules:
                    modules[module] = False

        if any(modules.itervalues()):
            logger.info(
                'Patching: {}'.format([k for k in modules if modules[k]])
            )
            gevent.monkey.patch_all(**modules)
        else:
            logger.info('No modules to patch.')
