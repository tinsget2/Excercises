package com.java.exercises.list_excercise;

import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;

public class GenerateDictionary {

	public static void main(String[] args) {
		try (// TODO Auto-generated method stub
			Scanner input = new Scanner(System.in)) {
			System.out.println("Enter the nth number");
			int num = input.nextInt();
			generate(num);
		}catch(Exception e) {
			System.out.println(e);
		}
		
	}
	public static void generate(int n) {
		Map<Integer, Integer> dict = new HashMap<>(); 
		for(int i=1; i<=n; i++) {
			dict.put(i, i*i);
		}
		System.out.println(dict);
	}

}
