# Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

# Every song is played at least once.
# A song can only be played again only if k other songs have been played.
# Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, goal = 3, k = 1
# Output: 6
# Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
# Example 2:

# Input: n = 2, goal = 3, k = 0
# Output: 6
# Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
# Example 3:

# Input: n = 2, goal = 3, k = 1
# Output: 2
# Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
 

# Constraints:

# 0 <= k < n <= goal <= 100

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}
        def count(cur_goal, old_songs):
            if cur_goal == 0 and old_songs == n:
                return 1
            if cur_goal == 0 or old_songs > n:
                return 0
            if (cur_goal, old_songs) in dp:
                return dp[(cur_goal, old_songs)]

            res = (n - old_songs)*(count(cur_goal - 1, old_songs + 1))
        
            if old_songs > k:
                res += (old_songs - k)* count(cur_goal - 1, old_songs)
            dp[(cur_goal, old_songs)] = res % mod

            return dp[(cur_goal, old_songs)]
        return count(goal, 0)
    

# Runtime 62 ms Beats 49.69%
# Memory 17.8 MB Beats 14.74%
#dummy