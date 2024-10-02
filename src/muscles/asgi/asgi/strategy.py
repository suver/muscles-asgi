from typing import Optional

from muscles.core import BaseStrategy
from watchdog.events import LoggingEventHandler
from .server import AsgiTransport, AsgiServer
from .error_handler import ResponseErrorHandler

event_handler = LoggingEventHandler()


class AsgiStrategy(BaseStrategy):
    """
    Стратегия ASGI сервера
    """

    def execute(self, *args, error_handler: Optional[ResponseErrorHandler] = None, **kwargs):
        """
        Запускаем обработку запросов
        :param args:
        :param error_handler:
        :param kwargs:
        :return:
        """
        host = kwargs['host'] if hasattr(kwargs, 'host') else 'localhost'
        port = kwargs['port'] if hasattr(kwargs, 'port') else 8080

        server = AsgiServer(host, port, error_handler=error_handler)
        transport = kwargs.get('transport', AsgiTransport)
        server.init_transport(transport)
        return server.execute(*args, **kwargs)
