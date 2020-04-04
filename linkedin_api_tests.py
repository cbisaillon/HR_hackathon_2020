from linkedin import server
import os
from dotenv import load_dotenv
load_dotenv()


def main():
    application = server.quick_api(os.getenv("LINKEDIN_CLIENT_ID"),
                                   os.getenv("LINKEDIN_SECRET"))


if __name__ == "__main__":
    main()
