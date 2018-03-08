/* This is the Java code for the client program */
import java.io.*;
import java.net.*;

class FileClient {
	
	public static void main(String argv[]) throws Exception {
		
		String fileName;
		String lineInFile;
		FileInputStream fis;
		BufferedReader inFromFile;
		byte[] sendData;
		DatagramPacket sendPacket;
		
		// create input stream from keyboard
		BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
		

		// create client socket
		DatagramSocket clientSocket = new DatagramSocket();

		
		// translate server's host name to IP address 
		InetAddress IPAddress = InetAddress.getByName("localhost");
		

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


		// create datagram for file name with data-to-send, length, IP address and port number
		sendData = fileName.getBytes();

		sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 7890);

		
		// send datagram to server
		clientSocket.send(sendPacket);
		
		// read line from file until file end
		while((lineInFile = inFromFile.readLine()) != null) {
			// create datagram for "line:"+line+"\r\n" with data-to-send, length, IP address and
			// port number 
			sendData = ("line:" + lineInFile + "\r\n").getBytes();
			sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 7890);

			
			// send datagram to server
			clientSocket.send(sendPacket);
		}
		
		// create datagram for "done" with data-to-send, length, IP address and port number
		sendData = "done".getBytes();

		sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 7890);

		
		// send datagram to server
		clientSocket.send(sendPacket);
		
		// close file and socket
		inFromFile.close();
		fis.close();
		clientSocket.close();

	}
}
