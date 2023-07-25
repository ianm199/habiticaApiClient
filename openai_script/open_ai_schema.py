import json
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class Message:
    role: Optional[str] = None
    content: Optional[str] = None

@dataclass
class Choice:
    index: Optional[int] = None
    message: Optional[Message] = None
    finish_reason: Optional[str] = None

@dataclass
class Output:
    id: Optional[str] = None
    object: Optional[str] = None
    created: Optional[int] = None
    model: Optional[str] = None
    choices: Optional[List[Choice]] = None
    usage: Optional[Dict[str, int]] = None

    @classmethod
    def init_from_json(cls, json_dict: dict):
        result = cls(**json_dict)
        result.choices = [Choice(**choice) for choice in result.choices]
        for choice in result.choices:
            choice.message = Message(**choice.message)
        return result

