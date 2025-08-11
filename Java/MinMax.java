import java.util.*;
// java Program to create an array and see its minimum and maximum element
public class Minmax{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter size of array");
		int sz= sc.nextInt();
		int num[] = new int[sz];
		int min = num[0];
		int max = num[0];
		System.out.println("Enter the elements of array:");
		for(int i=0; i<sz; i++){
			num[i]= sc.nextInt();
			}
		for (int i=0; i<= sz; i++){
			if(num[i] > max){
				num[i]= max;
				}
			if(num[i]< min){
				num[i]=min;
				}
			}
		System.out.print("The Minumum and Maximum Elements of the array are: " + max + min);
		
			}
			}		
