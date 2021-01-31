"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/


System requirements while designing LinkedIn:

Each member should be able to add information about their basic profile, experiences, education, skills, and accomplishments.

Any user of our system should be able to search for other members or companies by their name.

Members should be able to send or accept connection requests from other members.

Any member will be able to request a recommendation from other members.

The system should be able to show basic stats about a profile, like the number of profile views, the total number of connections, and the total number of search appearances of the profile.

Members should be able to create new posts to share with their connections.

Members should be able to add comments to posts, as well as like or share a post or comment.

Any member should be able to send messages to other members.

The system should send a notification to a member whenever there is a new message, connection invitation or a comment on their post.

Members will be able to create a page for a Company and add job postings.

Members should be able to create groups and join any group they like.

Members should be able to follow other members or companies.

====================================

We have three main Actors in our system:

Member: All members can search for other members, companies or jobs, as well as send requests for connection, create posts, etc.
Admin: Mainly responsible for admin functions such as blocking and unblocking a member, etc.
System: Mainly responsible for sending notifications for new messages, connections invites, etc.

====================================

Here are the top use cases of our system:

Add/update profile: Any member should be able to create their profile to reflect their experiences, education, skills, and accomplishments.
Search: Members can search other members, companies or jobs. Members can send a connection request to other members.
Follow or Unfollow member or company: Any member can follow or unfollow any other member or a company.
Send message: Any member can send a message to any of their connections.
Create post: Any member can create a post to share with their connections, as well as like other posts or add comments to any post.
Send notifications: The system will be able to send notifications for new messages, connection invites, etc.


"""
from enum import Enum
class ConnectionInvitationStatus(Enum):
    PENDING, ACCEPTED, CONFIRMED, REJECTED, CANCELED = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
    def __init__(self, id, password, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self):
        None


class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Member(Person):
    def __init__(self):
        self.__date_of_membership = datetime.date.today()
        self.__headline = ""
        self.__photo = []
        self.__member_suggestions = []
        self.__member_follows = []
        self.__member_connections = []
        self.__company_follows = []
        self.__group_follows = []
        self.__profile = Profile()

    def send_message(self, message):
        None

    def create_post(self, post):
        None

    def send_connection_invitation(self, connection_invitation):
        None


class Admin(Person):
    def block_user(self, customer):
        None

    def unblock_user(self, customer):
        None

class Profile:
    def __init__(self, summary, experiences, educations, skills, accomplishments, recommendations):
        self.__summary = summary
        self.__experiences = experiences
        self.__educations = educations
        self.__skills = skills
        self.__accomplishments = accomplishments
        self.__recommendations = recommendations
        self.__stats = []

    def add_experience(self, experience):
        None

    def add_education(self, education):
        None

    def add_skill(self, skill):
        None

    def add_accomplishment(self, accomplishment):
        None

    def add_recommendation(self, recommendation):
        None


class Experience:
    def __init__(self, title, company, location, date_from, date_to, description):
        self.__title = title
        self.__company = company
        self.__location = location
        self.__from = date_from
        self.__to = date_to
        self.__description = description

class Company:
    def __init__(self, name, description, type, company_size):
        self.__name = name
        self.__description = description
        self.__type = type
        self.__company_size = company_size

        self.__active_job_postings = []

import datetime
class JobPosting:
    def __init__(self, description, employment_type, location, is_fulfilled):
        self.__date_of_posting = datetime.date.today()
        self.__description = description
        self.__employment_type = employment_type
        self.__location = location
        self.__is_fulfilled = is_fulfilled

class Group:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__total_members = 0
        self.__members = []

    def add_member(self, member):
        None

    def update_description(self, description):
        None


class Post:
    def __init__(self, text, owner):
        self.__text = text
        self.__total_likes = 0
        self.__total_shares = 0
        self.__owner = owner


class Message:
    def __init__(self, sent_to, message_body, media):
        self.__sent_to = sent_to
        self.__message_body = message_body
        self.__media = media


from abc import ABC, abstractmethod

class Search:
    def search_member(self, name):
        None

    def search_company(self, name):
        None

    def search_job(self, title):
        None


class SearchIndex(Search):
    def __init__(self):
        self.__member_names = {}
        self.__company_names = {}
        self.__job_titles = {}

    def add_member(self, member):
        if member.get_name() in self.__member_names:
            self.__member_names.get(member.get_name()).add(member)
        else:
            self.__member_names[member.get_name()] = member

    def add_company(self, company):
        None

    def add_job_posting(self, job_posting):
        None

    def search_member(self, name):
        return self.__member_names.get(name)

    def search_company(self, name):
        return self.__company_names.get(name)

    def search_job(self, title):
        return self.__job_titles.get(title)