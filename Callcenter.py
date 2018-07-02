class Callcenter(object):
    def __init__(self, name, unique_id, caller_name, caller_phone, time_call, reason_call):
        self.name = name
        self.unique_id
        self.caller_name
        self.caller_phone
        self.time_call
        self.reason_call
    def unique_id(self):
        print "ID"
        return self
    def caller_name(self):
        print "caller name"
        return self
    def caller_phone(self):
        print "phone number"
        return self
    def time_call(self):
        print "time of call is:"
        return self
    def reason_call(self):
        print "reason of call is:"
        return self
    def display_all(self):
        return self
callcenter1 = Callcenter("call")
callcenter1.unique_id().caller_name().caller_phone().time_call().reason_call().display_all()