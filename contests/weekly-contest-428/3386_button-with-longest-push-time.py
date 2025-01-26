class Solution:
  def buttonWithLongestTime(self, events: list[list[int]]) -> int:
    max_button, max_time = events[0]

    for idx in range(1, len(events)):
      cur_button, cur_time = events[idx]
      delta_time = cur_time - events[idx - 1][1]

      if delta_time >= max_time:
        if delta_time == max_time and cur_button > max_button:
          continue
        max_button = cur_button
        max_time = delta_time

    return max_button