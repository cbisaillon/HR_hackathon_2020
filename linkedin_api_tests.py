from linkedin_v2.linkedin import LinkedInAuthentication, LinkedInApplication, PERMISSIONS
import os
from flask import Flask, request
from webbrowser import open_new_tab
from dotenv import load_dotenv
from xml.dom import minidom

load_dotenv()

PORT = 8000
app = Flask(__name__)

permissions = ["r_emailaddress", "r_liteprofile"]
authentication = LinkedInAuthentication(os.getenv("LINKEDIN_CLIENT_ID"),
                                        os.getenv("LINKEDIN_SECRET"),
                                        os.getenv("RETURN_URL"),
                                        permissions)


@app.route("/code")
def login():
    code = request.args.get('code')
    authentication.authorization_code = code

    application = LinkedInApplication(token=authentication.get_access_token())

    return str(application.make_request("GET", "https://api.linkedin.com/v1/companies").json())


def ask_permission():
    open_new_tab(authentication.authorization_url)


def main():
    # Ask user to login on linkedin
    ask_permission()
    app.run(port=PORT)


if __name__ == "__main__":
    main()
