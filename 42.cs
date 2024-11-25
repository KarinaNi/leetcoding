public class Solution {
    public int Trap(int[] height) {
        if (height == null || height.length == 0){
          return 0;
        }
        int n = height.length;
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];
        int trappedwater = 0;
        leftMax[0] = height[0];
        for(int i = 0; i < n; i++){
          leftMax[i] = Math.Max(leftMax[i-1], height[i])
        }

        rightmax[n-1] = height[n-1]
    }
}
