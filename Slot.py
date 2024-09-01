from web3 import Web3
import time
from termcolor import colored
import shutil

# Konfigurasi
rpc_url = 'https://hybrid-testnet.rpc.caldera.xyz/http'
chain_id = 1225
contract_address = '0x33C217042a6A5475d066FC48d56243473262a8fd'
private_key = 'ISI PRIVATE KEY EVM' #GANTI PRIVATE KEY EVM ANDA
my_address = 'ISI ADDRESS EVM' #GANTI ADDRESS EVM ANDA
explorer_url = 'https://explorer.buildonhybrid.com/tx/'

# ASCII Art
ascii_art = """
 __     ___ _    _ _            _     _ 
 \ \   / (_) | _(_) |_ ___  ___| |__ (_)
  \ \ / /| | |/ / | __/ _ \/ __| '_ \| |
   \ V / | |   <| | || (_) \__ \ | | | |
    \_/  |_|_|\_\_|\__\___/|___/_| |_|_|

"""

# Tambahkan jarak dua paragraf setelah deskripsi teks
print("\n\n")

# Inisialisasi Web3
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Cek koneksi
if not web3.is_connected():
    raise ConnectionError("Gagal terhubung ke RPC")

# Keccak untuk selector method
def get_method_selector(method_name):
    return web3.keccak(text=method_name)[:4].hex()

# Selector untuk metode 'mint' dan 'spin'
mint_selector = get_method_selector('mint()')
spin_selector = get_method_selector('spin()')

# Variabel penghitung
mint_success_count = 0
spin_success_count = 0
spin_count_since_last_mint = 0
last_nonce = None

def print_ascii_art():
    # Menghitung ukuran terminal
    columns, _ = shutil.get_terminal_size()
    art_lines = ascii_art.strip().split('\n')

    # Menentukan padding
    top_padding = (columns - max(len(line) for line in art_lines)) // 2
    for line in art_lines:
        print(colored(line.center(columns), 'green'))
    print("\n" * 2)  # Jarak 2 paragraf antara ASCII art dan output transaksi

def send_transaction(method_selector):
    global mint_success_count, spin_success_count, spin_count_since_last_mint, last_nonce
    nonce = web3.eth.get_transaction_count(my_address)

    if last_nonce is not None and nonce <= last_nonce:
        nonce = last_nonce + 1  # Memperbaiki nonce jika lebih rendah dari yang terakhir digunakan

    transaction = {
        'to': contract_address,
        'value': 0,
        'gas': 2000000,
        'gasPrice': web3.to_wei('20', 'gwei'),
        'nonce': nonce,
        'data': method_selector
    }

    # Menandatangani transaksi
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

    # Mengirim transaksi
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        last_nonce = nonce  # Simpan nonce yang terakhir digunakan
    except Exception as e:
        print(f'Error mengirim transaksi: {e}')
        return None

    tx_hash_hex = web3.to_hex(tx_hash)

    # Menghitung jumlah transaksi berhasil
    if method_selector == mint_selector:
        mint_success_count += 1
    elif method_selector == spin_selector:
        spin_success_count += 1
        spin_count_since_last_mint += 1

    return tx_hash_hex

def mint_and_spin():
    global mint_success_count, spin_success_count, spin_count_since_last_mint

    if spin_count_since_last_mint >= 1000:
        # Melakukan mint dan menampilkan hasilnya
        mint_tx_hash = send_transaction(mint_selector)  # Pertama, mint token
        if mint_tx_hash:
            print(f'\nMint Txhash : {explorer_url}{mint_tx_hash} = {mint_success_count}')
        spin_count_since_last_mint = 0  # Reset penghitung transaksi spin

    # Melakukan spin dan menampilkan hasilnya
    spin_tx_hash = send_transaction(spin_selector)  # Kemudian, spin
    if spin_tx_hash:
        print(f'Spin Txhash : {explorer_url}{spin_tx_hash} = {spin_success_count}')

def main():
    print_ascii_art()
    try:
        while True:
            mint_and_spin()
            time.sleep(2)  # Delay sebelum melakukan mint dan spin berikutnya
    except KeyboardInterrupt:
        print("Bot dihentikan.")

if __name__ == '__main__':
    main()
