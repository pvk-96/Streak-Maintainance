import java.util.*;
// java Program to create an array and show its properties
public class Arr{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter size of array");
		int sz= sc.nextInt();
		int num[] = new int[sz];
		System.out.println("Enter the elements of array:");
		for(int i=0; i<sz; i++){
			num[i]= sc.nextInt();
			}
		System.out.print("The Elements of the array are: ");
		for(int i=0; i<sz; i++){
			System.out.println(num[i]);
			}
			}
			}		
