class Solution {
    public int maxProfit(int[] prices) {

        int l = 0;
        int r = 0;
        int maxNum = 0;
        
        while(r < prices.length - 1){

            r++;

            if(prices[l] >= prices[r]){
                l = r;
            }
            else{
                maxNum = Math.max(maxNum,prices[r] - prices[l]);
            }



        }

        return maxNum;
        
    }
}
