package com.java.exercises.new_excercises;

import java.util.Scanner;

public class ReverseWord {
	public static void main(String[] args) {
		try (// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in)) {
			System.out.println("Enter a word");
			String inp = input.nextLine();
			String ans = reverse(inp);
			System.out.println(ans);
		}
	}
	
	public static String reverse(String a) {
		String xx = "";
		for(int i=a.length()-1; i>=0; i--) {
			xx = xx+ a.charAt(i);
		}
		return xx;
	}
}
