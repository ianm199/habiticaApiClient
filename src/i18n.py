from client import HabiticaBaseClient

class HabiticaI18nClient(HabiticaBaseClient):
    def get_i18n_browser_script(self) -> dict:
        return self.make_request('GET', '/i18n/browser-script')