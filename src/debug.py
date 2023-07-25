from typing import Dict
from client import HabiticaBaseClient

class HabiticaDevelopmentClient(HabiticaBaseClient):
    def add_ten_gems(self) -> Dict:
        return self.make_request('POST', '/debug/add-ten-gems')

    def add_hourglass(self) -> Dict:
        return self.make_request('POST', '/debug/add-hourglass')

    def set_cron(self) -> Dict:
        return self.make_request('POST', '/debug/set-cron')

    def make_admin(self) -> Dict:
        return self.make_request('POST', '/debug/make-admin')

    def modify_inventory(self, gear: Dict, special: Dict,
                         pets: Dict, mounts: Dict,
                         eggs: Dict, hatchingPotions: Dict,
                         food: Dict, quests: Dict) -> Dict:
        data = {
            "gear": gear,
            "special": special,
            "pets": pets,
            "mounts": mounts,
            "eggs": eggs,
            "hatchingPotions": hatchingPotions,
            "food": food,
            "quests": quests
        }
        return self.make_request('POST', '/debug/modify-inventory', data=data)

    def quest_progress(self) -> Dict:
        return self.make_request('POST', '/debug/quest-progress')