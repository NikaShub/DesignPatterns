from social_network import Facebook
from spammer import SocialSpammer


def main():
    network = Facebook()
    spammer = SocialSpammer()

    friends_iterator = network.create_friends_iterator("user_123")
    spammer.send(friends_iterator, "Hey friend, check this out!")

    coworkers_iterator = network.create_coworkers_iterator("user_123")
    spammer.send(coworkers_iterator, "Work update meeting at 5 PM.")


if __name__ == "__main__":
    main()