package com.java.exercises.new_excercises;

public class print0to6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		printNum();
	}
	public static void printNum() {
		for(int i=0; i<7; i++) {
			if(i==3 || i==6) {
				continue;
			}
			System.out.println(i);
		}
	}
}
