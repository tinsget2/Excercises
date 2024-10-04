package com.java.exercises.list_excercise;

import java.util.Map;
import java.util.HashMap;

public class AddDictElement {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		addDict();
	}
	public static void addDict() {
		Map<Integer, Integer> dict = new HashMap<Integer, Integer>();
		
		dict.put(0, 10);
		dict.put(1, 20);
		
		for(int i : dict.keySet()) {
			System.out.println(dict.get(i));
		}
		
		dict.put(2, 30);
		
		for(int i : dict.keySet()) {
			System.out.println(dict.get(i));
		}
	}

}
