

def number_blocks(height, block_count=0):
    if 'block_count' not in locals():
        block_count = 0
    if height <= 0:
        return block_count
    block_count += height
    return number_blocks(height - 1, block_count)

print(number_blocks(6))
