/*

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
*/

func isIsomorphic(s string, t string) bool {

  
	mapS := make(map[byte]byte)
	mapT := make(map[byte]byte)
	
	for i := range s {
  
	  
	  if _, okS := mapS[s[i]]; okS {
		if mapS[s[i]] != t[i] {
		  return false
		}
	  } else if _, okT := mapT[t[i]]; okT {
		if mapT[t[i]] != s[i] {
		  return false
		}
	  }
	  
	  mapS[s[i]] = t[i]
	  mapT[t[i]] = s[i]
	}
	
	return true
  }

// Runtime 7 ms Beats 18.74% of users with Go
// Memory 2.82 MB Beats 37.05% of users with Go
