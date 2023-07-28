from typing import Optional, Dict
from src.client import HabiticaBaseClient

class HabiticaWebhookClient(HabiticaBaseClient):
    def create_webhook(self, url: str, id: Optional[str] = None, label: Optional[str] = None,
                       enabled: Optional[bool] = None, type: Optional[str] = None, 
                       options: Optional[dict] = None) -> Dict:
        
        data = {"url": url}
        
        if id is not None:
            data["id"] = id
            
        if label is not None:
            data["label"] = label
            
        if enabled is not None:
            data["enabled"] = enabled
            
        if type is not None:
            data["type"] = type
            
        if options is not None:
            data["options"] = options
        
        return self.make_request('POST', '/user/webhook', data=data)

    def get_webhooks(self) -> Dict:
        return self.make_request('GET', '/user/webhook')

    def edit_webhook(self, id: str, url: Optional[str] = None, label: Optional[str] = None,
                     enabled: Optional[bool] = None, type: Optional[str] = None, 
                     options: Optional[dict] = None) -> Dict:
        
        data = {}
        
        if url is not None:
            data["url"] = url
            
        if label is not None:
            data["label"] = label
            
        if enabled is not None:
            data["enabled"] = enabled
            
        if type is not None:
            data["type"] = type
            
        if options is not None:
            data["options"] = options
        
        return self.make_request('PUT', f'/user/webhook/{id}', data=data)

    def delete_webhook(self, id: str) -> Dict:
        return self.make_request('DELETE', f'/user/webhook/{id}')