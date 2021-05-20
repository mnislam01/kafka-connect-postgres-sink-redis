import redis


class ConnectionService:
    def __init__(self):
        self.client = None
        """
                     host='localhost', port=6379,
                         db=0, password=None, socket_timeout=None
                    """
        self.conn_pool = redis.ConnectionPool(
            host='redis', port=6379, db=0,
            password=None, socket_timeout=None
        )

    def get_client(self):
        if self.client is None:
            self.client = redis.Redis(connection_pool=self.conn_pool)
        return self.client
