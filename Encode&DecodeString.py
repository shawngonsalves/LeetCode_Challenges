'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.



Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}


Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""] Medium_Encode&DecodeStrings
'''

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        print(strs)
        for s in strs:
            res+= str(len(s)) + '#' + s
            
        return res
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            print(length)
            res.append(s[j+1: j+1+length])
            i= j+1+length
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


'''
Runtime: 72 ms, faster than 38.73% of Python3 online submissions for Encode and Decode Strings.
Memory Usage: 14.6 MB, less than 71.55% of Python3 online submissions for Encode and Decode Strings.
'''