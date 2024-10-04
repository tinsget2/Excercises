package com.java.exercises.list_excercise;

import java.util.HashMap;

public class printSquareOfDict {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<Integer, Integer> dict = new HashMap<>();
		dict.put(1, 1);
		dict.put(2, 4);
		dict.put(3, 9);
		dict.put(4, 16);
		dict.put(5, 25);
		dict.put(6, 36);
		dict.put(7, 49);
		dict.put(8, 64);
		dict.put(9, 81);
		dict.put(10, 100);
		dict.put(11, 121);
		dict.put(12, 144);
		dict.put(13, 169);
		dict.put(14, 196);
		dict.put(15, 225);
		
		squareDict(dict);
		
	}
	public static void squareDict(HashMap<Integer, Integer> a) {
		for(int x : a.keySet()) {
			if(x>=1 && x<=15 && a.get(x) == x*x) {
				System.out.println(x + ","+ a.get(x));
			}
		}
	}

}
