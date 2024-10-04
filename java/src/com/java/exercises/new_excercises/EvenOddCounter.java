package com.java.exercises.new_excercises;
//import java.util.Scanner;
public class EvenOddCounter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Scanner input = new Scanner(System.in);
		int[] arr = {1,2,3,4,5,6,7,8,9};
		
		int[] count = counter(arr);
		System.out.println("Number of even numbers "+count[0]);
		System.out.println("Number of odd numbers "+count[1]);
	}
	public static int[] counter(int[] num) {
		int evenCounter = 0;
		int oddCounter = 0;
		
		for(int x : num) {
			if(x%2==0) {
				evenCounter++;
			}else {
				oddCounter++;
			}
		}
		int[] counter = {evenCounter, oddCounter};
		return counter;
	}
}
