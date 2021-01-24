"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

We will be designing a system with the following requirements:

Any non-member (guest) can search and view questions. However, to add or upvote a question, they have to become a member.
Members should be able to post new questions.
Members should be able to add an answer to an open question.
Members can add comments to any question or answer.
A member can upvote a question, answer or comment.
Members can flag a question, answer or comment, for serious problems or moderator attention.
Any member can add a bounty to their question to draw attention.
Members will earn badges for being helpful.
Members can vote to close a question; Moderators can close or reopen any question.
Members can add tags to their questions. A tag is a word or phrase that describes the topic of the question.
Members can vote to delete extremely off-topic or very low-quality questions.
Moderators can close a question or undelete an already deleted question.
The system should also be able to identify most frequently used tags in the questions.

We have five main actors in our system:

Admin: Mainly responsible for blocking or unblocking members.
Guest: All guests can search and view questions.
Member: Members can perform all activities that guests can, in addition to which they can add/remove questions, answers, and comments. Members can delete and un-delete their questions, answers or comments.
Moderator: In addition to all the activities that members can perform, moderators can close/delete/undelete any question.
System: Mainly responsible for sending notifications and assigning badges to members.
Here are the top use cases for Stack Overflow:

Top User Cases:

Search questions.
Create a new question with bounty and tags.
Add/modify answers to questions.
Add comments to questions or answers.
Moderators can close, delete, and un-delete any question.

"""


