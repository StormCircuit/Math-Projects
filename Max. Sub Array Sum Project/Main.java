package maximumSubArraySum;

public class Main {

	public static void main(String[] args) {
		int [] numbers = new int [] {3,-7,9,-5,16,-7,4,2,-4,12,1,-67,45,-100,73,-19,51,-19,49,85,70,12,30,-33,-62,-86,18,-29,-47,12,-75,9,30,-44,28,-2,52,-29,15,-91,-75,9,30,-44,28,-2,52,-29,15,-913,-7,9,-5,16,-7,4,2,-4,12,1,-67,45,-100,73,-19,51,-19,49,85,70,12,30,-33,-62,-86,18,-29,-47,12,-75,9,30,-44,28,-2,52,-29,15,-91,-75,9,30,-44,28,-2,52,-29,15,-913,-7,9,-5,16,-7,4,2,-4,12,1,-67,45,-100,73,-19,51,-19,49,85,70,12,30,-33,-62,-86,18,-29,-47,12,-75,9,30,-44,28,-2,52,-29,15,-91,-75,9,30,-44,28,-2,52,-29,15,-913,-7,9,-5,16,-7,4,2,-4,12,1,-67,45,-100,73,-19,51,-19,49,85,70,12,30,-33,-62,-86,18,-29,-47,12,-75,9,30,-44,28,-2,52,-29,15,-91,-75,9,30,-44,28,-2,52,-29,15,-913,-7,9,-5,16,-7,4,2,-4,12,1,-67,45,-100,73,-19,51,-19,49,85,70,12,30,-33,-62,-86,18,-29,-47,12,-75,9,30,-44,28,-2,52,-29,15,-91,-75,9,30,-44,28,-2,52,-29,15,-913,-7,9,-5,16,-7,4,2,-4,12,1,-67,45,-100,73,-19,51,-19,49,85,70,12,30,-33,-62,-86,18,-29,-47,12,-75,9,30,-44,28,-2,52,-29,15,-91,-75,9,30,-44,28,-2,52,-29,15,-91};
		SubarraySum Sum = new SubarraySum(numbers);
		long startTime = System.nanoTime();
		int bestSum = Sum.getKadanesMaxSub();
		long endTime = System.nanoTime();
		System.out.println("The best sum you can get for this array is " + bestSum);
		System.out.println( "This took "+ (endTime-startTime)+ " ns");
		startTime = System.nanoTime();
		int secondBestSum = Sum.bruteForceGetMaxSub();
		endTime = System.nanoTime();
		System.out.println("The best sum you can get for this array is " + secondBestSum);
		System.out.println( "This took "+ (endTime-startTime)+ " ns");
		startTime = System.nanoTime();
		int thirdBestSum =Sum.worseBruteForceGetMaxSub();
		endTime = System.nanoTime();
		System.out.println("The best sum you can get for this array is "+ thirdBestSum);
		System.out.println( "This took "+ (endTime-startTime)+ " ns");
	}

}
