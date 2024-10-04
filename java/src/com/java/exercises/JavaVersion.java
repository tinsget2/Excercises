package com.java.exercises;

public class JavaVersion {
	
	public static void version() {
		Runtime.Version version = Runtime.version();
		
		System.out.println("Java Version: " + version);
	}
}
