import java.util.HashMap;
import java.util.Stack;

public class NextGreatElementI {
    public int[] Solution(int[] nums1, int[] nums2) {
        Stack<Integer> stack = new Stack<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        // result 长度等于查询数组nums1
        int[] result = new int[nums1.length];
        // 遍历对比数组nums2
        for (int i = 0; i < nums2.length; i++) {
            while (!stack.empty() && nums2[i] > stack.peek()) {
                map.put(stack.pop(), nums2[i]);
            }
            stack.push(nums2[i]);
        }
        while (!stack.empty()) {
            map.put(stack.pop(), -1);
        }
        for (int i = 0; i < nums1.length; i++) {
            result[i] = map.get(nums1[i]);
        }
        return result;
    }
}

/**
 * 利用单调栈找出对 nums2 中所有元素的 next great number，并生成map
 * 最后查找 nums1 对应元素在 map 中的值
 */
