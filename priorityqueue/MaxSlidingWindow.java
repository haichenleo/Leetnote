class MaxSlidingWindow {
    // 方法1：暴力法 - 超出时间限制
    // 对每一个窗口计算最大值
    public int[] solution1(int[] nums, int k) {

        int n = nums.length;
        // 判空
        if (n * k == 0) {
            return new int[0];
        } else if (k > n) {
            int max = nums[0];
            for (int i : nums){
                max = Math.max(max, i);
            }
            return new int[]{max};
        }
        // 输出 - 大小为滑动窗口的次数+1
        int[] output = new int[n - k + 1];
        // 滑动窗口
        // l = i, r = i + k - 1 < n
        // i < n - k + 1
        for (int i = 0; i < n - k + 1; i++) {
            int max = nums[i];
            for (int j = i; j < i + k; j++) {
                max = Math.max(max, nums[j]);
            }
            output[i] = max;
        }
        return output;
    }
}
