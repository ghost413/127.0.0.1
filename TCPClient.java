/* This is the Java code for the client program */
import java.io.*;
import java.net.*;

class FileClient {
	
	public static void main(String argv[]) throws Exception {
		
		String fileName;		
		String lineInFile;
		FileInputStream fis;
		BufferedReader inFromFile;
		
		// create input stream from keyboard
		BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));

		
		// create client socket to connect to server
		Socket clientSocket = new Socket("localhost", 7890);

		
		// create output stream attached to client socket		
		DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());

		
		// create input stream attached to client socket
		BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));


		
		// read file name from keyboard
		System.out.print("Please input the file name: ");
		fileName = inFromUser.readLine();
		
		try {
			// open file by file name and create input stream attached to file
			fis = new FileInputStream(fileName);
			inFromFile = new BufferedReader(new InputStreamReader(fis));			
		} catch (Exception e) {
			// file does not exist or other error happens
			System.out.println(e);
			clientSocket.close();
			return;
		}
		
		// send file name+"\n" to server
		outToServer.writeBytes(fileName + '\n');


		
		// read line from file and write "line:"+line+"\n" to server until file end
		while((lineInFile = inFromFile.readLine()) != null) {
			outToServer.writeBytes("line: " + lineInFile + "\r\n");


		}
		
		// send "done" to server to indicate file end
		outToServer.writeBytes("done");


		
		// close file and socket
		inFromFile.close();
		fis.close();		
		clientSocket.close();


	}
}
