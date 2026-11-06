package maximumSubArraySum;

public class SubarraySum {
	private int[] numbers;
	public SubarraySum(int[]numbers) // creates the SubarraySum class with the int array
	{
		this.numbers = numbers;
	}
	public int worseBruteForceGetMaxSub() // uses the int array to get maximum sub array in worst possible way
	{
		int largestSum = Integer.MIN_VALUE; // initialize largest value

		for(int i=0;i<numbers.length;i++) //first index loop
		{
			for(int j=i; j<numbers.length;j++) //second index loop
			{
				 int currentSum = 0; //current sum value
				for(int k =i; k<=j; k++) // loop to find current sum
				{
					currentSum += numbers[k];
				}
				largestSum = Math.max(largestSum, currentSum); // compare between current and largest sum
			}
		}
		
		return largestSum; // return largest sum
	}
	public int bruteForceGetMaxSub() // Second worst way to find largest sum
	{
		int largestSum = Integer.MIN_VALUE; // initialize largest sum
		int currentSum; // initialize current sum 
		for(int i =0;i<numbers.length;i++) // first index counter
		{
			currentSum = 0; // reset current sum
			for(int j=i; j<numbers.length;j++) // second index counter
			{
				currentSum += numbers[j]; // add most recent value to current sum
				largestSum = Math.max(largestSum, currentSum); // compare between largest and current sum
			}
		}
		
		return largestSum; // return largest sum 
	}
	public int getKadanesMaxSub() // Best way to find largest sum
	{
		int currentMax = 0; // initialize current sum 
		int totalMax = 0; // initialize final sum
		for(int i =0;i<numbers.length;i++) // loop through array 
		{
			currentMax = Math.max(currentMax +numbers[i], numbers[i]); //compare between last max+the new value, and the new value
			totalMax = Math.max(totalMax, currentMax); // compare between total max and current max
		}
		return totalMax; // return current max
	}

}

