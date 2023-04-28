def engset(users, traffic, capacity, n=1, p=1.0):
    if n > capacity:
        return 1.0 / p
    denominator = (users - n) * traffic
    if denominator == 0:
        return engset(users, traffic, capacity, n + 1, p)
    p = 1.0 + p * n / denominator
    return engset(users, traffic, capacity, n + 1, p)


def max_users(block_prob_threshold, user_traffic_intensity, num_channels):
    total_traffic = 0
    num_users = 0
    while True:
        total_traffic += user_traffic_intensity
        num_users += 1
        block_prob = engset(num_users, user_traffic_intensity, num_channels)
       #print(block_prob)
        if block_prob > block_prob_threshold:
            break
    max_total_traffic = total_traffic - user_traffic_intensity
    return num_users - 1, max_total_traffic

num_channels = 2 * 30
block_prob_threshold = 0.005
user_traffic_intensity = 0.05*2

max_users_connected, max_total_traffic = max_users(block_prob_threshold, user_traffic_intensity, num_channels)
block_probability = engset(max_users_connected, user_traffic_intensity, num_channels)

print(f"Maksymalna liczba użytkowników, którzy mogą być połączeni z Hubem: {max_users_connected}")
print(f"Natężenie ruchu dla maksymalnej liczby użytkowników: {max_total_traffic:.2f} Erl")
rounded_probability = int(block_probability * 10000) / 10000 # zaokrąglenie w dół
print(f"Prawdopodobieństwo blokady: {rounded_probability:.2%}")

