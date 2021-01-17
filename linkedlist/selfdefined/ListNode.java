/**
 * ListNode
 */
public class ListNode {
    int val;
    ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    // 打印该节点及其之后的链表
    @Override
    public String toString() {
        ListNode tmp = this;  //当前节点
        StringBuffer sb = new StringBuffer();
        while (tmp != null) {
            sb.append(tmp.val);
            if (tmp.next != null) {
                sb.append("->");
            }
            tmp = tmp.next;
        }
        return sb.toString();
    }
}