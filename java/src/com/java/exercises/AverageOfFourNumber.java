package com.java.exercises;

public class AverageOfFourNumber {
	public static void average(int num1, int num2, int num3, int num4) {
		float sum = num1 + num2 + num3 + num4;
		float avg = sum/4;
		System.out.printf("Average: %.2f", avg);
	}
}
