int maxProfit(int* prices, int pricesSize) {
    int profit = 0;
    for(int i = 0; i<pricesSize; i++){
        for(int j = i+1; j<pricesSize; j++){
            if(prices[j] - prices[i]> 0 && prices[j] - prices[i] > profit){
                profit = prices[j] - prices[i];
            }
        }
    }

    return profit;
}