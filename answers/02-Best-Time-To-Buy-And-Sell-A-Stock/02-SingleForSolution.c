int maxProfit(int* prices, int pricesSize) {
    int minSoFar = prices[0];
    int profit = 0;

    for (int i = 0; i < pricesSize; i++) {
        if(prices[i] < minSoFar){
            minSoFar = prices[i];
        }

        if(prices[i] - minSoFar > profit){
            profit = prices[i] - minSoFar;
        }
    }

    return profit;
}