from thorn.request import Request as BaseRequest
from thorn.app import Thorn


class Request(BaseRequest):
    def dispatch(self, session=None, propagate=False):
        # type: (requests.Session, bool) -> 'Request'
        super().dispatch(session, propagate)
        self.response.raise_for_status()
        return self


class App(Thorn):
    request_cls = 'simpl.games.thorn:Request'


thorn_app = App(set_as_current=True)
