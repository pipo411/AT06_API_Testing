class SmsStore:
    message_storage = {}
    id = 0

    def __init__(self):
        SmsStore.message_storage = {}

    # Makes new SMS tuple, inserts it after other messages
    # in the store. When creating this message, its
    #  has_been_viewed status is set False.
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        SmsStore.id += 1
        self.has_been_viewed = False
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS
        self.listMessages = [self.has_been_viewed, self.from_number, self.time_arrived, self.text_of_SMS]
        SmsStore.message_storage.update({SmsStore.id: self.listMessages})

        return SmsStore.message_storage  # Returns the number of sms messages in my_inbox

    # Returns the number of sms messages in my_inbox
    def message_count(self):
        return len(SmsStore.message_storage)

    # Returns list of indexes of all not-yet-viewed SMS messages
    def get_unread_indexe(self):
        unread_messages_list = []
        for i in range(1, len(SmsStore.message_storage) + 1):
            if (SmsStore.message_storage[i])[0] == False:
                unread_messages_list.append(SmsStore.message_storage[i])
        return unread_messages_list

    # Return (from_number, time_arrived, text_of_sms) for message[i]
    # Also change its state to "has been viewed".
    # If there is no message at position i, return None
    def get_message(self):
        print(SmsStore.message_storage)
        key = int(input("Insert the ID that the message that you want to review: "))
        if SmsStore.message_storage.get(key) != None:
            SmsStore.message_storage.get(key)[0] = True
        else:
            return None
        return SmsStore.message_storage.get(key)

    # Delete the message at index i my_inbox.clear()
    def delete(self):
        print(SmsStore.message_storage)
        key = int(input("Insert the ID in order to delete it: "))
        del SmsStore.message_storage[key]
        return SmsStore.message_storage

    #  Delete all messages from inbox
    def clear(self):
        return SmsStore.message_storage.clear()


my_inbox = SmsStore()
my_inbox2 = SmsStore()
my_inbox3 = SmsStore()
my_inbox.add_new_arrival(70392587, "15:05", "Hello")
my_inbox2.add_new_arrival(7294198, "15:39", "Good Morning")
my_inbox3.add_new_arrival(70392928, "18:05", "Peperoni")

print(my_inbox.get_message())
print(my_inbox.delete())
print(my_inbox.clear())
