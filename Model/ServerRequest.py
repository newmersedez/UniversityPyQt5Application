class ServerRequest:
    def __init__(self):
        self.RequestName = None
        self.Args = []
        self._socket = None

    def sendRequestToServer(self, data: str, host: str, port: int):
        pass

    def receiveResponseFromServer(self) -> str:
        pass
