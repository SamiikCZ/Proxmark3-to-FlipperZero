#!/usr/bin/env python3
import json
import sys
import os

def hex_pairwise(hex_str):
    return [hex_str[i:i+2].upper() for i in range(0, len(hex_str), 2)]

def convert_json_to_flipper_text(input_path):
    with open(input_path, "r") as f:
        data = json.load(f)
    card_info = data["Card"]
    uid_hex_str = card_info["UID"]
    atqa_hex = card_info["ATQA"]
    sak_hex = card_info["SAK"]
    uid_pairs = hex_pairwise(uid_hex_str)
    uid_str_for_file = " ".join(uid_pairs)
    atqa_pairs = hex_pairwise(atqa_hex)
    atqa_pairs.reverse()
    atqa_str_for_file = " ".join(atqa_pairs).upper()
    sak_pairs = hex_pairwise(sak_hex)
    sak_str_for_file = " ".join(sak_pairs).upper()
    blocks = data["blocks"]
    header_lines = [
        "Filetype: Flipper NFC device",
        "Version: 4",
        "# Device type can be ISO14443-3A, ISO14443-3B, ISO14443-4A, ISO14443-4B, ISO15693-3, FeliCa, NTAG/Ultralight, Mifare Classic, Mifare Plus, Mifare DESFire, SLIX, ST25TB, EMV",
        "Device type: Mifare Classic",
        "# UID is common for all formats",
        f"UID: {uid_str_for_file}",
        "# ISO14443-3A specific data",
        f"ATQA: {atqa_str_for_file}",
        f"SAK: {sak_str_for_file}",
        "# Mifare Classic specific data",
        "Mifare Classic type: 1K",
        "Data format version: 2",
        "# Mifare Classic blocks, '??' means unknown data",
    ]
    block_lines = []
    for i in range(64):
        b = blocks[str(i)]
        pair_list = hex_pairwise(b)
        block_data_str = " ".join(pair_list)
        line = f"Block {i}: {block_data_str}"
        block_lines.append(line)
    output_filename = f"MFC_{uid_hex_str.upper()}_{os.path.basename(input_path)}.nfc"
    output_filename = output_filename.replace(".json", "")
    with open(output_filename, "w") as f_out:
        for hl in header_lines:
            f_out.write(hl + "\n")
        for bl in block_lines:
            f_out.write(bl + "\n")
    print(f"File '{output_filename}' created.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_to_flipper_text.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]
    if not os.path.exists(json_file):
        print(f"File '{json_file}' not found.")
        sys.exit(1)
    convert_json_to_flipper_text(json_file)