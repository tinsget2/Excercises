package com.java.exercises.new_excercises;

import java.util.Scanner;

public class DigitLetter {

	public static void main(String[] args) {
		try (// TODO Auto-generated method stub
			Scanner input = new Scanner(System.in)) {
			System.out.println("Enter a string");
			String temp = input.nextLine();
			figLetter(temp);
		}catch(Exception e) {
			System.out.println(e);
		}

	}
	
	public static void figLetter(String a) {
		int d =0;
		int l = 0;
		for(int i=0; i<a.length(); i++) {
			if(Character.isDigit(a.charAt(i))) {
				d++;
			}else if(Character.isAlphabetic(a.charAt(i))) {
				l++;
			}else {
				
			}
		}
		
		System.out.println("Digit: " + d);
		System.out.println("Letter:" + l);
	}

}
