package com.java.exercises.new_excercises;

import java.util.Scanner;

public class AddThreeNum {
	public static void main(String[] args) {
		try (Scanner input = new Scanner(System.in)) {
			//Declaring three integer values
			int a, b,c;
			//Declaring a variable to store value
			int sum;
			
			System.out.println("Enter the first number");
			a = input.nextInt();
			
			System.out.println("Enter the second number");
			b = input.nextInt();
			
			System.out.println("Enter the third number");
			c = input.nextInt();
			
			sum = a+b+c;
			
			System.out.println(sum);
		}

	}
}
