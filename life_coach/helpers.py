from datetime import datetime
from pathlib import Path
from typing import Any, Dict
import pytz
import os


def format_response(content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "response": content.strip(),
        "metadata": metadata,
        "timestamp": datetime.now().isoformat()
    }


def format_error_message(error: Exception, context: str = "") -> str:
    return (
        f"⚠️ An error occurred while {context}:\n\n"
        f"{type(error).__name__}: {str(error)}"
    )


def get_timezone_offset() -> str:
    try:
        tz = datetime.now().astimezone().tzinfo
        offset = tz.utcoffset(datetime.now())
        return str(int(offset.total_seconds() / 3600))
    except Exception:
        return "0"


def save_markdown_log(title: str, content: str, metadata: Dict[str, Any]) -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{title.replace(' ', '_').lower()}_{timestamp}.md"
    filepath = log_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Timestamp:** {timestamp}\n\n")
        for key, value in metadata.items():
            f.write(f"**{key}:** {value}\n\n")
