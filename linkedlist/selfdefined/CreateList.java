public class CreateList {
    
    public ListNode create(int[] nums) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        for (int num: nums){
            curr.next = new ListNode(num);
            curr = curr.next;
        }
        return dummy.next;
    }

    public void print(ListNode head) {
        while (head != null) {
            if (head.next != null) {
                System.out.print(head.val + "->");
            } else {
                System.out.print(head.val + "\n");
            }
        }
    }
}
