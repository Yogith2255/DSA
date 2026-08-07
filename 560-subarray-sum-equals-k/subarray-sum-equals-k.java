class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Long, Integer> map = new HashMap<>();
        long sum = 0;
        int ans = 0;
        for(int ele : nums) {
            sum += ele;
            if(sum == k) ans++;
            if(map.containsKey(sum - k)) {
                ans += map.get(sum - k);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return ans;
    }
}