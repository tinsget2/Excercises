package com.java.exercises.Data_Structure;

public class Linked_List {
	
	static class node{
		int data;
		node next;
		node(int value){
			data = value;
			next = null;
		}
	}
	
	static class nodeName{
		String name;
		nodeName next = null;
		
		nodeName(String value){
			name = value;
			next = null;
		}
	}
	
	static nodeName headName = null;
	
	static void insertName(String name) {
		nodeName p = new nodeName(name);
		
		p.next = headName;
		
		headName = p;
		
		System.out.println("Node: " + headName + " Data: "+ headName.name);
	}
	
	
	
	
	static node head;
	
	static void insertatbeginig(int data) {
		node lk = new node(data);
		System.out.println("Head node: " +lk);
		lk.next = head;
		System.out.println("Head node: " +lk.next);
		head = lk;
		System.out.println("Head node: " +head);
		
	}
	
	static void printName() {
		nodeName p = headName;
		
		while(p != null) {			
			System.out.println("Node: " + p + " Data: " + p.name + " nextnode: " + p.next);
			
			p = p.next;
		}
	}
	
	
	static void printList() {
		node p = head;
		
		while(p != null) {
			System.out.println(p.next);
			p = p.next;
		}
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		insertatbeginig(12);
//		insertatbeginig(22);
//		insertatbeginig(30);
//		insertatbeginig(44);
//		insertatbeginig(50);
		
//		printList();
		insertName("Tinsae");
		insertName("Getachew");
		insertName("Kebede");
		
		System.out.println("Print out");
		printName();
		
		
	}
	
		

}
