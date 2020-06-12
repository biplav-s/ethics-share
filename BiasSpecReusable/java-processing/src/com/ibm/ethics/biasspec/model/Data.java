package com.ibm.ethics.biasspec.model;

public class Data {
	private DataUnit[] data;
	

	public  DataUnit[] getDataUnits() {
		return data;
	}
	
	/**
	 * String representation of object
	 */
	public String toString() {
		
		String result = "";
		if(data == null)
			return result;
		
		for(int i=0; i<data.length; i++) {
			result += data[i].toString() + "\n";
		}		
		return result;
	}
}