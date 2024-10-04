package com.java.exercises.list_excercise;

import java.util.ArrayList;
import java.util.List;

public class SortArrayList {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<String> sortArr = new ArrayList<String>();
		
		sortArr.add("z");
		sortArr.add("b");
		sortArr.add("a");
		sortArr.add("l");
		sortArr.add("k");
		
		String a,b;
		System.out.println(sortArr);
//		System.out.println(sortArr.size());
		for(int i=0; i<sortArr.size(); i++) {
			for(int j=0; j<sortArr.size(); j++) {
				if(j == i) {
					
				}else {
					a = sortArr.get(i);
					b = sortArr.get(j);
					
//					System.out.println(a.compareTo(b));
					if(a.compareTo(b) <    0) {
						sortArr.set(i, b);
						sortArr.set(j, a);
					}
				}
			}
		}
		System.out.println(sortArr);
		
		
		List<Integer> numSort = new ArrayList<Integer>();
		
		numSort.add(5);
		numSort.add(6);
		numSort.add(9);
		numSort.add(4);
		numSort.add(2);
		numSort.add(3);
		numSort.add(5);
		
		System.out.println(numSort);
		
		int temp1, temp2;
		for(int i=0; i<numSort.size(); i++) {
			for(int j=0; j<numSort.size(); j++) {
				if(i==j) {
					
				}else {
					temp1 = numSort.get(i);
//					temp2 = numSort.get(j);
					
					if(numSort.get(i) < numSort.get(j)) {
						numSort.set(i, numSort.get(j));
						numSort.set(j, temp1);
					}
				}
			}
		}
		
		System.out.println(numSort);
		
	}
}
