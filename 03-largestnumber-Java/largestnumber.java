// # largestNumber: Write the function largestNumber(text) that takes a string of text and
// # returns the largest int value that occurs within that text, or 0 if no such value occurs.
// # You may assume that the only numbers in the text are non-negative integers and
// # that numbers are always composed of consecutive digits (without commas, for example). For example:
// #     	largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
// # returns 17 (the int value 17, not the string "17"). And
// #     	largestNumber("One person ate two hot dogs!")
// # returns None (the value None, not the string "None").

import java.util.*;
class largestnumber {
	public int fun_largestnumber(String s){
		int num = 0;
		Stack<Integer> stack = new Stack<Integer>();
		for(int i = 0; i < s.length();i++){
			char c = s.charAt(i);
			if(Character.isDigit(c)){
				num = num *10 + Integer.parseInt(c+"");
			}else{
				if (num != 0){
					stack.push(num);
				}
				num = 0;
			}
		}
		int max = 0;
		for(int x : stack){
			if (x > max){
				max = x;
			}
		}

		return max;


	}
}
