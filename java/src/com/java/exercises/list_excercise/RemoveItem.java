package com.java.exercises.list_excercise;

import java.util.Map;
import java.util.HashMap;

public class RemoveItem {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Map<String, String> item = removeDict("Middle Name");
		System.out.println(item);
	}
	public static Map<String, String> removeDict(String a){
		Map<String, String> items = new HashMap<>();
		items.put("Name", "Tinsae");
		items.put("Middle Name", "Getachew");
		items.put("Last Name", "Kebede");
		
		items.remove(a);
		return items;
	}
}
