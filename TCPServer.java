/* This is the Java code for the server program */
import java.io.*;
import java.net.*;

class FileServer {
	
	public static void main(String argv[]) throws Exception {
		
		String fileName;
		FileOutputStream fos;
		DataOutputStream outToFile;
		String lineFromClient;
		BufferedReader inFromClient;
		DataOutputStream  outToClient;
		Socket connectionSocket;
		
		// create welcoming socket
		ServerSocket welcomeSocket = new ServerSocket(7890);

		
		while(true) {
			
			// wait on welcoming socket accept() method for client contact to create and
			// return new socket connecting to client
			connectionSocket = welcomeSocket.accept();

			
			// create input stream attached to client socket 
			inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));

			
			// create output stream attached to client socket
			outToClient = new DataOutputStream(connectionSocket.getOutputStream());

			
			// read file name from client
			fileName = inFromClient.readLine();

			
			try {
				// create file by file name and output stream attached to file
				fos = new FileOutputStream(fileName);
				outToFile = new DataOutputStream(fos);
			} catch (Exception e) {
				// any error happens
				System.out.println(e);
				connectionSocket.close();
				return;
			}
			
			// read "line:"+line from client and write line to file until receive "done"
			// indicating file end
			while ((lineFromClient = inFromClient.readLine()) != null) {
				if (lineFromClient.equals("done")) break;
				outToFile.writeBytes(lineFromClient.substring("line: ".length()) +"\r\n");
			}
			
			// close file and socket
			fos.close();
			outToFile.close();
			connectionSocket.close();


		}
	}
}
