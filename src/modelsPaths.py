from src.client import HabiticaBaseClient

class HabiticaUserClient(HabiticaBaseClient):
    def get_model_paths(self, model: str):
        return self.make_request('GET', f'/models/{model}/paths')

class HabiticaTagClient(HabiticaBaseClient):
    def get_model_paths(self, model: str):
        return self.make_request('GET', f'/models/{model}/paths')

class HabiticaChallengeClient(HabiticaBaseClient):
    def get_model_paths(self, model: str):
        return self.make_request('GET', f'/models/{model}/paths')

class HabiticaGroupClient(HabiticaBaseClient):
    def get_model_paths(self, model: str):
        return self.make_request('GET', f'/models/{model}/paths')

class HabiticaHabitClient(HabiticaBaseClient):
    def get_model_paths(self, model: str):
        return self.make_request('GET', f'/models/{model}/paths')

class HabiticaDailyClient(HabiticaBaseClient):
    def get_model_paths(self, model: str):
        return self.make_request('GET', f'/models/{model}/paths')

class HabiticaTodoClient(HabiticaBaseClient):
    def get_model_paths(self, model: str):
        return self.make_request('GET', f'/models/{model}/paths')

class HabiticaRewardClient(HabiticaBaseClient):
    def get_model_paths(self, model: str):
        return self.make_request('GET', f'/models/{model}/paths')