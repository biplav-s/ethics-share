package com.ibm.ethics.biasspec.model;

public class DataUnit {
	private String name;
	private double frac;

	public String getName() {
		return name;
	}

	public double getFrac() {
		return frac;
	}
	
	/**
	 * String representation of object
	 */
	public String toString() {
		return " \t\t\t* name = " + getName() + ", frac = " + getFrac();
	}
}