import re

class Solution:
  def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    function_times = [0] * n
    function_stack = list()

    for log in logs:
      id, did_start, timestamp = self._parseLog(log)

      if did_start:
        if len(function_stack):
          last_function = function_stack[-1]
          function_times[last_function[0]] += timestamp - last_function[1]
          last_function[1] = timestamp
        function_stack.append([id, timestamp])
      else:
        last_function = function_stack[-1]
        function_times[last_function[0]] += timestamp - last_function[1] + 1
        function_stack.pop()
        if len(function_stack):
          function_stack[-1][1] = timestamp + 1

    return function_times        

  def _parseLog(self, log):
    '''
    Parse given log. Returns ID, did_start, timestamp
    '''
    match = re.match(r"(?P<ID>\d+):(?P<did_start>start|end):(?P<timestamp>\d+)", log)
    if match == None:
      raise ValueError(f"Invalid log: {log}")
    return int(match.group("ID")), match.group("did_start") == "start",int(match.group("timestamp"))
  
class Solution:
  def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    function_times = [0] * n
    function_stack = list()
    prev_time = 0

    for log in logs:
      id, did_start, timestamp = log.split(":")
      id, did_start, timestamp = int(id), did_start == "start", int(timestamp)

      if did_start:
        if len(function_stack):
          function_times[function_stack[-1]] += timestamp - prev_time
        function_stack.append(id)
        prev_time = timestamp
      else:
        function_times[id] += timestamp - prev_time + 1
        function_stack.pop()
        prev_time = timestamp + 1

    return function_times        