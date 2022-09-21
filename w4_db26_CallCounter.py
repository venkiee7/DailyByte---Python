# This question is asked by Google. Create a class CallCounter that tracks the number of calls a client has made within the last 3 seconds. Your class should contain one method, ping(int t) that receives the current timestamp (in milliseconds) of a new call being made and returns the number of calls made within the last 3 seconds.
# Note: you may assume that the time associated with each subsequent call to ping is strictly increasing.

class CallCounter:
  def __init__(self):
    self.pings = []
  
  def ping(self, t):
    self.pings.insert(0, t)
    print(self.pings)
    while self.pings[-1] + 3000 < t:
      self.pings.pop()
      print(self.pings)
    return len(self.pings)

cc = CallCounter()
print(cc.ping(1))
print(cc.ping(300)) 
print(cc.ping(3000))
print(cc.ping(3301))
print(cc.ping(8000))