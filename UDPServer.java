/* This is the Java code for the server program */
import java.io.*;
import java.net.*;

class FileServer {
	
	public static void main(String argv[]) throws Exception {
		
		String fileName;
		FileOutputStream fos;
		DataOutputStream outToFile;
		String lineFromClient;
		byte[] receiveData = new byte[1024];
		DatagramPacket receivePacket;
		
		// create server socket
		DatagramSocket serverSocket = new DatagramSocket(7890);
		
		while(true) {
			// create space for received datagram and then receive datagram
			receivePacket = new DatagramPacket(receiveData, receiveData.length);

			serverSocket.receive(receivePacket);
			
			// read file name from received datagram
			fileName = new String(receivePacket.getData(), 0, receivePacket.getLength());

			
			try {
				// create file by file name and output stream attached to file
				fos = new FileOutputStream(fileName);				
				outToFile = new DataOutputStream(fos);				
			} catch (Exception e) {
				// any error happens
				System.out.println(e);				
				serverSocket.close();				
				return;				
			}
			
			// read "line:"+line from client and write line to file until receive "done" indicating
			// file end
			do {
				// create space for received datagram and then receive datagram
				receivePacket = new DatagramPacket(receiveData, receiveData.length);

				serverSocket.receive(receivePacket);
				
				// read "line:"+line from received datagram
				lineFromClient = new String(receivePacket.getData(), 0, receivePacket.getLength());

				
				if (lineFromClient.equals("done")) break;
				outToFile.writeBytes(lineFromClient.substring("line:".length()));
			}while(!lineFromClient.equals("done"));
			
			// close file
			fos.close();
			outToFile.close();
		}
	}
}
