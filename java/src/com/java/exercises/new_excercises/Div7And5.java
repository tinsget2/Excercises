package com.java.exercises.new_excercises;

import java.util.ArrayList;
import java.util.List;

public class Div7And5 {
	public static void main(String[] args) {		
		List<Integer> a = div7A5();
		
		System.out.println(a.size());
		for(int x : a) {
			System.out.println(x);
		}
	}
	
	public static List<Integer> div7A5() {
		List<Integer> store = new ArrayList<Integer>();
		int i=1500;
		int a = 0;
		while(i<=2700) {
			a++;
			if(i%5 == 0) {					
				if(i%7 == 0) {
					store.add(i);
					i=i+30;
				}
				i = i+5;
			}else {
				i = i+1;
			}
		}
		System.out.println(a);
		return store;
	}
	
	public static List<Integer> div(){
		List<Integer> store = new ArrayList<Integer>();
		for(int i=1500; i<=2700; i++) {
			if(i%5==0 && i%7==0) {
				store.add(i);
			}
		}
		return store;
	}
}
