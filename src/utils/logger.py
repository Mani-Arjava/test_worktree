from datetime import datetime


class Logger:
    def log(self, message: str) -> None:
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] {message}")
