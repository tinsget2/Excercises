package com.java.exercises.new_excercises;

import java.util.Scanner;

public class Guess {
	public static void main(String[] args) {
		try (// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in)) {
			boolean test = true;
			while(test) {
				System.out.println("Guess The number");
				int a = input.nextInt();
				int guess = (int)(Math.random() * 10);
				if(a==guess) {
					System.out.println("Well Done");
					test = false;
				}
			}
		}
		
		
	}
}
