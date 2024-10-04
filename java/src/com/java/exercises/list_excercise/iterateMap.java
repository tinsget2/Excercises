package com.java.exercises.list_excercise;

import java.util.HashMap;
import java.util.Map;

public class iterateMap {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Map<Integer, Integer> xx = new HashMap<>();
		for(int i=1; i<=10; i++) {
			xx.put(i, i*10);
		}
		iterateMapItem(xx);
	}
	
	public static void iterateMapItem(Map<Integer, Integer> a) {
		for(int x : a.keySet()) {
			System.out.println(a.get(x));
		}
	}

}
