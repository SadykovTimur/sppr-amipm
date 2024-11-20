import json
from typing import Any, Dict, List, Optional


def filter_logs(
    logs: List[Dict[str, Any]], method_name: Optional[str] = None, url: Optional[str] = None
) -> List[Dict[str, Any]]:
    logs = [json.loads(log['message']) for log in logs]

    if method_name:
        logs = [log for log in logs if method_name == log['message']['method']]

    if url:
        logs = [log for log in logs if url in log['message']['params']['headers'][':path']]

    return logs
