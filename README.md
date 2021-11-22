# Wireless Sensor Network
Design Wireless Sensor Network (WSN) in GNU Radio

## This network contains four nodes
![image](https://user-images.githubusercontent.com/47606879/142787395-e59d46bc-81bb-441e-b433-e8f9bb8ee58a.png)

I uses this MATLAB code to generate codes for Preamble
- codeGenerator(n)
- function [rby] = codeGenerator(n)
- rby = '';
- for k = 1:n
-     rby = rby + string(randi(2 , 1)-1);
- end
- end


## This is the design in the GNU Radio

![wsn](https://user-images.githubusercontent.com/47606879/142787315-d31ce29b-b996-4495-b0ec-383100976764.png)


## Input
I used this picture as the input (it is in the "WSN" folder)

![image](https://user-images.githubusercontent.com/47606879/142787623-09c0ab2e-eebd-460b-81e7-e56433f869e4.png)

## Outputs
These are the results:
### 1 to 2
![image](https://user-images.githubusercontent.com/47606879/142787612-8b1ecb28-abd2-4d56-aa7d-34c57b3ab701.png)
### 1 to 3
![image](https://user-images.githubusercontent.com/47606879/142787637-bedfe883-c58e-4d3d-804e-42a9bee9521c.png)
### 1 to 4
![image](https://user-images.githubusercontent.com/47606879/142787649-73a78409-f6e0-4afd-8c44-d5a6c8731cee.png)

### 1 to 2 to 4
![image](https://user-images.githubusercontent.com/47606879/142787678-d6a42263-b7c1-4622-b472-e56792da61db.png)

### 1 to 2 to 3
![image](https://user-images.githubusercontent.com/47606879/142787697-a56fc784-a75c-4010-b09b-987f08ad31c1.png)

### 1 to 3 to 4
![image](https://user-images.githubusercontent.com/47606879/142787742-a96e5998-53db-4a82-869b-425ba9e7b5e1.png)

### 1 to 2 to 3 to 4
![image](https://user-images.githubusercontent.com/47606879/142787723-85062bed-d312-4faa-81bf-b53df09e2f6f.png)


* There are two folders as below:
	- BER : contains the simulation of Bit Error Rate for all nodes.
	- WSN : contains the simulation of Wireless Sensor Network which includes 4 nodes with linear topology 
		and an image file has been named "input.jpg" for testing
