from libraries import os, shutil, log, sys

log.basicConfig(level=log.INFO,
                filename=r"C:/uninstall_log.log",
                filemode='a',
                )
uninstall_path: str = r"C:/"

class Uninstall:

    def __init__(self) -> None:
        self.folder_path: str = os.path.dirname(os.path.abspath(__file__))
        self.WTS_del_command: str = 'schtasks /delete /tn "Are-you-asleep"'

    def log_info(self, message: str) -> None:
        log.info(30 * "_")
        log.info(message)

    def drop_content(self) -> None:
        """Removes all content from folder"""
        try:
            shutil.rmtree(self.folder_path)
        except Exception as e:
            self.log_info(f"Error found during content deletion: {e}")
            sys.exit(1)
        self.log_info("Content deletion successful")

    def drop_task(self) -> None:
        """Deletes early created task to run periodically"""
        try:
            os.system(f"{self.WTS_del_command}")
        except Exception as e:
            self.log_info(f"Error found during task deletion: {e}")
            sys.exit(1)
        self.log_info("Task Deletion successful")

def main() -> None:
    unist = Uninstall()
    unist.drop_task()
    unist.drop_content()

if __name__ == "__main__":
    main() 