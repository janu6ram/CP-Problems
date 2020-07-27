// # Write the function hasBalancedParentheses, which takes a string and returns True
// # if that code has balanced parentheses and False otherwise (ignoring all
// # 	non-parentheses in the string). We say that parentheses are balanced if each
// # right parenthesis closes (matches) an open (unmatched) left parenthesis,
// # and no left parentheses are left unclosed (unmatched) at the end of the text.
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) ("
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as
// # you iterate over the string.

import java.util.*;
class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s){
		String[] arr = s.split("");
		Stack<String> stack = new Stack<String>();
		System.out.println(Arrays.toString(arr));
		for(int i = 0; i < arr.length; i++){
			if (arr[i].equals("(")){
				stack.push(arr[i]);
			}else if (arr[i].equals(")") && (i == 0 || !stack.pop().equals("("))){
				return false;
			}
		}
		if (stack.empty()) {
			return true;
		}
		return false;
	}
}
