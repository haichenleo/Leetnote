import java.util.Stack;

import selfdefined.CreateList;
import selfdefined.ListNode;

public class AddTwoNumbers2 {

    public ListNode addTwoNumbers2(ListNode l1, ListNode l2) {
        Stack<Integer> stack1 = new Stack<>();
        Stack<Integer> stack2 = new Stack<>();
        while (l1 != null){
            stack1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            stack2.push(l2.val);
            l2 = l2.next;
        }
        ListNode last = null;
        int carry = 0;
        while (!stack1.isEmpty() || !stack2.isEmpty() || carry > 0) {
            int sum = carry;
            sum += stack1.isEmpty() ? 0 : stack1.pop();
            sum += stack2.isEmpty() ? 0 : stack2.pop();
            ListNode newNode = new ListNode(sum % 10);
            carry = sum / 10;
            newNode.next = last;
            last = newNode;
        }
        return last;
    }

    // test
    public static void main(String[] args) {
        ListNode l1 = CreateList.create(new int[]{7,2,4,3});
        ListNode l2 = CreateList.create(new int[]{5,6,4});
        ListNode res = new AddTwoNumbers2().addTwoNumbers2(l1, l2);
        CreateList.print(res);
    }
}
