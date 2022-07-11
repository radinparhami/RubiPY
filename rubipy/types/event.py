class Event():
    def __init__(self, update):
        self.type = update.type
        self.pinned_message_id = update.pinned_message_id
        self.performer_type = update.performer_object.type
        self.performer_user_quid = update.performer_object.object_guid
        self.peer_type = update.peer_objects and update.peer_objects.type
        self.peer_user_guid = update.peer_objects and update.peer_objects.object_guid

        self.LeaveGroup = self.type == 'LeaveGroup'
        self.AddedGroupMembers = self.type == 'AddedGroupMembers'
        self.JoinedGroupByLink = self.type == 'JoinedGroupByLink'
        self.RemoveGroupMembers = self.type == 'RemoveGroupMembers'
        self.PinnedMessageUpdated = self.type == 'PinnedMessageUpdated'

        self.Left_Member = self.RemoveGroupMembers or self.LeaveGroup
        self.New_Member = self.AddedGroupMembers or self.JoinedGroupByLink
