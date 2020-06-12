package com.ibm.ethics.biasspec.reader;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;

import com.google.gson.Gson;
import com.ibm.ethics.biasspec.model.TestingContext;

/**
 * Reader for bias specification in a JSON file October 2017
 * 
 * @author Biplav Srivastava
 * 
 */
public class BiasSpecReader {

	public static TestingContext[] ctxs;

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		loadConfigs();
	}

	/**
	 * Load config files
	 */
	public static void loadConfigs() {

		// String file = "data/sample.json";
		String file = "../data/input/biasTestParameters.json";

		String dataRead = loadJSONFile(file);

		// --------------------------------------------------
		// Check reading status
		
		if (dataRead != null) {
			System.out.println("STATUS: read file - " + file);
			// System.out.println("STATUS: content - \n" + dataRead);
		} else {
			System.out.println("STATUS: failed to read file - " + file);
		}

		// --------------------------------------------------
		// Now parse the JSON and list the specs
		
		Gson gson = new Gson();
		ctxs = gson.fromJson(dataRead, TestingContext[].class);

		System.out.println("STATUS: read - " + ctxs.length + " test specs.");
		for (int i = 0; i < ctxs.length; i++) {
			// Print each specification read
			System.out.println(ctxs[i]);
		}
		
		// --------------------------------------------------
		// All done
		

	}

	/**
	 * Read passed file with JSON content
	 * 
	 * @param fileName
	 * @return
	 */
	static public String loadJSONFile(String fileName) {

		String data = "";

		try {

			InputStream inputStream = new FileInputStream(fileName);
			DataInputStream in = new DataInputStream(inputStream);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));
			String strLine;
			while ((strLine = br.readLine()) != null) {
				data += strLine + "\n";
			}
			in.close();
			return data;

		} catch (Exception e) {
			return null;
		}
	}

	/**
	 * Write JSON data to file passed. Return boolean depending on whether
	 * operation succeeded or not.
	 * 
	 * @param fileName
	 * @param data
	 * @return
	 */
	static public boolean writeJSONFile(String fileName, String data) {

		try {

			// -----------------------------------------------------------
			// -----------------------------------------------------------
			// Open the summary file
			OutputStream os = new BufferedOutputStream(new FileOutputStream(fileName));

			// Write the data
			os.write(data.getBytes());

			// -----------------------------------------------------------
			// -----------------------------------------------------------
			// Close the summary file
			os.close();

		} catch (Exception e) {
			System.out.println("Exception: Could not write to file - " + fileName + ". Exception is \n\t" + e);
			return false;
		}

		return true;
	}

}
