# <!-- Title: Calculate cache hits and misses

# Description:

# You have a system cache and request. Calculate number of cache hits and misses:

#     - The number of "hits" are digits in the request that are in the correct position as that of cache
#     - The number of "misses" are digits in the request that are in your cache but are located in the wrong position. 

# Given the cache and request, return number of hits and misses.

# Input: cache = "1807", request = "7810"
# Output: "1H3M"

# Explanation:
# "1807"
#   |
# "7810" -->

#constaints: same length
def calculate_hits_misses(cache, request):
    hits, misses = 0, 0
    cache_dict = {}
    req_dict = {}


    for c in cache:
        cache_dict[c] = 1+ cache_dict.get(c, 0)
    for r in request:
        req_dict[r] = 1+ req_dict.get(r, 0)
        

    for i in range(len(cache)):
        if cache[i] == request[i]:
            hits += 1
            cache_dict[cache[i]] -= 1
            req_dict[request[i]] -= 1
    
    for digit, count in req_dict.items():
        if digit in cache_dict:
            misses += min(count, cache_dict[digit])
          
    return f"{hits}H{misses}M"



cache = "1122"
request = "2211"
result = calculate_hits_misses(cache, request)
print(result)
    

# An optimization would be to use only 2 for loops 
# O(n) + O(n) TC



