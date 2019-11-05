from django.utils.version import get_version

VERSION = (3, 1, 0, 'alpha', 0)

__version__ = get_version(VERSION)                                                            # --- 原来version--- 是写在这里的
                                                                                              # --- __all__ = [] 这个也写在这里

def setup(set_prefix=True):                                                                   # 建造者模式将所有写的类进行输出，在java
    """
    Configure the settings (this happens as a side effect of accessing the                    # 可能是个接口之类的
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    from django.apps import apps
    from django.conf import settings
    from django.urls import set_script_prefix
    from django.utils.log import configure_logging

    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
    if set_prefix:
        set_script_prefix(
            '/' if settings.FORCE_SCRIPT_NAME is None else settings.FORCE_SCRIPT_NAME
        )
    apps.populate(settings.INSTALLED_APPS)
