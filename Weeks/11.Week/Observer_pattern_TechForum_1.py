class Publisher:
    def __init__(self):
        # make it uninhabitable
        pass

    def register(self):
        pass

    def unregister(self):
        pass

    def notifyAll(self):
        pass


class TechForum(Publisher):
    def __init__(self):
        self.__listOfUsers = []
        self.PostName = None

    def register(self, objectUser):
        if objectUser not in self.__listOfUsers:
            self.__listOfUsers.append(objectUser)

    def unregister(self, objectUser):
        self.__listOfUsers.remove(objectUser)

    def notifyAll(self):
        for objects in self.__listOfUsers:
            objects.notify(self.PostName)

    def WriteNewPost(self, postname):
        # user write a post
        self.PostName = postname
        # when submits the post is published and notification sent to all
        self.notifyAll()


class Subscriber:
    def __init__(self):
        pass

    def notify(self):
        pass


class User1(Subscriber):
    def notify(self, postname):
        print(f"User1 notified a new post: {postname}")


class User2(Subscriber):
    def notify(self, postname):
        print(f"User2 notified a new post: {postname}")


class SisterSites(Subscriber):
    def __init__(self):
        self.__sistersites = ["site 1", "site 2", "site 3"]  # the sites that connected with us

    def notify(self, postname):
        for site in self.__sistersites:
            # send updates
            print(f"sent notify to site --> {site}")


if __name__ == "__main__":
    techforum = TechForum()
    # create users
    user1 = User1()
    user2 = User2()
    sites = SisterSites()
    # resister opjectusers
    techforum.register(user1)
    techforum.register(user2)
    techforum.register(sites)

    # make post for all users
    techforum.WriteNewPost("Observe pattern in python")

    # remove or unregister the user
    techforum.unregister(user1)

    # make new post
    techforum.WriteNewPost("MVC Pattern in python")
