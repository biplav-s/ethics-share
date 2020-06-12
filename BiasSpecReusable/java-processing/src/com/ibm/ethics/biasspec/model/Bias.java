package com.ibm.ethics.biasspec.model;

public class Bias {

	private Data[] bias;
	private Data[] unbias;

	public Data[] getBiased() {
		return bias;
	}

	public Data[] getUnbiased() {
		return unbias;
	}
	
	/**
	 * String representation of object
	 */
	public String toString() {
		
		String result = "";
		
		if(unbias != null) {
			result += "\t Unbias specs follow = \n"; 
			for(int i=0; i<unbias.length; i++) {
				result += "\t \t unbias spec (" + (i+1) + ") of " + unbias.length +  "\n"; 
				result += unbias[i].toString() + "\n";
			}	
		}
		
		if(bias != null) {
			result += "\t Bias specs follow = \n"; 
			for(int i=0; i<bias.length; i++) {
				result += "\t \t bias spec (" + (i+1) + ") of " + bias.length +  "\n"; 
				result += bias[i].toString() + "\n";
			}	
		}
		
	
		return result;
	}
}
