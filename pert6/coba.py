import random

# Daftar item dalam gacha dengan probabilitas masing-masing
gacha_items = {
    "Rare Item": 5,      # 5% chance
    "Uncommon Item": 25, # 25% chance
    "Common Item": 70    # 70% chance
}

def pull_gacha():
    # Membuat daftar item dan probabilitas kumulatif
    items = []
    probabilities = []
    cumulative_probability = 0

    for item, probability in gacha_items.items():
        cumulative_probability += probability
        items.append(item)
        probabilities.append(cumulative_probability)

    # Menghasilkan angka acak antara 0 dan 99
    random_number = random.randint(0, 99)

    # Menentukan item berdasarkan probabilitas
    for item, probability in zip(items, probabilities):
        if random_number < probability:
            return item

# Simulasi beberapa kali gacha pull
number_of_pulls = 10
results = []

for _ in range(number_of_pulls):
    result = pull_gacha()
    results.append(result)
    print(f"Anda mendapatkan: {result}")

# Menampilkan hasil keseluruhan
print("\nHasil Gacha:")
for item in gacha_items.keys():
    count = results.count(item)
    print(f"{item}: {count} kali")