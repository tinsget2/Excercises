package com.java.exercises.list_excercise;

import java.util.Map;
import java.util.HashMap;

public class SumMapElements {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Map<Integer, Integer> a = new HashMap<>();
		
		for(int i=1; i<=10; i++) {
			a.put(i, i*10);
		}
		
		int sum = sumDict(a);
		System.out.println(sum);
		
		float mul = mulDict(a);
		System.out.println(mul);
	}
	
	public static int sumDict(Map<Integer, Integer> val) {
		int sum = 0;
		for(int x : val.keySet()) {
			sum += val.get(x);
		}
		
		return sum;
	}
	
	public static float mulDict(Map<Integer, Integer> val) {
		float mul=1;
		for(int x : val.values()) {
			mul *= x;
		}
		
		return mul;
	}

}
