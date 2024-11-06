# Hashcat Cheat Sheet

> A comprehensive guide for using Hashcat, covering hash modes, attack types, and various options.

---

## 🔢 Hash Modes
- `0` : MD5
- `100` : SHA-1
- `1400` : SHA-256
- `1000` : NTLM
- `3200` : bcrypt
- `300` : MySQL5
- `2500` : WPA/WPA2
- `1450` : HMAC-SHA256
- `1750` : HMAC-SHA512

For a full list of hash modes, check [Hashcat's official documentation](https://hashcat.net/wiki/doku.php?id=example_hashes).

---

## ⚙️ Attack Modes
| Mode          | Flag | Description                              |
|---------------|------|------------------------------------------|
| Dictionary    | `-a 0` | Crack using a wordlist                    |
| Combination   | `-a 1` | Combine words from two wordlists         |
| Brute-Force   | `-a 3` | Brute-force using a mask                 |
| Hybrid Dict+Mask | `-a 6` | Use dictionary with mask suffix     |
| Hybrid Mask+Dict | `-a 7` | Use mask with dictionary suffix      |

---

## 🔍 Common Commands
- `hashcat -m <hash_type> -a <attack_mode> -o <output_file> <hash_file> <dictionary_or_mask>`: Basic command format.
- `--show`: Display cracked hashes.
- `--username`: Ignore username part in hash file.
- `--status`: Display the status during cracking.
- `--potfile-disable`: Disable saving cracked hashes to the potfile.

---

## 🎭 Masks
- `?l` : Lowercase letter
- `?u` : Uppercase letter
- `?d` : Digit
- `?s` : Special character
- `?a` : Any character

### Example Mask: `?a?a?a?a?a`
Represents any 5-character combination including letters, digits, and symbols.

---

## 📂 Output Options
- `-o <output_file>`: Output file for cracked hashes.
- `--outfile-autohex-disable`: Disable hex encoding for special characters.
- `--potfile-path <file>`: Specify path for the potfile (where cracked hashes are stored).

---

## ⚡ Performance Options
- `-w <level>`: Set workload profile (1 to 4, 4 being the fastest and most resource-intensive).
- `--force`: Ignore warnings and run Hashcat.
- `--session <session_name>`: Save session progress to allow resuming later.

---

## Examples

### 1. Dictionary Attack on NTLM Hash
```bash
hashcat -m 1000 -a 0 -o cracked.txt hashes.txt /path/to/wordlist.txt
hashcat -m 0 -a 3 -o cracked.txt hashes.txt ?a?a?a?a?a
hashcat -m 1400 -a 6 -o cracked.txt hashes.txt /path/to/wordlist.txt ?d?d?d
