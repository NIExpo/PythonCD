# Py2VS_UDP

This example demonstrates a workflow to communicate Python code with the VeriStand engine through UDP. Since the communication is not through the VeriStand gateway, the Python code can run on any OS including Linux RT.

## Python Example

This is what the python example script *data_generator.py* does:


1 Opens a UDP socket that will send packages to IP 127.0.0.1 (localhost) and to port 61557. This can be easily changed from the script if it was required.

2 Generates a message with four random numbers and packages each of them as floating32 along with a header that includes the total package size in bytes.

3 The message is sent through UDP.

4 Steps 2 and 3 are repeated once every 2 seconds until a keyboard interruption is detected.

## VeriStand Configuration

On the VeriStand side, we use the [UDP Data Link Custom Device](https://github.com/NIVeriStandAdd-Ons/UDP-Data-Link-Custom-Device) to read the message and map the values to four VeriStand channels.

The provided *rx_signals.csv* file is used to configure the channels to receive by the UDP custom device.

## How to Run on Linux RT?

1. [SSH into the cRIO] (https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z000000P8bQSAS&l=en-US) using something like Putty.

2. Run the commands:

	opkg update
	opkg install python3 python3-misc
	
3. Use something like WinSCP or WebDav to transfer the py script into the cRIO. For example transfer it into /home/admin.

4. Run the script from Putty:
	
	python3 /home/admin/data_generator.py
	
	
5. Open VeriStand project and system definition file. Change the target IP Address and others settings as needed.

6. Deploy VS project and open UI. Channels should update as the Python script runs.


## Future Improvements

Program a service in LabVIEW that transfers and runs the Python script on the target automatically when VS project is deployed. 

[Adding a VeriStand Service](http://zone.ni.com/reference/en-XX/help/372846M-01/veristand/add_services/)

For the newer project explorer, a VI file can be added. Then right-click the VI and select *Run on Deploy*.

Plink, which is a light command line interface for Putty can be called from LabVIEW using System Exec VI to transfer the script using SCP and to run it.

The python script can be extended to also receive data from the VS system. For example, it could receive a stop signal that the LabVIEW service can trigger to high when the system is undeploying.






	









