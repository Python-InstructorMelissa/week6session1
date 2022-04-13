self.friend = None
self.me = None



allFriendships = []
for row in results:
    frienship = cls(row)
    # looking at janes 1st friendship
    userData = {
        'id': row['user.id'],
        'firstName': row['user.firstName'],
        'lastName': row['user.lastName'],
    }
    frienship.me = User(userData)
    friendData = {
        'id': row['friend.id'],
        'firstName': row['friend.firstName'],
        'lastName': row['friend.lastName'],
    }
    frienship.friend = User(friendData)
    allFriendships.append(frienship)
