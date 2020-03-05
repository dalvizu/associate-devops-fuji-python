
class App:

    """
    Your assignment is to write a method which returns a list of JIRA
    tickets (as String). This will be used as a library in a bigger flow:
    one program will provide the list of GitCommits, and another
    will consume the list of Strings provided to do stuff on JIRA.

    Implement me!!!
    """
    def get_jira_tickets(self, git_commits):
        """

        Return a list of JIRA tickets present in the provided gitCommits

        :param git_commits: a List of strings containing a git Commit message
        :return: a List of Strings representing JIRA tickets
        """
        assert(type(git_commits) is list)
        return ["SSD-101", "SSD-102" ]
