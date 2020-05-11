from lib import Login, Controllers
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    con = Controllers.WorkspaceController()
    con.refresh_dataset("Sales", "Sales")
