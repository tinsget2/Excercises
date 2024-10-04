package com.java.exercises;

public class SwapString {
	public static void swap(String first, String second) {
		String tmp = first;
		second = first;
		first = tmp;
		System.out.printf("First: %s, Second: %s", first, second);
	}
}
