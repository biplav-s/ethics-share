package com.ibm.ethics.biasspec.model;

public class TestingContext {

	// --------------
	private String name;

	public String getName() {
		return name;
	}

	// --------------
	private String[] triggers;

	public String[] getTriggers() {
		return triggers;
	}

	// --------------
	private String[] values;

	public String[] getValues() {
		return values;
	}

	// -----------
	public Bias dataspec;

	public Bias getDataSpec() {
		return dataspec;
	}

	// -----------
	/**
	 * String representation of object
	 */
	public String toString() {

		String result = "";

		if (getName() != null)
			result += "Spec context name = " + getName() + "\n";

		if (getTriggers() != null) {
			result += "\t Triggers:\n";			
			for (int i = 0; i < triggers.length; i++) {
				result += "\t\t " + triggers[i] + "\n";	
			}
		}
		
		if (getValues() != null) {
			result += "\t Values:\n";			
			for (int i = 0; i < values.length; i++) {
				result += "\t\t " + values[i] + "\n";	
			}
		}		
		
		if(dataspec != null)
			result += dataspec.toString();

		return result;
	}

}
