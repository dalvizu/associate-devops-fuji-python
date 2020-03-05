from fuji import App

app = App()

ticket = """
commit 55c0bb88b6e4f096574991dd9217bcf8c745d05e
Author: Example User <example@pingidentity.com>
Date:   Mon May 4 17:09:19 2015 -0600

    SSD-101 super duper feature
    Fix tomcat issue with using forks over spoons.
"""


# I should print ['SSD-101']
print(app.get_jira_tickets([ticket]))
