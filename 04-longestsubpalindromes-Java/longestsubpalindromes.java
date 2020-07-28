// # Write the function longestSubpalindrome(s), that takes a string s and returns
// the longest palindrome that occurs as consecutive characters (not just letters, but
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!")
// # returns "b-4-b". If there is a tie, return the lexicographically larger value --
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce")
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions,
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also,
// from the explanation above, we see that longestSubpalindrome("aba") is "aba",
// and longestSubpalindrome("a") is "a".

class longestsubpalindromes {
	public String fun_longestsubpalindromes(String s){
		int max = 1;
		String longPall = s.substring(0,1);
		for(int i = 0; i < s.length(); i++){
			for(int j = i+1; j < s.length();j++){
				if (s.charAt(i) == s.charAt(j) && checkPallindrome(s.substring(i,j+1))){
					int len = j + 1 - i;
					String newPall = s.substring(i,j+1);
					if (len >= max){
						max = len;
						longPall = newPall;
						System.out.println(len+ " "+longPall);
					}
				}
			}
		}
		return longPall;
	}
	public boolean checkPallindrome(String str){
		int len = str.length();
		for(int i = 0; i < len/2;i++){
			if (str.charAt(i) != str.charAt(len-1-i)){
				return false;
			}
		}
		return true;
	}
}
