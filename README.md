# Proxmark3 to FlipperZero
 Python .json to .nfc

This Python script converts a Proxmark3 MIFARE Classic JSON dump (FileType: “mfc v2”) into a text-based .nfc file suitable for Flipper Zero. It reads the JSON file, processes UID/ATQA/SAK data, and generates a file with a header and 64 blocks.

Usage:

	1.	Place the script and your JSON dump in the same directory.
 
	2.	In a terminal, run:

python convert.py <json_file>


	3.	A .nfc file will be created, including a Flipper‐style header.
	4.	Copy the generated .nfc file to your Flipper Zero’s SD card (NFC folder or similar).
	5.	Test it on Flipper Zero to see if it is recognized and emulated successfully.

Features:

	Reads a JSON dump from Proxmark3 (MIFARE Classic 1K).
 
	Outputs a text‐based .nfc file with a Flipper‐style header.
 
	Attempts to match Flipper Zero’s expected format (Version 4, Mifare Classic).

Limitations:

	Some firmware versions of Flipper Zero may require different version numbers or device type strings in the header.
 
	If Flipper Zero rejects the file, you may need to adjust ATQA byte order, version, or device type.
