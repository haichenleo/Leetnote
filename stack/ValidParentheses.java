import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 == 1) {
            return false;
        }
        
        // Deque 可以用作 stack
        // push - addFirst
        // pop - removeFirst
        // peek - getFirst
        Deque<Character> stack = new LinkedList<>();
        // 声明 - 实例化 hashmap
        HashMap<Character, Character> map = new HashMap<>();
        // put - 放入k,v
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for (int i=0; i<s.length(); i++) {
            // charAt - 根据下标获取char
            char c = s.charAt(i);
            // containsKey - 判断key是否在map中
            if (map.containsKey(c)) {
                if (stack.isEmpty() || map.get(c) != stack.peek()) {
                    return false;
                }
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}

class Solution2 {
    public boolean isValid(String s) {
        if (s.isEmpty())
            return false;
        // Stack类 - 给予数组实现栈
        Stack<Character> stack = new Stack<>();
        // toCharArray - string 转化为 array
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.empty() || c != stack.pop())
                return false;
        }
        if (stack.empty())
            return true;
        return false;
        
    }
}

/**
 * ValidParentheses
 */
public class ValidParentheses {

    public static void main(String[] args) {
        Solution2 s = new Solution2();
        boolean result = s.isValid("[]");
        System.out.println(result);
    }
}