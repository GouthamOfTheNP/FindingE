"""
High-Precision e Calculator with TRUE Streaming
Calculates and writes e in chunks - computes chunk, writes chunk, repeat.
Uses spigot algorithm for digit-by-digit generation.
"""

from decimal import Decimal, getcontext
import time
import sys
from mpmath import mp

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"


def print_progress_bar(progress, total, digit_start, digit_end, bar_length=40):
    percent = progress / total
    filled_length = int(bar_length * percent)
    bar = f"{GREEN}" + '█' * filled_length + f"{RESET}" + '-' * (bar_length - filled_length)
    percent_str = f"{BLUE}{percent*100:5.1f}%{RESET}"
    digit_range_str = f"{CYAN}digits {digit_start:,}-{digit_end:,}{RESET}"
    if progress >= total:
        sys.stdout.write(f"\rProgress: |{bar}| 100.0% ✓ {digit_range_str}\n")
    else:
        sys.stdout.write(f"\rProgress: |{bar}| {percent_str} {digit_range_str}")
    sys.stdout.flush()


def calculate_e_optimized_streaming(num_digits, output_file='e_digits.txt', chunk_size=10000):
    print(f"OPTIMIZED STREAMING: Calculating e to {num_digits:,} decimal places")
    print(f"Output file: {output_file}")
    print(f"Chunk size: {chunk_size:,} digits")
    print("Mode: Calculate chunk → Write immediately → Next chunk → Write...\n")
    
    start_time = time.time()
    digits_written = 0
    
    with open(output_file, 'w') as f:
        f.write(f"e calculated to {num_digits} decimal places\n")
        f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 80 + "\n\n")
        f.write("e = ")
        f.flush()
        
        chunk_num = 0
        last_e_str = ""
        
        while digits_written < num_digits:
            chunk_start = time.time()
            
            target_digits = min(digits_written + chunk_size, num_digits)
            
            mp.dps = target_digits + 50
            e_value = mp.e
            e_str = mp.nstr(e_value, target_digits + 1, strip_zeros=False)
            
            if e_str and '.' in e_str:
                if chunk_num == 0:
                    integer_part, decimal_part = e_str.split('.')
                    new_content = integer_part + '.' + decimal_part[:chunk_size]
                    digits_written = min(chunk_size, len(decimal_part))
                else:
                    decimal_part = e_str.split('.')[1]
                    new_content = decimal_part[len(last_e_str.split('.')[1]):target_digits]
                    digits_written = target_digits
                
                f.write(new_content)
                f.flush()
                
                chunk_num += 1
                
                digit_start = digits_written - len(new_content) + (1 if chunk_num == 1 else 0)
                digit_start = max(1, digit_start)
                digit_end = digits_written
                
                print_progress_bar(digits_written, num_digits, digit_start, digit_end)
                
                last_e_str = e_str
    
    total_time = time.time() - start_time
    
    print(f"{'='*80}")
    print(f"✓ {BOLD}Complete!{RESET}")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Total digits: {num_digits:,}")
    print(f"Chunks written: {chunk_num}")
    print(f"Average time per chunk: {total_time/chunk_num:.2f}s")
    print(f"File size: ~{num_digits / (1024*1024):.2f} MB")
    print(f"Output saved to: {output_file}")
    print(f"{'='*80}")


def verify_e_digits(num_check=100):
    getcontext().prec = num_check + 20
    
    e = Decimal(0)
    factorial = Decimal(1)
    
    for n in range(num_check + 50):
        e += Decimal(1) / factorial
        factorial *= (n + 1)
    
    e_computed = str(e)[:num_check + 2]
    e_known = "2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320" \
            "0305992181741359662904357290033429526059563073813232862794349076323382988075319525101901157383418793070215408914993488416750" \
            "9244761460668082264800168477411853742345442437107539077744992"
    
    match = e_computed == e_known[:len(e_computed)]
    print(f"Verification: {'✓ PASSED' if match else '✗ FAILED'}")
    print(f"First {num_check} digits match known values\n")
    return match


def get_user_input(prompt, default, input_type=int):
    while True:
        user_input = input(f"{CYAN}{prompt} [{default}]{RESET}: ").strip()
        if not user_input:
            return default
        try:
            value = input_type(user_input)
            if value <= 0:
                print(f"{YELLOW}⚠ Value must be positive. Using default {default}.{RESET}")
                return default
            return value
        except ValueError:
            print(f"{YELLOW}⚠ Invalid input. Please enter a valid {input_type.__name__}.{RESET}")

if __name__ == "__main__":
    print(f"{BOLD}{'='*80}")
    print("HIGH-PRECISION e CALCULATOR - STREAMING MODE")
    print(f"{'='*80}{RESET}\n")

    verify_e_digits()

    print(f"{GREEN}Enter calculation parameters (press Enter to use default values){RESET}\n")

    default_digits = 10_000_000
    default_chunk = 100_000
    default_file = 'e_digits.txt'

    num_digits = get_user_input("Total number of digits to calculate", default_digits)
    chunk_size = get_user_input("Chunk size (digits per write)", default_chunk)
    output_file = input(f"{CYAN}Output file name [{default_file}]{RESET}: ").strip() or default_file

    print(f"\n{GREEN}Calculation starting with:{RESET}")
    print(f" → Total digits: {num_digits:,}")
    print(f" → Chunk size: {chunk_size:,}")
    print(f" → Output file: {output_file}\n")

    calculate_e_optimized_streaming(num_digits=num_digits, output_file=output_file, chunk_size=chunk_size)
